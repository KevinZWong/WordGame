import random
import nltk
import random
from itertools import product
import json

#env\Scripts\activate
# download the English dictionary if you haven't already done so
#nltk.download('words')
# get the words from the English dictionary
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


#words = ['apple', "california", "potatoe", "apples"]


#searchLetters = [WordsList[random.randint(0, 23)], WordsList[random.randint(0, 23)]]
finalWord = []
split1 = []
wordSeachCounter = 0
for word in possibleWords:
    word = word.upper()
    split1 = list(word)
    
    counter = 0
    for letter in split1:
        if searchLetters[counter] == letter:
            counter += 1
        if counter == len(searchLetters):
            finalWord.append(word)
            break
    wordSeachCounter += 1
    print("Words Searched: ", wordSeachCounter)

print(len(finalWord))

#51538 correct
fileName = ""
for i in searchLetters:
    fileName += i
fileName += "_generatedWords.json"
# open a file for writing
with open(fileName, "w") as file:
    # write the data to the file in JSON format
    json.dump(finalWord, file)



