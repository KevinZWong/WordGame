import json
import nltk
import time
class Wordgame:
        
    def __init__(self):
        self.searchLetters = ["A", "L"]
        self.user_score = 0
        self.userLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.words = nltk.corpus.words.words()
    def getWords(self):
        return self.words
    
    def getUserLetters(self):
        return self.userLetters
    def removeUserLetters(self, remove):
        self.userLetters.remove(remove)


    def getsearchLetters(self):
        return self.searchLetters
    
    def getScore(self):
        return self.user_score
    def changeScore(self, change):
        self.user_score += change
    def binary_search(self, arr, target):
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

    def displayBoard(self):
        displayScore = ""
        for i in self.searchLetters:
            displayScore += i + "..."
        displayScore = "..." + displayScore

        print("##########################################")
        print("Score: ", self.user_score)
        print(displayScore)
        print("Letters Left:", self.userLetters)
        

with open("AL_generatedWords.json", "r") as file:
    # read the JSON data from the file
    data = json.load(file)

Wordgame1 = Wordgame()
done = True
while(done):
    Wordgame1.displayBoard()
    inputuser = input("Enter a word: ").upper()
    inputuserList = list(inputuser)
    if getWord()s

        for i in inputuserList:
            if i in Wordgame1.getsearchLetters():
                

            else:
                if i in Wordgame1.getUserLetters():
                    Wordgame1.removeUserLetters(i)
                    Wordgame1.changeScore(10)
                else:
                    Wordgame1.changeScore(-5)
        if len(Wordgame1.getUserLetters()) == 0:
            done = False


Wordgame1.displayBoard()











