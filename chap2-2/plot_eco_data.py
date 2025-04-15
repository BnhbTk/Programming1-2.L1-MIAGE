import datetime as dt
import pandas as pd
import yfinance as yf
ticker_list = {'INTC': 'Intel',
    'MSFT': 'Microsoft',
    'IBM': 'IBM',
    'BHP': 'BHP',
    'TM': 'Toyota',
    'AAPL': 'Apple',
    'AMZN': 'Amazon',
    'C': 'Citigroup',
    'QCOM': 'Qualcomm',
    'KO': 'Coca-Cola',
    'GOOG': 'Google'
}
def read_data(ticker_list,start=dt.datetime(2025, 1, 1),end=dt.datetime(2025, 4, 9)):
    """
    This function reads in closing price data from Yahoo
    for each tick in the ticker_list.
    """
    ticker = pd.DataFrame()
    for tick in ticker_list:
        stock = yf.Ticker(tick)
        prices = stock.history(start=start, end=end)
        # Change the index to date-only
        prices.index = pd.to_datetime(prices.index.date)
        closing_prices = prices['Close']
        ticker[tick] = closing_prices
    return ticker

ticker = read_data(ticker_list)
plt.plot(ticker)
plt.legend(ticker_list.values())
plt.show()
