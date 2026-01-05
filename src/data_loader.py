import yfinance as yf
import pandas as pd

def load_data(symbol, start, end):
    df = yf.download(symbol, start=start, end=end)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    df.dropna(inplace=True)

    # Ensure proper datetime index
    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)

    return df
