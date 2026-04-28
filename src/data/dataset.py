import numpy as np

def generate_dummy_data(n=100):
    X = np.random.rand(n, 1)
    y = 3 * X + 2
    return X, y