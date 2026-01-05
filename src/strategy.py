import pandas as pd
from src.indicators import ema


def ema_crossover_strategy(df, fast=20, slow=50):
    df = df.copy()

    df['EMA_fast'] = ema(df['Close'], fast)
    df['EMA_slow'] = ema(df['Close'], slow)

    df['Signal'] = 0
    df.loc[df['EMA_fast'] > df['EMA_slow'], 'Signal'] = 1
    df.loc[df['EMA_fast'] < df['EMA_slow'], 'Signal'] = 0

    df['Position'] = df['Signal'].diff()

    return df
