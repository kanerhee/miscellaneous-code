letterPoints = {
    'a':1,
    'b':3,
    'c':3,
    'd':2,
    'e':1,
    'f':4,
    'g':2,
    'h':4,
    'i':1,
    'j':8,
    'k':5,
    'l':1,
    'm':3,
    'n':1,
    'o':1,
    'p':3,
    'q':10,
    'r':1,
    's':1,
    't':1,
    'u':1,
    'v':4,
    'w':4,
    'x':8,
    'y':4,
    'z':10}

def createWordList(filename):
    file = open(filename, 'r')
    s = file.read()
    file.close()
    L = s.split('\n')
    return L

def canWeMakeIt(myWord, myLetters):
    charList = list(myLetters)          # turns myLetters into list of chars
    build = ''
    for ch in myWord:                   # iterates through each ch in myWord
        if ch not in charList:
            return False
        elif ch in charList:
            build += ch
            charList.remove(ch)
    if build == myWord:
        return True
    else:
        return False
        
def getWordPoints(myWord, letterPoints):
    points = 0
    for ch in myWord:
        points += letterPoints[ch]
    return points

def scrabbleWords(myLetters):
    wordList = createWordList('wordlist.txt')           # creates word list

    myWords = []                                        # creates list of possible words outta myLetters
    for word in wordList:
        if canWeMakeIt(word, myLetters) == True:
            myWords.append(word)
        else:
            myWords = myWords

    pointWordList = []                                  # assigns points to possible word list
    for word in myWords:
        pointValue = getWordPoints(word, letterPoints)
        pointWordList.append( (pointValue,word) )
    pointWordList.sort(reverse = True)

    sPrintToScreen = ''                                 # prints list in format
    N = len(myLetters)+4
    printForm = '{:' + str(N) + '}{}\n'
    for pair in pointWordList:
        sPrintToScreen += printForm.format(pair[1], pair[0])

    title = str(myLetters)+'.txt'                       # writes list to new file w filename
    newFile = open(title, 'w')
    newFile.write(sPrintToScreen)
    newFile.close()

    print(sPrintToScreen)
    