import math

class InventoryPolicy:
    def __init__(self, s=100, S=300, D=18250, K=200, H=5):
        self.s = s
        self.S = S
        self.D = D
        self.K = K
        self.H = H

    def should_order(self, inventory):
        return inventory < self.s

    def order_quantity(self, inventory):
        return self.S - inventory

    def calculate_eoq(self):
        return math.sqrt((2 * self.D * self.K) / self.H)