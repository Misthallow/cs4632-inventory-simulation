def get_default_config():
    return {
        "days": 365,
        "demand_lambda": 50,
        "lead_time_mu": 7,
        "lead_time_sigma": 2,
        "s": 100,
        "S": 300,
        "holding_cost": 2,
        "ordering_cost": 200,
        "shortage_cost": 50,
        "seed": 42
    }