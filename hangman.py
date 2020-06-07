import random
import string
from pathlib import Path

WORD_FILE = Path("words.txt")


def get_word_list():
    print("Getting Random Word from the wordlist...")
    with open(WORD_FILE, "r") as file:
        all_words = file.read().splitlines()
    return all_words


def choose_random_word(word_list):
    chosen_word = random.choice(word_list)
    print("Word Chosen")
    return chosen_word


def isWordGuessed(secretWord, lettersGuessed):
    check = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            check += 1
    if check == len(secretWord):
        return True
    else:
        return False


def getAvailableLetters(lettersGuessed):
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    reduced_letter_list = [
        letter for letter in alphabet if letter not in lettersGuessed
    ]
    return reduced_letter_list


def getGuessedWord(secretWord, lettersGuessed):
    total_length = len(secretWord)
    fake_string = ["*"] * total_length
    for idx, letter in enumerate(secretWord):
        if letter in lettersGuessed:
            fake_string[idx] = letter
    return "".join(fake_string)


def play_hangman(secretWord):
    mistakesLeft = 10
    wordGuessed = False
    lettersGuessed = []

    print("Welcome to Hangman!!")
    print(f"I am thinking of a word that is {len(secretWord)} letters long!")
    print("------------------------------")

    while mistakesLeft > 0 and not wordGuessed:
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            wordGuessed = True
            break
        print(f"You have {mistakesLeft} guesses left!")
        print(f"Available Letters: {' '.join(getAvailableLetters(lettersGuessed))}")
        guess = input("Guess a Letter: ").lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print("Sorry, you have already guessed this letter!")
                print("------------------------------")
            else:
                lettersGuessed.append(guess)
                print(
                    f"Fantastic selection: {getGuessedWord(secretWord, lettersGuessed)}"
                )
                print("------------------------------")
        else:
            if guess in lettersGuessed:
                print("Sorry, you have already guessed this letter!")
                print("------------------------------")
            else:
                lettersGuessed.append(guess)
                mistakesLeft -= 1
                print(
                    f"Oh No, that letter is not in the word: {getGuessedWord(secretWord, lettersGuessed)}"
                )
                print("------------------------------")

    if wordGuessed:
        print("Congrats, you guessed the word!")
        print("------------------------------")
    elif mistakesLeft == 0:
        print(f"Sorry, you ran out attempts. The word was: {secretWord}")
        print("------------------------------")


if __name__ == "__main__":
    wordList = get_word_list()
    check = True
    while check:
        secret_word = choose_random_word(wordList)
        play_hangman(secret_word)
        should_continue = input("Would you like to play again? ").lower()
        potential_yes = ["y", "yes", "true", "t"]
        if should_continue in potential_yes:
            check = True
        else:
            check = False
