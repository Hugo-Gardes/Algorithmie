import numpy as np


def choose_signs(numbers, b):
    sorted_indices = np.argsort(-np.abs(numbers))
    S = b
    signs = np.ones_like(numbers, dtype=int)
    for idx in sorted_indices:
        if abs(S + numbers[idx]) < abs(S - numbers[idx]):
            signs[idx] = 1
            S += numbers[idx]
        else:
            signs[idx] = -1
            S -= numbers[idx]
    return signs.tolist()


rng = np.random.default_rng()
numbers = rng.normal(loc=0, scale=0.005, size=4000)
b = rng.normal(loc=0, scale=0.05)

signs = choose_signs(numbers, b)
print(signs[:10])  # Print first 10 signs
