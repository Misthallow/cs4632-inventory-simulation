import numpy as np
import random
import math

inventory = 200
s = 100
S = 300

holding_cost = 2
ordering_cost = 200
shortage_cost = 50

total_cost = 0

for day in range(365):

    demand = np.random.poisson(50)

    if demand <= inventory:
        inventory -= demand
    else:
        shortage = demand - inventory
        inventory = 0
        total_cost += shortage * shortage_cost

    if inventory < s:
        order_qty = S - inventory
        inventory += order_qty
        total_cost += ordering_cost

    total_cost += inventory * holding_cost

print("Simulation complete")
print("Final inventory:", inventory)
print("Total cost:", total_cost)