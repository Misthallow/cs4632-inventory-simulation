import numpy as np

class Supplier:
    def __init__(self, mu=7, sigma=2):
        self.mu = mu
        self.sigma = sigma

    def sample_lead_time(self):
        return max(1, int(np.random.normal(self.mu, self.sigma)))