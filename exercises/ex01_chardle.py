"""EX01 - Chardle - A cute step toward Wordle."""

_author_ = "730451631"

start_word: str = input ("Enter a 5-character word ")

if (len(start_word)<5):
    print("Error: word must contain 5 letters")
if (len(start_word)<5):
    quit()

start_letter: str = input ("Enter a single character ")
matches_found: int = 0

if (start_letter in start_word):
    print("searching" + " for " + "letter " + start_letter + " in " + start_word)
    
if (start_letter == start_word[0]):
    print(start_letter + " found at index 0 ")
    matches_found = matches_found + 1
if (start_letter == start_word[1]):
    print(start_letter + " found at index 1 ")
    matches_found = matches_found + 1
if (start_letter == start_word[2]):
    print(start_letter + " found at index 2 ")
    matches_found = matches_found + 1
if (start_letter == start_word[3]):
    print(start_letter + " found at index 3 ")
    matches_found = matches_found + 1
if (start_letter == start_word[4]):
    print(start_letter + " found at index 4 ")
    matches_found = matches_found + 1

print(str(matches_found) + " instances of " + start_letter + " found in " + start_word)