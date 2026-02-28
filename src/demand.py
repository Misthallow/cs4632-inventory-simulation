import numpy as np

class DemandGenerator:
    def __init__(self, lam=50):
        self.lam = lam

    def sample(self):
        return np.random.poisson(self.lam)