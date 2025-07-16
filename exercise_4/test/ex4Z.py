import numpy as np


def choose_signs(numbers: np.ndarray, b: float) -> np.ndarray:
    signs = np.ones_like(numbers)
    current_sum = b + np.sum(numbers)

    indices = np.argsort(-np.abs(numbers))

    for i in indices:
        flipped_sum = current_sum - 2 * numbers[i]
        if abs(flipped_sum) < abs(current_sum):
            signs[i] = -1
            current_sum = flipped_sum

    return signs


rng = np.random.default_rng()
numbers = rng.normal(loc=0, scale=0.005, size=4000)
b = rng.normal(loc=0, scale=0.05)

signs = choose_signs(numbers, b)

print(signs[:10])
print("Nombre de +1 :", np.sum(signs == 1))
print("Nombre de -1 :", np.sum(signs == -1))
