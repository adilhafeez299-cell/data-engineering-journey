# Project 8: Algorithmic Trading Backtester

**Timeline:** Month 2-3
**Status:** Not Started

---

## Overview

A Python backtesting framework that downloads historical price data, implements trading strategies, and evaluates performance with standard metrics. Built with IBKR-style thinking: clean signal generation, position sizing, and realistic transaction cost modelling.

**What to Build:**
A CLI backtesting engine that:
- Downloads OHLCV data via yfinance
- Implements at least 2 strategies (SMA crossover, RSI mean-reversion)
- Simulates trades with configurable commission and slippage
- Calculates performance metrics (Sharpe, max drawdown, CAGR, win rate)
- Outputs equity curve and trade log
- Generates performance report (CSV + charts)

---

## Learning Objectives

- Apply Python to a real quantitative finance workflow
- Understand backtesting mechanics and common pitfalls (lookahead bias, survivorship bias)
- Practice signal generation and portfolio simulation
- Demonstrate IBKR / trading domain knowledge to fintech employers
- Work with time-series data at scale using Pandas

---

## Tech Stack

**Core:**
- Python 3.11+
- Pandas
- NumPy
- yfinance (data)

**Visualization:**
- Matplotlib

**Supporting:**
- pytest
- argparse
- Black / pylint

---

## Success Criteria

- [ ] Downloads and caches historical data from yfinance
- [ ] SMA crossover strategy implemented and backtested
- [ ] RSI mean-reversion strategy implemented and backtested
- [ ] Sharpe ratio, max drawdown, CAGR, and win rate all calculated
- [ ] Transaction costs (commission + slippage) modelled
- [ ] Equity curve plotted vs buy-and-hold benchmark
- [ ] Trade log exported to CSV
- [ ] No lookahead bias in signal generation
- [ ] 80%+ test coverage
- [ ] CLI accepts ticker, date range, strategy as arguments

---

## Project Structure

```
project-8-algo-trading-backtester/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── data_loader.py
│   ├── strategies/
│   │   ├── __init__.py
│   │   ├── base_strategy.py
│   │   ├── sma_crossover.py
│   │   └── rsi_mean_reversion.py
│   ├── backtester.py
│   ├── performance.py
│   └── visualizer.py
├── tests/
│   ├── __init__.py
│   ├── test_strategies.py
│   ├── test_backtester.py
│   └── test_performance.py
├── data/
│   ├── cache/
│   └── output/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Implementation Plan

### Phase 1 — Data Layer
- `data_loader.py`: `download(ticker, start, end)`, cache to parquet locally

### Phase 2 — Strategy Framework
- `base_strategy.py`: abstract base class with `generate_signals(df)` interface
- `sma_crossover.py`: buy when fast SMA crosses above slow SMA, sell on cross below
- `rsi_mean_reversion.py`: buy when RSI < 30, sell when RSI > 70

### Phase 3 — Backtester Engine
- `backtester.py`: `run(strategy, data, initial_capital, commission, slippage)`
- Returns equity curve DataFrame and trade log

### Phase 4 — Performance Metrics
- `performance.py`: `sharpe_ratio()`, `max_drawdown()`, `cagr()`, `win_rate()`, `calmar_ratio()`

### Phase 5 — Visualization + CLI
- `visualizer.py`: equity curve, drawdown chart, monthly returns heatmap
- `main.py`: argparse CLI wiring everything together

---

## Key Concepts

**Sharpe Ratio:** (mean return - risk-free rate) / std(returns) * sqrt(252)
**Max Drawdown:** max peak-to-trough decline in equity curve
**CAGR:** (end_value / start_value)^(1/years) - 1
**Lookahead bias:** never use future data to generate a signal — always shift signals by 1 bar

---

## Resources

- yfinance docs: https://ranaroussi.github.io/yfinance/
- Quantopian lecture series (archived on GitHub)
- https://www.investopedia.com/terms/s/sharperatio.asp
