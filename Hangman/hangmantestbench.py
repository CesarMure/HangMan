import random

randomnumber = random.randint(1, 1000)
with open("hangman.txt") as f:
    word_list = [word.strip() for word in f]
    global word
    word = word_list[randomnumber]
    print(word)

def hangman_Stages():
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

guessed_letters = []
max_attempts = 6
attempts = 0
hidden_word = ['_'] * len(word)

while attempts < max_attempts and '_' in hidden_word:
    print(" ".join(hidden_word))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Attempts remaining: {max_attempts - attempts}")
    hangman_Stages()
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try again.")
        continue

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                hidden_word[i] = guess
    else:
        attempts += 1

    guessed_letters.append(guess)

if '_' not in hidden_word:
    print(f"Congratulations! You've guessed the word: {word}")
else:
    print(f"Sorry, you've run out of attempts. The word was: {word}")


