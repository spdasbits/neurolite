from src.nn.layers import Linear
from src.data.dataset import generate_dummy_data

X, y = generate_dummy_data()

model = Linear(1, 1)

for epoch in range(10):
    preds = model.forward(X)
    loss = ((preds - y) ** 2).mean()
    print(f"Epoch {epoch}, Loss: {loss}")