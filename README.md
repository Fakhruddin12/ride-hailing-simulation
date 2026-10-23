# Ride-Hailing Service Simulation
### Event-driven matching, rider abandonment and driver outcomes

**Question:** How do arrival patterns, matching and driver availability affect waiting, abandonment, utilisation and the distribution of driver earnings?

This academic team project implements a discrete-event simulator with rider arrivals, driver arrivals, matching, pickup, drop-off, abandonment and driver exit. It records service and driver-level outcomes and supports repeated-seed comparisons.

## What to inspect

| Component | Purpose |
|---|---|
| [classes/simulation.py](classes/simulation.py) | Event queue, state and time-average statistics |
| [modules/handler_functions.py](modules/handler_functions.py) | Matching and event handling |
| [modules/metrics.py](modules/metrics.py) | Waits, abandonment, utilisation and dispersion |
| [report_analysis.py](report_analysis.py) | Repeated runs, intervals and plots |
| [EDA.ipynb](EDA.ipynb) | Exploratory analysis source; saved outputs cleared |

## Run a small, reproducible example

```bash
python scripts/run_smoke.py --minutes 30 --seed 42
```

The smoke run uses the original simulation settings with a shorter horizon and saves its full parameters and KPIs. It is an execution example, not a validated operational performance claim. For a full configured run use `python main.py`; for the original repeated-run analysis install `requirements.txt` and run `python report_analysis.py`.

## Units and scope

The source calls its parameters `MEAN_*`, but passes them to `random.expovariate`, which expects a **rate**. The actual original settings are 34.6 rider arrivals per minute, 4.74 driver arrivals per minute and patience rate 2 per minute (mean 0.5 minutes). Driver availability is 6–8 minutes; speed is 20 map units per minute. The 960-minute default horizon is **16 hours**.

These conventions are preserved and documented rather than silently replaced with guessed empirical parameters. They must be reconciled with the assignment's real-world units before interpreting the model as a calibrated city simulation. Driver earnings are accumulated in arbitrary fare units; earning rates in the source are per minute. Gini and other dispersion measures describe the simulated allocation, not proof of fairness.

The simulation core does not require the original spreadsheet inputs. Those inputs are needed only for the exploratory notebook and are described in [DATA.md](DATA.md). Saved notebook outputs and attachments are cleared in this public version to avoid redistributing row-level dataset excerpts. See [authorship](AUTHORS.md) for the team-work distinction.

[Portfolio](https://github.com/Fakhruddin12)
