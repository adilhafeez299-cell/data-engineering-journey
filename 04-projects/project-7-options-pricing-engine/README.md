# Project 7: Options Pricing Engine

**Timeline:** Month 2
**Status:** Not Started

---

## Overview

A Python-based options pricing engine implementing the Black-Scholes model and binomial tree model, with full Greeks calculation (delta, gamma, theta, vega, rho). Designed to price European and American options and visualize sensitivity surfaces.

**What to Build:**
A CLI + importable library that:
- Prices European options via Black-Scholes
- Prices American options via Binomial Tree
- Calculates all 5 Greeks analytically and numerically
- Generates volatility surface and Greeks sensitivity plots
- Supports batch pricing from CSV input
- Outputs results to CSV/JSON

---

## Learning Objectives

- Implement quantitative finance models in Python
- Understand options theory (calls, puts, Greeks, put-call parity)
- Practice numerical methods (binomial tree, finite differences)
- Build a clean, importable Python library
- Demonstrate domain knowledge relevant to fintech roles

---

## Tech Stack

**Core:**
- Python 3.11+
- NumPy
- SciPy (normal distribution, optimization)
- Pandas

**Visualization:**
- Matplotlib
- Seaborn

**Supporting:**
- pytest
- argparse
- Black / pylint

---

## Success Criteria

- [ ] Black-Scholes prices match known test values
- [ ] Binomial tree converges to Black-Scholes as steps increase
- [ ] All 5 Greeks calculated correctly (delta, gamma, theta, vega, rho)
- [ ] Put-call parity holds for all test cases
- [ ] Batch pricing from CSV works end-to-end
- [ ] At least 3 visualizations (payoff diagram, Greeks surface, convergence plot)
- [ ] 80%+ test coverage
- [ ] CLI accepts spot, strike, rate, vol, expiry as arguments

---

## Project Structure

```
project-7-options-pricing-engine/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── black_scholes.py
│   ├── binomial_tree.py
│   ├── greeks.py
│   └── visualizer.py
├── tests/
│   ├── __init__.py
│   ├── test_black_scholes.py
│   ├── test_binomial_tree.py
│   └── test_greeks.py
├── data/
│   ├── input/
│   └── output/
├── notebooks/
│   └── exploration.ipynb
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Implementation Plan

### Phase 1 — Black-Scholes
- `black_scholes.py`: `call_price()`, `put_price()`, `implied_volatility()`
- Inputs: S (spot), K (strike), T (time to expiry), r (risk-free rate), sigma (volatility)

### Phase 2 — Greeks
- `greeks.py`: `delta()`, `gamma()`, `theta()`, `vega()`, `rho()`
- Both analytical (closed-form) and numerical (finite difference) implementations

### Phase 3 — Binomial Tree
- `binomial_tree.py`: `price_european()`, `price_american()`
- Configurable number of steps; convergence test against Black-Scholes

### Phase 4 — Visualization
- `visualizer.py`: payoff diagrams, Greeks vs spot price, volatility surface

### Phase 5 — CLI + Batch
- `main.py`: argparse CLI, CSV batch pricing, JSON/CSV export

---

## Key Formulas

**Black-Scholes Call:**
```
C = S * N(d1) - K * e^(-rT) * N(d2)
d1 = [ln(S/K) + (r + σ²/2)T] / (σ√T)
d2 = d1 - σ√T
```

**Delta:** dC/dS = N(d1)
**Gamma:** d²C/dS² = N'(d1) / (S * σ * √T)
**Theta:** -[S*N'(d1)*σ / (2√T)] - r*K*e^(-rT)*N(d2)
**Vega:** S * N'(d1) * √T
**Rho:** K * T * e^(-rT) * N(d2)

---

## Resources

- Options, Futures, and Other Derivatives — John Hull
- https://www.investopedia.com/terms/b/blackscholes.asp
- https://numpy.org/doc/
- https://scipy.org/
