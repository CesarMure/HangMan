import csv
import random

random = random.randint(0, 1000)

with open("hangman.txt") as f:
    word_list = [word.strip() for word in f]
    global word
    word = word_list[random]
    print(word)