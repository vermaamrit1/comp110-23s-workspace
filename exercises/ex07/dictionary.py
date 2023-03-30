"""EX07 - Dictonaries!"""

__author__ = "730451631"


def invert(inputdict: dict[str, str]) -> dict[str, str]:
    """Inverts the key and value for a dict of strings."""
    outputdict = {}
    for i in inputdict:
        if i in outputdict or inputdict[i] in outputdict:
            raise KeyError("More than one of the same thing.")
        outputdict[inputdict[i]] = i
    return outputdict


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the color that appears most frequently in the dict."""
    result = ""
    coloroutput = {}
    idx = 0
    for i in colors:
        current_color = colors[i]
        if current_color in coloroutput:
            coloroutput[colors[i]] += 1
        else: 
            coloroutput[colors[i]] = 1
        if coloroutput[colors[i]] > idx:
            result = colors[i]
            idx + 1
        return result


def count(numlist: list[str]) -> dict[str, int]:
    """Returns frequency of the list from dict."""
    output = {}
    for i in numlist:
        if i in output:
            output[i] += 1
        else:
            output[i] = 1
    return output