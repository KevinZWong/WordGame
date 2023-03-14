searchLetters = [WordsList[random.randint(0, 23)], WordsList[random.randint(0, 23)]]

possibleWords = []
for i in words:
    split1 = list(i)
    wordSeachCounter = 0
    counter = 0
    for j in split1:
        if searchLetters[counter] == j:
            counter += 1
        if counter == len(searchLetters):
            possibleWords.appennd(i)
            break
    counter += 1
    print("Words Searched: ", counter)