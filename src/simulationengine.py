import csv
import json
from demand import DemandGenerator
from supplier import Supplier
from policy import InventoryPolicy
from store import Store


class SimulationEngine:

    def __init__(self, config):
        self.config = config
        self.days = config["days"]

        self.store = Store()
        self.policy = InventoryPolicy(s=config["s"], S=config["S"])
        self.demand = DemandGenerator(lam=config["demand_lambda"])
        self.supplier = Supplier(
            mu=config["lead_time_mu"],
            sigma=config["lead_time_sigma"]
        )

        self.h = config["holding_cost"]
        self.K = config["ordering_cost"]
        self.p = config["shortage_cost"]

        self.total_inventory = 0
        self.total_demand = 0
        self.total_shortage = 0

        self.time_series = []

    def run(self):
        arrival_day = None
        order_qty = 0

        for day in range(self.days):

            # Receive order if it arrives
            if arrival_day == day:
                self.store.add_inventory(order_qty)
                arrival_day = None

            # Demand occurs
            demand = self.demand.sample()
            self.total_demand += demand

            shortage = self.store.process_demand(demand, self.p)
            self.total_shortage += shortage

            # Place order if needed (and no pending order)
            if arrival_day is None and self.policy.should_order(self.store.inventory):
                order_qty = self.policy.order_quantity(self.store.inventory)
                arrival_day = day + self.supplier.sample_lead_time()
                self.store.ordering_cost += self.K

            # Holding cost
            self.store.holding_cost += self.store.inventory * self.h

            # Track averages
            self.total_inventory += self.store.inventory

            # Time-series logging
            self.time_series.append({
                "day": day,
                "inventory": self.store.inventory,
                "demand": demand,
                "shortage": shortage,
                "holding_cost": self.store.holding_cost,
                "ordering_cost": self.store.ordering_cost,
                "shortage_cost": self.store.shortage_cost
            })

        total_cost = (
            self.store.holding_cost +
            self.store.ordering_cost +
            self.store.shortage_cost
        )

        avg_inventory = self.total_inventory / self.days

        service_level = 1 - (self.total_shortage / self.total_demand) if self.total_demand > 0 else 1

        return total_cost, avg_inventory, service_level

    def export_timeseries(self, filename):
        if not self.time_series:
            return

        keys = self.time_series[0].keys()
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.time_series)

    def export_summary(self, filename, total_cost, avg_inventory, service_level):
        summary = {
            "total_cost": total_cost,
            "avg_inventory": avg_inventory,
            "service_level": service_level,
            "parameters": self.config
        }

        with open(filename, "w") as f:
            json.dump(summary, f, indent=4)