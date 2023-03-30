"""Example function for unit tests"""

# def sum(xs: list[float]) -> float:
#     """return sum of all elements in xs"""
#     sum_total: float = 0.0
#     idx: int = 0
#     while idx < len(xs):
#         sum_total += xs[idx]
#         idx += 1
#     return sum_total

# def sum(xs: list[float]) -> float:
#     sum_total: float = 0.0
#     for elem in xs:
#         sum_total += elem
#     return sum_total

def sum(xs: list[float]) -> float:
    sum_total: float = 0.0
    for idx in range(len(xs)):
        sum_total += xs[idx]
    return sum_total