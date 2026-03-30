from simulationengine import SimulationEngine
from config import get_default_config
import numpy as np
import random

base_config = get_default_config()

runs = [
    {"id": "001", "changes": {}},
    {"id": "002", "changes": {"demand_lambda": 70}},
    {"id": "003", "changes": {"demand_lambda": 30}},
    {"id": "004", "changes": {"s": 80}},
    {"id": "005", "changes": {"s": 120}},
    {"id": "006", "changes": {"S": 400}},
    {"id": "007", "changes": {"lead_time_mu": 10}},
    {"id": "008", "changes": {"lead_time_mu": 4}},
    {"id": "009", "changes": {"holding_cost": 5}},
    {"id": "010", "changes": {"shortage_cost": 100}},
]

for run in runs:
    config = base_config.copy()
    config.update(run["changes"])

    # Set seed for reproducibility
    np.random.seed(config["seed"])
    random.seed(config["seed"])

    engine = SimulationEngine(config)
    total_cost, avg_inventory, service_level = engine.run()

    run_id = run["id"]

    engine.export_timeseries(f"run_{run_id}_timeseries.csv")
    engine.export_summary(
        f"run_{run_id}_summary.json",
        total_cost,
        avg_inventory,
        service_level
    )

    print(f"Run {run_id} complete")
    print(f"  Total Cost: {total_cost}")
    print(f"  Avg Inventory: {avg_inventory}")
    print(f"  Service Level: {service_level}")
    print("-" * 40)