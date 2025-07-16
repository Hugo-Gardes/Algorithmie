import numpy as np

"""
Determines the optimal signs (+1 or -1) for each element in the input array `numbers`
such that the absolute value of the sum of the elements, when multiplied by their
respective signs, is minimized.
Parameters:
numbers (np.ndarray): An array of numbers for which the signs need to be chosen.
b (float): A constant value to be added to the sum of the elements in `numbers`.
Returns:
np.ndarray: An array of signs (+1 or -1) corresponding to each element in `numbers`.
"""


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