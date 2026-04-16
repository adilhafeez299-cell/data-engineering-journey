# Project 9: Epidemic Spread Simulator

**Timeline:** Month 3
**Status:** Not Started

---

## Overview

A Python simulation of epidemic spread using the SIR (Susceptible-Infected-Recovered) compartmental model and extensions (SEIR, SIRS). Demonstrates numerical Python skills, ODE solving, parameter fitting, and data visualization.

**What to Build:**
A simulation engine that:
- Solves SIR and SEIR ODEs numerically
- Supports configurable population, transmission rate (β), recovery rate (γ)
- Fits model parameters to real or synthetic case data
- Runs Monte Carlo simulations for uncertainty quantification
- Visualizes epidemic curves, R0 sensitivity, and phase portraits
- Exports simulation results to CSV/JSON

---

## Learning Objectives

- Apply numerical methods (ODE solving) with SciPy
- Understand compartmental epidemic models
- Practice parameter estimation / curve fitting
- Demonstrate numerical Python proficiency
- Work with differential equations as data pipelines

---

## Tech Stack

**Core:**
- Python 3.11+
- NumPy
- SciPy (odeint / solve_ivp, curve_fit)
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

- [ ] SIR model produces correct epidemic curves (S+I+R = N at all times)
- [ ] SEIR extension implemented with exposed compartment
- [ ] R0 = β/γ correctly drives epidemic behaviour (R0 > 1 = outbreak)
- [ ] Parameter fitting works against synthetic noisy data
- [ ] Monte Carlo simulation runs N scenarios and reports confidence intervals
- [ ] At least 3 visualizations (epidemic curve, phase portrait, R0 sensitivity)
- [ ] 80%+ test coverage
- [ ] CLI accepts population, beta, gamma, days as arguments

---

## Project Structure

```
project-9-epidemic-simulator/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── sir.py
│   │   ├── seir.py
│   │   └── sirs.py
│   ├── simulator.py
│   ├── fitting.py
│   └── visualizer.py
├── tests/
│   ├── __init__.py
│   ├── test_sir.py
│   ├── test_seir.py
│   └── test_fitting.py
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

### Phase 1 — SIR Model
- `sir.py`: `deriv(y, t, N, beta, gamma)` — ODE system
- `simulate(N, I0, beta, gamma, days)` — returns DataFrame of S, I, R over time
- Validate: S+I+R = N at all timesteps

### Phase 2 — SEIR Extension
- `seir.py`: adds Exposed compartment E with incubation rate σ
- `simulate(N, E0, I0, beta, gamma, sigma, days)`

### Phase 3 — SIRS (Waning Immunity)
- `sirs.py`: adds immunity loss rate ξ (recovered → susceptible)

### Phase 4 — Parameter Fitting
- `fitting.py`: `fit_sir(observed_cases, N)` using `scipy.optimize.curve_fit`
- Returns estimated β, γ and R0

### Phase 5 — Monte Carlo
- `simulator.py`: `run_monte_carlo(n_runs, param_distributions)` — samples β, γ from distributions
- Returns confidence intervals for peak infection and epidemic duration

### Phase 6 — Visualization + CLI
- `visualizer.py`: epidemic curve, phase portrait (S vs I), R0 heatmap, MC confidence bands
- `main.py`: argparse CLI

---

## Key Equations

**SIR ODEs:**
```
dS/dt = -β * S * I / N
dI/dt =  β * S * I / N - γ * I
dR/dt =  γ * I
```

**Basic Reproduction Number:** R0 = β / γ
- R0 > 1: epidemic grows
- R0 < 1: epidemic dies out
- R0 = 1: endemic equilibrium

**SEIR adds:**
```
dE/dt = β * S * I / N - σ * E
dI/dt = σ * E - γ * I
```

---

## Resources

- https://scipy.org/
- Keeling & Rohani — Modeling Infectious Diseases in Humans and Animals
- https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology
