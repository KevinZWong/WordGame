import json
import nltk
import time
import random 
from WordGeneration import WordProcessing
import copy
def binary_search( arr, target):
    # define the starting and ending indices
    left = 0
    right = len(arr) - 1
    
    # continue searching while the left index is less than or equal to the right index
    while left <= right:
        # calculate the middle index
        mid = (left + right) // 2
        
        # if the middle element is the target, return its index
        if arr[mid] == target:
            return mid
        
        # if the target is greater than the middle element, search the right half of the array
        elif arr[mid] < target:
            left = mid + 1
        
        # if the target is less than the middle element, search the left half of the array
        else:
            right = mid - 1
    
    # if the target is not found in the array, return -1
    return -1
    #start_time = time.monotonic()
    #print(binary_search(data, "PTERYGOIDAL"))
    #end_time = time.monotonic()
    #print('execution time: ', end_time - start_time)
    # open the JSON file for reading

def displayBoard(searchLetters, user_score, userLetters):
    displayScore = ""
    for i in searchLetters:
        displayScore += i + "..."
    displayScore = "..." + displayScore

    print("##########################################")
    print("Score: ", user_score)
    print(displayScore)
    print("Letters Left:", userLetters)

'''
with open("AL_generatedWords.json", "r") as file:
    # read the JSON data from the file
    data = json.load(file)
'''


WordProcessingObj = WordProcessing()
user_score = 0
userLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
searchLetters = [userLetters[random.randint(0, 24)], userLetters[random.randint(0, 24)]]
words = nltk.corpus.words.words()
dataName = WordProcessingObj.generate(searchLetters)
with open(dataName, "r") as file:
    # read the JSON data from the file
    data = json.load(file)
done = True
print("Rules:")
print("Type an enlish word that contains the letters shown Ex: ...A...L...")
print("the letters would be removed for your letters left list")
print("Getting rid of one letter that u have gets +10 points")
print("reusing a letter gets u -5 points")
print("goal is to get rid of all ur letters")
print("this kinda works, still a of bugs")
while(done):
    displayBoard(searchLetters, user_score, userLetters)
    inputuser = input("Enter a word: ").upper()
    inputuserList = list(inputuser)
    #if (binary_search(data, inputuser) != -1):
    searchLetters_copy = copy.deepcopy(searchLetters)
    print("searchLetters", searchLetters)
    print("searchLetters_copy", searchLetters_copy)
    for i in inputuserList:
        if i in userLetters:
            userLetters.remove(i)
            user_score += 10
        else:
            if (i in searchLetters_copy):
                searchLetters_copy.remove(i)
            else:
                user_score -= 5
    if len(userLetters) == 0:
        done = False
    #else:
    #    print(inputuser,"is not a valid word")


displayBoard(searchLetters, user_score, userLetters)










