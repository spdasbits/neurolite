import numpy as np

class Tensor:
    def __init__(self, data):
        self.data = np.array(data)
        self.grad = np.zeros_like(self.data)

    def __repr__(self):
        return f"Tensor(data={self.data}, grad={self.grad})"
    