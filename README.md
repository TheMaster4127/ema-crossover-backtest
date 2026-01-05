# EMA Crossover Backtest

A simple and modular **EMA (Exponential Moving Average) crossover backtesting project** written in Python.

This project is meant as a **learning and research foundation** for quantitative trading and time-series analysis, not as a ready-to-trade strategy.

---

## What This Project Does (So Far)

- Downloads historical price data using `yfinance`
- Calculates fast and slow EMAs
- Generates buy/exit signals based on EMA crossovers
- Runs a basic backtest with proper time-series handling
- Calculates:
  - Equity curve
  - CAGR
  - Maximum drawdown
- Plots:
  - Price with EMA overlays
  - Equity curve

---

## Strategy Logic (High Level)

- **Enter Long** when fast EMA > slow EMA  
- **Exit** when fast EMA < slow EMA  
- No short selling (long / flat only)
- Trades are executed on the **next bar** (no lookahead bias)

---

## Project Structure

```text
ema-crossover-backtest/
├── data/
├── notebooks/
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── indicators.py
│   ├── strategy.py
│   ├── backtest.py
│   └── metrics.py
├── plots/
├── main.py
├── requirements.txt
└── README.md
