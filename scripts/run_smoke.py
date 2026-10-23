"""Run the existing simulator at a small horizon and preserve parameters."""
from pathlib import Path
import argparse, json, random, sys
root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root))
from classes import config
from classes.simulation import Simulation
from classes.generate_random import Distributions
from classes.event_handlers import EventHandlers

def run(minutes, seed):
    if minutes <= 0:
        raise ValueError('minutes must be positive')
    random.seed(seed)
    config.SIMULATION_LENGTH = minutes
    handlers, distributions = EventHandlers(None), Distributions(None)
    sim = Simulation(handlers, distributions)
    handlers.simulation = distributions.simulation = sim
    sim.run()
    result = {'seed': seed, 'horizon_minutes': minutes,
              'parameters': {k: getattr(config, k) for k in dir(config) if k.isupper()},
              'kpis': sim.get_results(),
              'interpretation': 'Execution example; original parameter units require calibration.'}
    out = root / 'reports/smoke_run.json'
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--minutes', type=float, default=30.)
    parser.add_argument('--seed', type=int, default=42)
    args = parser.parse_args()
    run(args.minutes, args.seed)
