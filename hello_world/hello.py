import numpy as np


def say_hello(x: str) -> str:
    return f"Hello, {x.capitalize()}!"


def get_random_number() -> float:
    return np.random.uniform(0, 1, size=1)
