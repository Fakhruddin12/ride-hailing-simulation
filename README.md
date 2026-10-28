# Simulating a Ride-Hailing Service

**What happens to passenger waits, cancelled requests and driver utilisation when demand and driver availability change?**

This academic team project models the sequence from a passenger requesting a ride to matching, pickup and drop-off. Passengers can leave if they wait too long, and drivers enter and leave the service. The simulator records the resulting passenger and driver outcomes.

The contribution is the **event-driven model and its measurement framework**, rather than a claimed improvement to a real ride-hailing business. The current settings are executable, but their time-unit conventions need reconciliation before treating the simulation as calibrated to a city.

[**Simulation engine**](classes/simulation.py) · [**Repeated-run analysis**](report_analysis.py) · [**Example output**](reports/smoke_run.json) · [**Team authorship**](AUTHORS.md)

## What the model does

- Generates rider and driver arrivals and processes events in time order.
- Matches available drivers to waiting riders, then simulates pickup, travel and completion.
- Tracks rider abandonment, waiting time, driver availability and utilisation.
- Summarises earnings and utilisation dispersion and supports repeated runs to study simulation variability.

## Read the example correctly

The saved 30-minute, seed 42 execution completes 905 rides and records 123 abandonments. Those numbers show that the code runs and reports events under its configured assumptions. They are **not an operational forecast, an achieved service improvement or a fair comparison of alternative policies**.

The input names beginning `MEAN_` are passed to Python's `random.expovariate`, which expects a rate. Consequently, the original configuration produces 34.6 rider arrivals and 4.74 driver arrivals **per minute**, with a mean patience of 0.5 minutes. Driver availability is 6–8 minutes, and the default 960-minute horizon is 16 hours. These conventions are preserved explicitly instead of silently relabelled as hourly rates.

## Run a small example

From the repository root:

```bash
python scripts/run_smoke.py --minutes 30 --seed 42
```

For the full configured simulation run `python main.py`. Install `requirements.txt` and run `python report_analysis.py` for the original repeated-run analysis.

## Implementation and inputs

The [engine](classes/simulation.py) maintains the event queue and time-average state. [Event handlers](modules/handler_functions.py) implement matching and transitions, while [metrics](modules/metrics.py) compute waiting, abandonment, utilisation and dispersion.

The simulation core does not need the original spreadsheets; the exploratory notebook does. [Data instructions](DATA.md). Row-level notebook outputs are cleared in the public version. Earnings use arbitrary fare units, and their dispersion is a property of the simulation rather than proof of fairness. This is collaborative coursework; no sole-authorship claim is made.

[Portfolio](https://github.com/Fakhruddin12)
