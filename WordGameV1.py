import random

WordsList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print("WordList", WordsList)

UserList = []

while (len(UserList) != 7):
    randNum = random.randint(0,24)
    bool1 = True
    while (bool1):
        randLetter = WordsList[randNum]
        bool1 = not(randLetter in WordsList)
    UserList.append(randLetter)
print(UserList)
