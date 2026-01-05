import numpy as np

def backtest(df, initial_capital=100000):
    df = df.copy()

    df['Returns'] = df['Close'].pct_change()
    df['Strategy_Returns'] = df['Returns'] * df['Signal'].shift(1)

    df['Equity'] = (1 + df['Strategy_Returns']).cumprod() * initial_capital

    return df
