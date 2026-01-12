import numpy as np

def cagr(equity, periods_per_year=252):
    """
    Compute Compound Annual Growth Rate (CAGR).

    Parameters
    ----------
    equity : pd.Series
        Equity curve
    periods_per_year : int
        Trading periods per year (252 for daily data)

    Returns
    -------
    float
        CAGR value, or np.nan if not computable
    """
    equity = equity.dropna() ##

    if len(equity) < periods_per_year:
        return np.nan

    start_value = equity.iloc[0]
    end_value = equity.iloc[-1]

    if start_value <= 0:
        return np.nan

    num_years = len(equity) / periods_per_year

    return (end_value / start_value) ** (1 / num_years) - 1


def max_drawdown(equity):
    roll_max = equity.cummax()
    drawdown = equity / roll_max - 1
    return drawdown.min()
    
def sharpe_ratio(returns, risk_free=0.0):
    return (returns.mean() - risk_free) / returns.std() * (252 ** 0.5)
