"""EX05 - Functions!"""

__author__ = "730451631"


def only_evens(numlist: list[int]) -> list:
    """Function for finding evens in list."""
    idx: int = 0
    evens: list[int] = list()
    while idx != len(numlist):
        if numlist[idx] % 2 == 0:
            evens.append(numlist[idx])
        idx += 1
    return evens


def concat(list1: list[int], list2: list[int]) -> list:
    """Function for concat two lists."""  
    new_list: list[int] = list(list1 + list2)
    return new_list


def sub(start_list: list[int], int1: int, int2: int) -> list:
    """Function for sub in list."""
    num_list: list[int] = list()
    if int1 < 0:
        int1: int = 0
    if int2 > len(start_list):
        int2 = len(start_list)
    if len(start_list) == 0 or int1 >= len(start_list) or int2 <= 0:
        return num_list
    for idx in range(int1, int2):
        num_list.append(start_list[idx])
    return num_list