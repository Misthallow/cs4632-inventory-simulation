class Store:
    def __init__(self, inventory=200):
        self.inventory = inventory
        self.holding_cost = 0
        self.ordering_cost = 0
        self.shortage_cost = 0

    def process_demand(self, demand, penalty):
        if demand <= self.inventory:
            self.inventory -= demand
        else:
            shortage = demand - self.inventory
            self.inventory = 0
            self.shortage_cost += shortage * penalty

    def add_inventory(self, qty):
        self.inventory += qty