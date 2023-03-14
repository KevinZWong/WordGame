import nltk
import random
import nltk
import random
from itertools import product

WordsList = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
words = nltk.corpus.words.words()

#searchLetters = random.choices(list(WordsList), k=2)
searchLetters = ["A", "L"]

possibleWords = []
for word in [word.upper() for word in words]:
    letter1_found = False
    letter2_found = False
    for letter in word:
        if letter == searchLetters[0]:
            letter1_found = True
        if letter == searchLetters[1]:
            letter2_found = True
        if letter1_found and letter2_found:
            possibleWords.append(word)
            break


print(len(possibleWords))
