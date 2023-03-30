"""practice writing functions""""

def mimic(my_words: str) -> str:
    "given teh string my_words, outputs the same string"
    return my_words

mimic("Hello")

print(mimic("Hello"))

my_words: str = "Hello"
response: str = mimic(my_words)
print(response)

def mimic_letter(my_words: str, letter_idx: int) -> str
"""outputs the character if my_words at index_letter"""
if letter_idx >= len(my_words):
    return("Index too high")
    #if we made it here, that means the letter_idx is valid
    return my_words(letter_idx)
    
    else:
        return my_words[letter_idx
]