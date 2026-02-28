from demand import DemandGenerator
from supplier import Supplier
from policy import InventoryPolicy
from store import Store

class SimulationEngine:

    def __init__(self, days=365):
        self.days = days

        self.store = Store()
        self.policy = InventoryPolicy()
        self.demand = DemandGenerator()
        self.supplier = Supplier()

        self.h = 2
        self.K = 200
        self.p = 50

        self.total_inventory = 0

    def run(self):
        arrival_day = None
        order_qty = 0

        for day in range(self.days):

            if arrival_day == day:
                self.store.add_inventory(order_qty)

            demand = self.demand.sample()
            self.store.process_demand(demand, self.p)

            if self.policy.should_order(self.store.inventory):
                order_qty = self.policy.order_quantity(self.store.inventory)
                arrival_day = day + self.supplier.sample_lead_time()
                self.store.ordering_cost += self.K

            self.store.holding_cost += self.store.inventory * self.h
            self.total_inventory += self.store.inventory

        total_cost = (
            self.store.holding_cost +
            self.store.ordering_cost +
            self.store.shortage_cost
        )

        avg_inventory = self.total_inventory / self.days

        return total_cost, avg_inventory