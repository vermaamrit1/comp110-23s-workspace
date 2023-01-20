"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730451631"

start_word: str = input("Enter a 5-character word: ")

if (len(start_word) < 5):
    print("Error: Word must contain 5 characters")
if (len(start_word) < 5):
    quit()
if (len(start_word) > 5):
    print("Error: Word must contain 5 characters")
if (len(start_word) > 5):
    quit()

start_letter: str = input("Enter a single character: ")
    
if (len(start_letter) > 1):
    print("Error: Character must contain a single character.")
    quit()
if (len(start_letter) < 1):
    print("Error: Character must contain a single character.")
    quit()

matches_found: int = 0

print("Searching" + " for " + start_letter + " in " + start_word)
    
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

if (matches_found == 0):
    print("No instances of " + start_letter + " found in " + start_word)
if (matches_found == 1):
    print("1 instance of " + start_letter + " found in " + start_word)
if (matches_found == 2):
    print("2 instances of " + start_letter + " found in " + start_word)
if (matches_found == 3):
    print("3 instances of " + start_letter + " found in " + start_word)
if (matches_found == 4):
    print("4 instances of " + start_letter + " found in " + start_word)
if (matches_found == 5):
    print("5 instances of " + start_letter + " found in " + start_word)