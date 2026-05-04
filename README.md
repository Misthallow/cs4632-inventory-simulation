# Discrete-Event Inventory Simulation

## Overview
This project is a discrete-event simulation of a stochastic inventory system using an (s, S) policy.  
It models customer demand, supplier lead times, and cost trade-offs in a retail supply chain environment.

The goal is to analyze how key parameters (demand rate, lead time, reorder policy, and cost structure) affect system performance.

---

## Features
- Poisson-based stochastic demand generation
- Normal-distributed supplier lead times
- (s, S) inventory control policy
- Full cost tracking (holding, ordering, shortage)
- Scenario testing and sensitivity analysis
- Visualization of system performance

---

## System Components
- Simulation Engine: Controls event flow
- Store: Tracks inventory and costs
- Supplier: Handles delayed shipments
- Inventory Policy: Implements (s, S) logic
- Demand Generator: Produces stochastic demand

---

## How to Run
python main.py
### Install dependencies:
pip install -r requirements.txt

---

## Parameters

- Demand rate (λ): controls customer demand
- Lead time (μ): supplier delay
- s: reorder threshold
- S: maximum inventory level
- Costs: holding, ordering, shortage costs

---

## Key Results
- Demand rate has the highest impact on total cost
- Lead time strongly affects service level
- Shortage cost dominates system cost behavior

---

## Author
Jasper Zheng  
CS 4632 – Modeling and Simulation  
Kennesaw State University
