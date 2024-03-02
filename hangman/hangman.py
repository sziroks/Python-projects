import random
import os


def is_letter(letter: str) -> bool:
    """
    Check if user input is a single letter
    
    Parameters:
       * letter: string - user input
    Returns:
       * boolean, True if user input is a single letter, False otherwise
    """
    return True if letter.isalpha() and len(letter) == 1 else False


word_list = [
    "treatment",
    "quarter",
    "temporary",
    "draft",
    "utter",
    "vegetarian",
    "accountant",
    "house",
    "recognize",
    "edition",
]

MAX_TRIES = 10 
curr_tries = 0
used_letters: list[str] = []

word = random.choice(word_list)
word_hash = ["_" for char in word]

while "_" in word_hash and curr_tries < MAX_TRIES:
    word_hash_str = "".join(word_hash)
    print(word_hash_str)
    print(f"Used letters: {used_letters}")
    print(f"Remaining tries: {MAX_TRIES - curr_tries}")
    user_letter = input("\nInput letter: ").lower()
    valid = is_letter(user_letter)
    while not valid:
        user_letter = input("\nInvalid input, try again: ").lower()
        valid = is_letter(user_letter)

    if user_letter not in list(word):
        used_letters.append(user_letter)
        curr_tries += 1
        os.system("cls")
        continue

    for i, word_letter in enumerate(word):
        if user_letter == word_letter:
            word_hash[i] = user_letter
            used_letters.append(user_letter)

    os.system("cls")
    curr_tries += 1

if word_hash == list(word):
    print(word)
    print(f"Congratulations, you won! The word was: {word}")
else:
    print(f"You lose, the word was: {word}")
    