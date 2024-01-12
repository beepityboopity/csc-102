#########################
# Program 7
# AI does 99% of the work
# ########################
# 11/5/2023
#########################

import random


# Function to choose a random word from a predefined list
def choose_word():
    file = open("words.txt")
    wordy = []
    for line in file:
        wordy.append(line)

    return random.choice(wordy)


# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


# Main function to play Hangman
def play_hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    while True:
        print(f"Word: {display_word(word_to_guess, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")

        if guess in guessed_letters:
            print("You've already guessed that letter.")

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
            if set(guessed_letters) == set(word_to_guess):
                print(f"Congratulations! You guessed the word: {word_to_guess}")
                break
        else:
            print("Wrong guess!")
            attempts -= 1
            if attempts == 0:
                print(f"You're out of attempts. The word was '{word_to_guess}'. Game over!")
                break


play_hangman()
