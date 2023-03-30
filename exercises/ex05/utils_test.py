"""Unit tests for utils."""

__author__ = "730451631"

from ex05.utils import only_evens, concat, sub


def test_only_evens() -> None:
    """Test for evens."""
    evens_list: list[int] = [2, 4, 5, 8]
    assert only_evens(evens_list) == [2, 4, 8]


def test_only_evens_odds() -> None:
    """Test two for evens in odds."""
    odds_list: list[int] = [1, 3, 5, 8]
    assert only_evens(odds_list) == [8]


def test_only_evens_empty() -> None:
    """Test for empty list."""
    empty_list: list[int] = []
    assert only_evens(empty_list) == []


def test_concat_one() -> None:
    """Test for concat decreasing values."""
    list1: list[int] = [11, 10]
    list2: list[int] = [9, 8, 7]
    assert concat(list1, list2) == [11, 10, 9, 8, 7]


def test_concat_two() -> None:
    """Test for concat single value."""
    list1: list[int] = []
    list2: list[int] = [101]
    assert concat(list1, list2) == [101]


def test_concat_none() -> None:
    """Test for concat none."""
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []


def test_sub_one() -> None:
    """Test for sub multiples of 10."""
    test_list: list[int] = [10, 100, 1000, 10000, 1000000]
    int1 = 1
    int2 = 4
    assert sub(test_list, int1, int2) == [100, 1000, 10000]


def test_sub_two() -> None:
    """Test for sub increasing by 10."""
    test_list: list[int] = [10, 20, 30, 40]
    int1 = 0
    int2 = 2
    assert sub(test_list, int1, int2) == [10, 20]


def test_sub_negative() -> None:
    """Test for sub negative numbers."""
    test_list: list[int] = [-5, -10, -15, -20]
    int1 = 0
    int2 = 2
    assert sub(test_list, int1, int2) == [-5, -10]