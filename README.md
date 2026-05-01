<img width="1254" height="1254" alt="image" src="https://github.com/user-attachments/assets/7425367d-83ca-40d2-88b4-a559f06fa77a" />

# Neurolite 🧠⚡

**Lightweight Deep Learning Framework (Built from Scratch)**

---

## 🚀 Overview

Neurolite is a minimal, educational deep learning framework built from scratch in Python.
It focuses on understanding the **core building blocks of neural networks** without relying on heavy libraries like PyTorch or TensorFlow.

This project is designed for:

* Learning deep learning internals
* Experimenting with custom architectures
* Building intuition for training pipelines

---

## 🧱 Project Structure

```text
neurolite/
│
├── src/
│   ├── core/        # Tensor, autograd engine (planned)
│   ├── nn/          # Neural network layers (Linear, Activation)
│   ├── training/    # Training loop, optimizer (planned)
│   ├── data/        # Data handling utilities
│
├── experiments/     # Training scripts and experiments
├── tests/           # Unit tests
├── docs/            # Documentation
│
├── README.md
├── requirements.txt
```

---

## ⚙️ Features

* Custom neural network layers (e.g., Linear)
* Modular design for extensibility
* Simple training scripts
* Clean, readable codebase

---

## 🧠 Example (Linear Layer Usage)

```python
from src.nn.layers import Linear

layer = Linear(3, 2)
output = layer([1.0, 2.0, 3.0])
print(output)
```

---

## 🏃 Getting Started

### 1. Create virtual environment

```bash
python -m venv neurolite
```

### 2. Activate

```bash
# Windows (PowerShell)
.\neurolite\Scripts\Activate.ps1

# Linux / Mac
source neurolite/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Training Example

```bash
python -m experiments.train_small_model
```

---

## 🧪 Roadmap

* [ ] Tensor class implementation
* [ ] Autograd engine
* [ ] Loss functions
* [ ] Optimizers (SGD, Adam)
* [ ] GPU support (future)
* [ ] Model serialization

---

## 📊 Goals

* Build intuition for deep learning internals
* Keep implementation minimal and transparent
* Enable experimentation without heavy frameworks

---

## 🏗️ Design Principles

* Simplicity over complexity
* Readability over abstraction
* Learning-first approach

---

## 📄 License

MIT License

---

## 👤 Author

Built by **Shrikrishna Das**

---






# NeuroLite

A from-scratch deep learning framework to understand AI at first principles.

## Goals
- Build neural networks without relying on high-level frameworks
- Implement backpropagation manually
- Understand transformers from scratch

## Structure
- core: tensor + autograd
- nn: layers + architectures
- training: optimizers + loss
- data: datasets

## Status
🚧 Work in progress
