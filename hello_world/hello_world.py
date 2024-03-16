import numpy as np


def hello(x: str) -> str:
    return f"Hello, {x.capitalize()}!"


def random_number() -> float:
    return np.random.uniform(0, 1, size=1)
