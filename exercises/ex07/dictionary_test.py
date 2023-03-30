"""Test for dictionary."""

__author__ = "730451631"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert() -> None:
    """Test that inverts the name of famous soccer players."""
    invert_test: dict[str, str] = {"lionel": "messi", "cristiano": "ronaldo", "neymar": "jr"}
    assert invert(invert_test) == {"messi": "lionel", "ronaldo": "cristiano", "jr": "neymar"}


def test_invert_2() -> None:
    """Test that inversts fruits and thier colors."""
    invert_test: dict[str, str] = {"apple": "red", "pear": "green", "grape": "purple"}
    assert invert(invert_test) == {"red": "apple", "green": "pear", "purple": "grape"}


def test_invert_3() -> None:
    """Test that inverts an empty dict."""
    invert_test: dict[str, str] = {}
    assert invert(invert_test) == {}


def test_favorite_color() -> None:
    """Test that returns the color of star wars character and lightsaber color."""
    favorite_color_test: dict[str, str] = {"darth vader": "black", "luke skywalker": "green", "kylo ren": "black"}
    assert favorite_color(favorite_color_test) == "black"


def test_favorite_color_2() -> None:
    """Test that returns most frequent color out of only two different values."""
    favorite_color_test: dict[str, str] = {"jake": "orange", "justin": "yellow"}
    assert favorite_color(favorite_color_test) == "orange"


def test_favorite_color_3() -> None:
    """Test that returns the string of two empty strings and values."""
    favorite_color_test: dict[str, str] = {"": "", "": ""}
    assert favorite_color(favorite_color_test) == ""


def test_count() -> None:
    """Test that counts the number of times a sport appears in the list and returns as a dict."""
    count_test: list[str] = ["football", "soccer", "tennis", "football", "football"]
    assert count(count_test) == {'football': 3, 'soccer': 1, 'tennis': 1}


def test_count_2() -> None:
    """Test that returns the dict of a blank list."""
    count_test: list[str] = []
    assert count(count_test) == {}


def test_count_3() -> None:
    """Test that returns the dict of a list full of the same values."""
    count_test: list[str] = ["mars", "mars", "mars", "mars",]
    assert count(count_test) == {'mars': 4}