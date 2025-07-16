import time
import numpy as np
import matplotlib.pyplot as plt
from exercise_3_functions import function_1, function_2

"""
Measures the execution time of a function for different input values.

Args:
    func (callable): The function to be measured. It should accept a single integer argument.
    n_values (list of int): A list of integer values to be passed to the function.

Returns:
    list of float: A list of execution times corresponding to each input value in n_values.
"""


def measure_time(func, n_values):
    times = []
    for n in n_values:
        start = time.perf_counter()
        func(n)
        end = time.perf_counter()
        times.append(end - start)
    return times


n_values = [10, 20, 30, 40, 50]

times_1 = measure_time(function_1, n_values)
times_2 = measure_time(function_2, n_values)

poly_fit_1 = np.polyfit(n_values, times_1, 4)
poly_fit_2 = np.polyfit(n_values, times_2, 2)

fit_times_1 = np.polyval(poly_fit_1, n_values)
fit_times_2 = np.polyval(poly_fit_2, n_values)

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(n_values, times_1, "o-", label="Measured Times")
plt.plot(n_values, fit_times_1, "r--", label="Fitted Polynomial (degree 4)")
plt.title("Function 1: Measured vs Fitted Times")
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(n_values, times_2, "o-", label="Measured Times")
plt.plot(n_values, fit_times_2, "r--", label="Fitted Polynomial (degree 2)")
plt.title("Function 2: Measured vs Fitted Times")
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.legend()

plt.tight_layout()
plt.show()
