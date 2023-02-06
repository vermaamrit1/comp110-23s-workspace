"""EX01 - Chardle - One Shot Wordle - Loops."""

__author__ = "730451631"

wordle_guess: str = input("what is your 6-letter guess? ")
secret_word: str = "python"
playing: bool = True
word_count: int = len(secret_word)
guess_idx: int = 0
emoji_guess: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

if (len(wordle_guess) != len(secret_word)):
    # if the length of the guess is not equal to the length of the secret word, print:
    wordle_guess = str(input("That was not 6 letters! Try again: "))

while guess_idx < 6:
    # test if index of current guess is equal to index of secret word
    current_guess: str = secret_word[guess_idx]
    guessed_chr: bool = False
    word_idx: int = 0
    if (current_guess == wordle_guess[guess_idx]):
        # if the idx of guess matches idx of secreet word print a green box
        emoji_guess = emoji_guess + GREEN_BOX
    else:
        while guessed_chr is False and word_idx < word_count:
            # test if the idx of the guess matches any of the characters in the secret word
            if secret_word[word_idx] == wordle_guess[guess_idx]:
                guessed_chr = True
            else: 
                word_idx = word_idx + 1
        if guessed_chr is True:
            emoji_guess = emoji_guess + YELLOW_BOX
        else:
            emoji_guess = emoji_guess + WHITE_BOX

    guess_idx = guess_idx + 1
print(emoji_guess)

while playing:
    if wordle_guess == secret_word:
        print("Woo! You got it! ")
        quit()
    if len(wordle_guess) == len(secret_word):
        print("Not quite. Play again soon. ")
        playing = False