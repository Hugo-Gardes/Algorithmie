import numpy as np

from utils import evaluate_solution

import ex4
import ex4Z
from nic import random_sign


def main():
    rng = np.random.default_rng()
    evaluate_solution(
        solution_name="choose_signs",
        solution=ex4.choose_signs,
        rng=rng,
    )
    evaluate_solution(
        solution_name="choose_signs Z",
        solution=ex4Z.choose_signs,
        rng=rng,
    )
    evaluate_solution(
        solution_name="random_sign",
        solution=random_sign,
        rng=rng,
    )


if __name__ == "__main__":
    main()
