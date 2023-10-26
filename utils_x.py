import pymc as pm
import numpy as np
import scipy as sp

def compute_mle(model):
    results = pm.find_MAP(model=model, progressbar=False)
    return [v.item() for (k, v) in results.items() if not k.endswith('_interval__')]


def generate_data(num_samples, theta, random_state=42):
    np.random.seed(random_state)
    num_vars = len(theta)
    x_row = []
    for _ in range(num_samples):
        x = [sp.stats.bernoulli(p=theta[0]).rvs()]
        for k in range(1, num_vars):
            prob = x[k - 1] * (1 - theta[k]) + (1 - x[k - 1]) * theta[k]
            x.append(sp.stats.bernoulli(p=prob).rvs())
        x_row.append(np.array(x))
    return np.row_stack(x_row)
