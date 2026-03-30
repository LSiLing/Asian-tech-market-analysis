import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

stock_list = ['TSM', '005930.KS', '9988.HK', '0700.HK', '2317.TW', 'SONY']
names_dict = {
    'TSM': 'TSMC','005930.KS': 'Samsung', '9988.HK':'Alibaba', '0700.HK':'Tencent', '2317.TW': 'Foxconn', 'SONY': 'Sony' }

def get_stock_info():
    """
    Downloads historical Close prices and Volume for selected stocks from Yahoo Finance.
    Returns a DataFrame with MultiIndex columns (metric, ticker).
    Returns None if the download fails.
    """
    try:
        data = yf.download(stock_list, period='2y')[['Close', 'Volume']]
        return data

    except Exception as error:
        print(f'Error downloading data: {error}')
        return None

def cleaning_data(df):
    """Cleans the dataset by forward-filling missing values and removing incomplete rows."""

    close = df['Close'].ffill().dropna()
    volume = df['Volume'].fillna(0).reindex(close.index)

    return pd.concat({'Close': close, 'Volume': volume}, axis=1)

def get_daily_returns(cleaned_df):
    """
        Calculates daily percentage changes for the entire dataset.
        Used as a basis for correlation and volatility analysis.
    """
    daily_returns = cleaned_df.pct_change().dropna()
    return daily_returns

def get_volatility(daily_returns):
    """Calculates annualized volatility for each stock."""

    close_returns = daily_returns['Close']
    volatility = close_returns.std() * (252 ** 0.5)
    return volatility

def correlation_heatmap(daily_returns):
    """
    Calculates the  correlation matrix for the portfolio's daily returns.
    """

    close_returns = daily_returns['Close']
    corr = close_returns.corr()
    corr = corr.rename(columns = names_dict, index=names_dict)
    plt.figure(figsize = (10,10))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
    plt.title('Stock Market Correlation Matrix (2Y)')
    plt.savefig('stock_reports/Market_Correlation_Heatmap.png')
    plt.close()

def add_moving_average(cleaned_df, ticker):
    """Calculates 20-day and 50-day Simple Moving Averages (SMA) for a specific ticker."""

    stock_data = cleaned_df.xs(ticker, axis=1, level=1).copy()
    stock_data['SMA20'] = stock_data['Close'].rolling(20).mean()
    stock_data['SMA50'] = stock_data['Close'].rolling(50).mean()
    return stock_data

def plot_stock_dashboard(stock_data, ticker, volatility, daily_returns):


    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 8), sharex=True)

    ax1.plot(stock_data.index, stock_data['Close'], label='Price')
    ax1.plot(stock_data.index, stock_data['SMA20'], label='SMA 20')
    ax1.plot(stock_data.index, stock_data['SMA50'], label='SMA 50')

    ax2.bar(stock_data.index, stock_data['Volume'], color='gray', label='Volume')
    ax1.set_title(f'{names_dict.get(ticker, ticker)} Prices')
    ax2.set_title(f'{names_dict.get(ticker, ticker)} Volume')

    ax1.legend()
    ax2.legend()

    ax3.plot(daily_returns.index, daily_returns, color='steelblue', alpha=0.5, label='Daily Returns')
    daily_vol = volatility / (252 ** 0.5)
    ax3.axhline(y=daily_vol, color='red', linestyle='--',
                label=f'Daily Volatility: {daily_vol:.2%} (Ann: {volatility:.2%})')
    ax3.axhline(y=-daily_vol, color='red', linestyle='--')
    ax3.set_title(f'{names_dict.get(ticker, ticker)} Daily Returns & Volatility')
    ax3.legend()

    plt.tight_layout()
    plt.savefig(f'stock_reports/{ticker}_Dashboard.png')
    plt.close()

def main():
    df = get_stock_info()
    if df is not None and not df.empty:

        folder_name = 'stock_reports'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)


        cleaned_df = cleaning_data(df)
        returns = get_daily_returns(cleaned_df)
        correlation_heatmap(returns)
        volatility = get_volatility(returns)

        for ticker in stock_list:
            stock_data = add_moving_average(cleaned_df, ticker)
            ticker_volatility = volatility[ticker]
            ticker_returns = returns['Close'][ticker]
            plot_stock_dashboard(stock_data, ticker, ticker_volatility, ticker_returns)
    else:
        print('Data download unsuccessful.')
        
if __name__ == '__main__':

    main()

