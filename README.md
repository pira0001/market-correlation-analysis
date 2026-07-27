# Market Correlation Analysis

this is a python script that pulls daily price data for one or more stock tickers, calculates daily returns, and then graphs out:

- a volatility chart for all assets that you selected
- and a set of scatter plots for the best ranked correlations

## Features

- Accepts stock tickers as comma-separated input
- Resolves ticker symbols to their company names via YFinance
- Calculates daily return correlation matrix
- Displays volatility and the charts with the best few correlation pairs 

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

## Example:

enter tickers:AAPL,MSFT,GOOG

AAPL: Apple Inc.
MSFT: Microsoft Corporation
GOOG: Alphabet Inc.

input backtest in days (max 1825): 1000

Ticker      Apple Inc.  Alphabet Inc.  Microsoft Corporation
Date                                                        
2023-11-02    2.069313       0.791724               0.650155
2023-11-03   -0.518107       1.392121               1.286173
2023-11-06    1.460503       0.828408               1.057254
2023-11-07    1.445083       0.722707               1.121939
2023-11-08    0.588491       0.649531               0.740574
...                ...            ...                    ...
2026-07-20   -2.142385       1.516815               2.150729
2026-07-21    0.352122      -1.474227              -1.128541
2026-07-22   -0.564464      -1.236315              -1.862980
2026-07-23   -1.297987      -6.893629              -2.244200
2026-07-27    4.142567       2.368511               2.961376

[682 rows x 3 columns]

Correlation:
Ticker                 Apple Inc.  Alphabet Inc.  Microsoft Corporation
                                                              
Apple Inc.                  1.000          0.395                  0.408
Alphabet Inc.               0.395          1.000                  0.378
Microsoft Corporation       0.408          0.378                  1.000


<img width="1419" height="612" alt="image" src="https://github.com/user-attachments/assets/bce1bc74-c8ad-4a05-a7b5-6f6552e36762" />
<img width="1418" height="460" alt="image" src="https://github.com/user-attachments/assets/b90cc989-b32b-4cd6-a03a-e513539dca22" />





