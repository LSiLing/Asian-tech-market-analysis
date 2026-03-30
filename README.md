# Asian Tech Market Analysis

A Python data analysis project exploring price trends, volatility, and correlations
between six major Asian technology companies — TSMC, Samsung, Alibaba, Tencent,
Foxconn, and Sony — over the last 2 years.

This is one of my first Python projects, built while learning data analysis and finance fundamentals.

## What this project does

* Fetches historical price and volume data from Yahoo Finance using `yfinance`
* Cleans and preprocesses the data by forward-filling missing values
* Calculates annualized volatility based on daily returns
* Builds a correlation matrix to show how the six stocks move relative to each other
* Generates individual dashboards for each stock: price with moving averages (SMA20/SMA50), trading volume, and daily returns with volatility bands

## Key findings

* Alibaba was the most volatile stock in this period (45.90% annualized), while Sony was the most stable (29.07%)
* Tencent and Alibaba showed the strongest correlation (0.71) — likely reflecting shared exposure to Chinese market conditions
* Most other pairs had very low correlations (below 0.20), which makes sense given how differently these companies operate across different markets
* TSMC showed a strong and consistent upward trend throughout the 2-year period, with price nearly doubling — likely driven by global AI chip demand

## Charts

![Correlation Heatmap](https://raw.githubusercontent.com/LSiLing/asian-tech-market-analysis/main/stock_reports/Market_Correlation_Heatmap.png)
![TSMC](https://raw.githubusercontent.com/LSiLing/asian-tech-market-analysis/main/stock_reports/TSM_Dashboard.png)
![Samsung](https://raw.githubusercontent.com/LSiLing/asian-tech-market-analysis/main/stock_reports/005930_KS_Dashboard.png)
![Alibaba](https://raw.githubusercontent.com/LSiLing/asian-tech-market-analysis/main/stock_reports/9988_HK_Dashboard.png)
![Tencent](https://raw.githubusercontent.com/LSiLing/asian-tech-market-analysis/main/stock_reports/0700_HK_Dashboard.png)
![Foxconn](https://raw.githubusercontent.com/LSiLing/asian-tech-market-analysis/main/stock_reports/2317_TW_Dashboard.png)
![Sony](https://raw.githubusercontent.com/LSiLing/asian-tech-market-analysis/main/stock_reports/SONY_Dashboard.png)

## Technologies used

* Python 3.13
* pandas
* matplotlib
* seaborn
* yfinance

## How to run

1. Clone the repository
2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the analysis:
```
python main.py
```

## Output files

* `stock_reports/Market_Correlation_Heatmap.png` — heatmap of correlations between all six stocks
* `stock_reports/{ticker}_Dashboard.png` — individual dashboard per stock with price, volume, and volatility

## What I learned

This project helped me go further with data handling than my previous one. I chose these six companies as representatives of the biggest tech markets in Asia — not as an investment portfolio, just as an interesting dataset to work with.

The most unexpected challenge was dealing with multiple trading sessions and calendars. Stocks listed in Hong Kong, South Korea, Taiwan, and the US don't all trade on the same days, which created gaps in the data I hadn't thought about before.

I also used moving averages (SMA20/SMA50) for the first time. The math behind them is simple, but figuring out how to apply rolling calculations in pandas and then display them cleanly on a chart took more time than expected.

Building the three-panel dashboards was the most complex visualization I've done so far — combining price, volume, and daily returns in one figure pushed me to think more carefully about how to present information clearly.

The biggest technical challenge overall was working with MultiIndex DataFrames. When you download data for multiple tickers at once, pandas structures it in layers, and learning to navigate that — using `.xs()`, slicing by column level, reindexing — was genuinely new territory for me.

## Author

LSiLing | [GitHub](https://github.com/LSiLing)
