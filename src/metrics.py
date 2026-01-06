import numpy as np

def cagr(equity, periods_per_year=252):
    total_return = equity.iloc[-1] / equity.iloc[0]
    years = len(equity) / periods_per_year
    return total_return ** (1 / years) - 1

def max_drawdown(equity):
    roll_max = equity.cummax()
    drawdown = equity / roll_max - 1
    return drawdown.min()
    
def sharpe_ratio(returns, risk_free=0.0):
    return (returns.mean() - risk_free) / returns.std() * (252 ** 0.5)
