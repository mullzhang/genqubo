# Optneal

Optneal is a Python module for mathematical optimization using annealing and LP solvers.

- Typical transformation of cost function and constraints to unconstrained form.
- Useful functions for Binary Unconstrained Model(BQM).
- Leap Hybrid DQM Sampler acceptable for BQM.

## install

```
$ pip install git+https://github.com/mullzhang/optneal.git
```

## How to use

K-hot problem:

```python
import random
from optneal import Cost, Penalty

N = 10
K = 2
numbers = [random.uniform(0, 5) for _ in range(N)]
cost_dict = {i: numbers[i] for i in range(N)}
cost = Cost(cost_dict, shape=N)

constraints = [({i: 1 for i in range(N)}, K)]
penalty = Penalty(constraints, shape=N)

lam = 5.0
cost_func = cost + lam * penalty.normalize()
bqm = cost_func.to_dimod_bqm()
print(bqm)
```
