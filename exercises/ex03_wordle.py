"""EX03 - Structured Wordle"""

__author__ = "730451631"

def contains_char(secret: str, single_chr: str) -> bool:
    """Returns single character if in my word"""
    assert len(single_chr) == 1
    word_len: int = len(secret)
    idx: int = 0
    while idx < word_len:
        if single_chr == (secret[idx]):
            return True
        idx = idx + 1
    return False

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def emojified(guess: str, secret: str) -> str:
    """Returns emoji's that represent letter accuracy"""
    assert len(guess) == len(secret)
    emoji_sequence: str = "" 
    idx: int = 0
    while idx < len(secret):
        if secret[idx] == guess[idx]:
            emoji_sequence = emoji_sequence + GREEN_BOX
        else:
            if contains_char(secret, guess[idx]) is True:
                emoji_sequence = emoji_sequence + YELLOW_BOX    
            else:
                emoji_sequence = emoji_sequence + WHITE_BOX
        idx = idx + 1
    return emoji_sequence

def input_guess(expected_len: int) -> str:
    """returns user's guess of the correct length"""
    wordle_guess: str = input(f"Enter a {expected_len} character word: ")
    if len(wordle_guess) == expected_len:
        return wordle_guess
    else:
        while len(wordle_guess) != expected_len:
            wordle_guess = input(f"That wasn't {expected_len} chars! Try again: ")
        return wordle_guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    current_turn_number: int = 1
    secret_word = "codes"

    while current_turn_number <= 6: 
        print(f"=== Turn {current_turn_number}/6 ===")
        word_guess = input_guess(len(secret_word))
        emoji_guess = emojified(word_guess, secret_word)
        print(emoji_guess)
        current_turn_number = current_turn_number + 1
        if word_guess == secret_word:
            print(f"You won in {current_turn_number - 1}/6 turns! ")
            return
        if current_turn_number > 6:
            print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()