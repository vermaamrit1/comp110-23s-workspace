"""EX04 - Utils."""


__author__ = "730451631"


def all(int_list: list[int], num: int) -> bool:
    """Returns if integers in list equal all."""
    idx = 0
    if len(int_list) == idx:
        return False
    else:
        while len(int_list) > idx:
            if int_list[idx] == num:
                idx = idx + 1
            else:
                return False
        return True


def max(input: list[int]) -> int:
    """Returns maximum value in list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list.")
    idx = 0
    max: int = int(input[idx])
    while len(input) != idx:
        current: int = int(input[idx])
        if max < current:
            max = current
        idx = idx + 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns if first list is identical to second list."""
    idx = 0
    if len(list1) != len(list2):
        return False
    while len(list1) != idx:
        if list1[idx] != list2[idx]:
            return False
        idx = idx + 1
    return True
    
