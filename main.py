import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from itertools import combinations
import numpy as np

user_input = input(
    "input must be seperated by commas:"
)

markets = user_input.split(",") #turns into readable list 

markets = [market.strip().upper() for market in markets] #cleans tickers 

market_names = {}

for ticker in markets: #this is to obtain the name of the ticker
    try:
        ticker_information = yf.Ticker(ticker).info
        name = (
            ticker_information.get("shortName")
            or ticker_information.get("longName")
            or ticker
        )
    except Exception:
        name = ticker

    market_names[ticker] = name
    print(f"{ticker}: {name}")

backtest_days = int(
    input("input backtest in days (max 1825): ")
)

if backtest_days <= 30:     #preparation to efficiently retrieve the data requested. still long-winded but idk how to improve 
    download_period = "1mo"
elif backtest_days <= 90:
    download_period = "3mo"
elif backtest_days <= 180:
    download_period = "6mo"
elif backtest_days <= 365:
    download_period = "1y"
elif backtest_days <= 730:
    download_period = "2y"
else:
    download_period = "5y"

data = yf.download(
    markets,
    period=download_period,
    interval="1d",
    auto_adjust=True,
    progress=False
)

prices = data["Close"]

start_date = datetime.now() - timedelta(days=backtest_days) #calculates x calendar days from today 

prices = prices[prices.index >= start_date] #trims off extra data from the yf boundary 
ill_method='None'
daily_returns = prices.pct_change().dropna() * 100 #dropna removes all the null data
daily_returns = daily_returns.rename(
    columns=lambda column: market_names.get(column, column)
)

print(daily_returns)

corr_matrix = daily_returns.corr()
print("\nCorrelation:")
print(corr_matrix.round(3))

ranked_relationships = []

for a, b in combinations(daily_returns.columns, 2): #calculating correlation for the unique pairs
    correlation = daily_returns[a].corr(daily_returns[b])
    ranked_relationships.append((a, b, correlation))


def get_strength(relationship):
    return abs(relationship[2])


ranked_relationships.sort(key=get_strength, reverse=True)

daily_volatility = daily_returns.std() #volatility for the whole thing is calculated from the std

volatility_text = "Daily volatility\n"

for market, volatility in daily_volatility.items():
    volatility_text += f"{market}: {volatility:.2f}%\n"


top_relationships = ranked_relationships[:4]

volatility_fig, volatility_axis = plt.subplots(figsize=(13, 4.2), dpi=110)
daily_returns.plot(ax=volatility_axis)

volatility_axis.axhline(0, linewidth=1)
volatility_axis.set_title(
    f"Volatility (measured as percentage change) over the last {backtest_days} days"
)
volatility_axis.set_xlabel("Date")
volatility_axis.set_ylabel("Daily percentage change (%)")
volatility_axis.legend(title="Market")

volatility_axis.text(
    0.99,
    0.98,
    volatility_text,
    transform=volatility_axis.transAxes,
    horizontalalignment="right",
    verticalalignment="top",
    bbox={
        "boxstyle": "round",
        "facecolor": "black",
        "alpha": 0.8,
    },
)

volatility_fig.tight_layout()
volatility_fig.canvas.manager.set_window_title("Volatility")
volatility_fig.show()
plt.pause(0.001)

num_pairs = len(top_relationships)
rows = max(1, int(np.ceil(num_pairs / 2)))
scatter_fig, axes = plt.subplots(
    nrows=rows,
    ncols=2,
    figsize=(13, max(4.2, rows * 2.8)),
    dpi=110,
)
axes = np.array(axes).flatten()

for axis in axes[num_pairs:]:
    axis.axis("off")

for rank, relationship in enumerate(top_relationships, start=1):
    market_a, market_b, correlation = relationship

    x_returns = daily_returns[market_a]
    y_returns = daily_returns[market_b]

    slope, intercept = np.polyfit(x_returns, y_returns, 1)

    x_line = np.sort(x_returns)
    y_line = slope * x_line + intercept

    axis = axes[rank - 1]

    axis.scatter(x_returns, y_returns, alpha=0.6)
    axis.plot(x_line, y_line)
    axis.axhline(0, linewidth=1)
    axis.axvline(0, linewidth=1)

    axis.set_title(
        f"Rank {rank}: {market_a} vs {market_b}\n"
        f"Correlation: {correlation:.3f}"
    )
    axis.set_xlabel(f"{market_a} daily change (%)")
    axis.set_ylabel(f"{market_b} daily change (%)")

scatter_fig.tight_layout()
scatter_fig.canvas.manager.set_window_title("Scatter Plots")
scatter_fig.show()
plt.show()

