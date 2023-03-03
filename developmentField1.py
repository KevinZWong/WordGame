import nltk
import random
#env\Scripts\activate
# download the English dictionary if you haven't already done so
#nltk.download('words')
# get the words from the English dictionary

WordsList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

words = nltk.corpus.words.words()

done = True

while(done):
    firstLetter = WordsList[random.randint(0, 23)]
    secondLetter = WordsList[random.randint(0, 23)]
    possibleWords = []
    for i in words:
        if (firstLetter in i and secondLetter in i):
            possibleWords.append(i)
    if (len(possibleWords) > 200):
        done = False
print("firstLetter", firstLetter)
print("secondLetter", secondLetter)
print(possibleWords)