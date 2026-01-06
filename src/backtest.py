def backtest(df, initial_capital=100000, cost_per_trade=0.0005):
    df = df.copy()

    df['Returns'] = df['Close'].pct_change()
    df['Strategy_Returns'] = df['Returns'] * df['Signal'].shift(1)

    df['Position_Change'] = df['Signal'].diff().abs()
    df['Costs'] = cost_per_trade * df['Position_Change']

    df['Strategy_Returns'] -= df['Costs']
    df['Equity'] = (1 + df['Strategy_Returns']).cumprod() * initial_capital

    return df
