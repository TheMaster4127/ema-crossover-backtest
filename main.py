import matplotlib.pyplot as plt
from src.data_loader import load_data
from src.strategy import ema_crossover_strategy
from src.backtest import backtest
from src.metrics import cagr, max_drawdown
from src.metrics import sharpe_ratio

df = load_data("NVDA", "2015-01-01", "2026-01-01")
df = ema_crossover_strategy(df)
df = backtest(df)

print("CAGR:", cagr(df['Equity']))
print("Max Drawdown:", max_drawdown(df['Equity']))
print("Sharpe:", sharpe_ratio(df['Strategy_Returns'].dropna()))

df[['Close', 'EMA_fast', 'EMA_slow']].plot(figsize=(12,6))
plt.show()

df['Equity'].plot(title="Equity Curve", figsize=(12,6))
plt.show()


