import csv
import random
import sys

guessed_letters = ""
remaining_attempts =6

def hangman_Stages():
    global remaining_attempts
    max_attempts = 7
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    return HANGMANPICS[max_attempts - remaining_attempts]

#selets a random number between 1 and 1000 as 1000 line long text file
random = random.randint(0, 1000)
with open("hangman.txt") as f:
    word_list = [word.strip() for word in f]
    global word
    word = word_list[random]
    print(word)



def print_word():
    print(" _ " * len(word))

print("Welcome to Hangman! Let's see if you can guess this word!\n")
guess = input("Guess a letter: ")


def is_guess_in_word(guess, word):
    guessed = False
    if len(guess) > 1 or not guess.isalpha():
        print("Only single letters allowed, unable to continue")
        sys.exit()
    else:
        if guess in word:
            return True
        else:  
            return False

guess_in_secret_word = guess(guess, word)

guess()
