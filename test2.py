import random

WordsList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

firstLetter = WordsList[random.randint(0, 23)]
secondLetter = WordsList[random.randint(0, 23)]

print("firstLetter", firstLetter)
print("secondLetter", secondLetter)