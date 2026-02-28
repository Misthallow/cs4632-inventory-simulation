# Inventory Management Simulation
**CS 4632 – Modeling and Simulation**  
Jasper Zheng

---

## Project Overview
This project implements a **discrete-event simulation** of a retail inventory system operating under stochastic customer demand and uncertain supplier lead times.

The objective is to evaluate and compare inventory control policies and measure their impact on:

- Total cost
- Holding cost
- Ordering cost
- Shortage cost
- Stockout rate
- Service level (fill rate)
- Average inventory

---

## Milestone 2 Status

### Implemented
- Discrete-event simulation engine
- Event scheduling (demand + shipment arrivals)
- Stochastic demand generation (Poisson distribution)
- (s, S) inventory control policy
- EOQ analytical baseline
- Stochastic lead time modeling
- Cost and performance metric tracking
- Console output of simulation results

### In Progress
- Policy comparison experiments
- Visualization graphs
- Parameter tuning

### Planned
- Statistical analysis of results
- Additional testing scenarios
- Extended reporting

---

## Repository Structure

src/ – Python simulation source code  
docs/ – UML diagrams and screenshots  
main.tex – LaTeX report  
references.bib – bibliography  
requirements.txt – dependencies  
README.md – project documentation  

## Installation

Install Python 3.10+ and run: 
pip install -r requirements.txt

---

## Running the Simulation
python src/main.py


The program prints inventory performance metrics to the console.

---

## Models Implemented

### Stochastic Demand
Daily demand:
Poisson(λ = 50 units/day)

### (s, S) Policy
If inventory < s → order up to S  
Example: s = 100, S = 300

### EOQ
Q* = sqrt(2DS / H) used as analytical comparison

### Lead Time
Normally distributed: mean 7 days, std 2 days

---

## Author
Jasper Zheng  
CS 4632 – Modeling and Simulation  
Kennesaw State University
