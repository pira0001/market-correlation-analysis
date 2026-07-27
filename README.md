# FXCM Market Correlation Analyzer

this is a python script that pulls daily price data for one or more stock tickers, calculates daily returns, and then graphs out:

- a volatility chart for all assets that you selected
- and a set of scatter plots for the best ranked correlations

## Features

- Accepts stock tickers as comma-separated input
- Resolves ticker symbols to their company names via Yahoo Finance
- Calculates daily return correlation matrix
- Displays volatility and the charts with the best correlation pairs 

## Requirements

Install the dependencies:

```bash
pip install yfinance matplotlib numpy
```

## Usage

Run the script:

```bash
python main.py
```

Then provide:

1. A comma-separated list of tickers (for example: `AAPL,MSFT,GOOG`)
2. A backtest length in days (up to 1825)

## Output

The script prints:

- the resolved ticker names
- a daily % change table 
- a correlation matrix for all combinations 

It also opens two charts:

- a volatility chart
- a scatter-plot window for the top correlation pairs

This was an initial project to help me build and understand the foundation of matplotlib and using yfinance for coding a future forex strategy.
