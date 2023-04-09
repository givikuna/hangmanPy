input_ = input("Enter a sentence or a word: ")
trueLetters = []
chosenLetters = []
turns = 6
def currentString():
    s = ""
    for i in input_:
        if i in chosenLetters:
            s += i
        elif i == " ":
            s += " "
        else:
            s += "_"
    return s

def isDone():
    if "_" not in currentString():
        return True
    return False

for i in input_:
    trueLetters.append(i)
while True:
    print(currentString())
    print("you have ", turns, " lives left")
    chosenLetter = input("Choose a letter: ")
    if chosenLetter in chosenLetters:
        print("The letter has already been entered")
        continue
    if chosenLetter not in trueLetters:
        turns -= 1
        print("Wrong!")
    else:
        chosenLetters.append(chosenLetter)
        print("Correct!")
    if turns == 0 or isDone():
        break
 
if isDone():
    print("You won!")
else:
    print("Take the L!")
