#BEST NOTES by Connor Williams
#calculates the best way to provide change to a person for a given
#amount of money.

#money is stores as an int as a number of cents so $10 = 1000
amount = 0
notesAvailable = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5]
bestNotes = []
calcRemainder = 0

def Main():
    while(True):
        STARTUP()
        #ask for amount (and turn into cents)
        turnToCents(askForAmount())
        #calculate best notation
        calcNotations(amount)
        #output to screen
        displayResult()

def askForAmount():
    gotInput = False
    while(gotInput == False):
        userInput = input("Please enter an amount of money in dollars: ")
        try:
            x = float(userInput)      
            gotInput = True
            return x * 100
        except ValueError:
            print("Please enter a numerical value.")

def turnToCents(x):
    global amount
    try:
        amount = int(x)
        #print(str(int(x)))
    except:
        #doesn't actually work LOL
        print("Value was more that 2 decimal places.")
    
def calcNotations(x):
    global calcRemainder
    for i in range (0, len(notesAvailable)):
        currentNoteValue = notesAvailable[i]
        if(x == 0):
            bestNotes[i] = 0
        if(x < currentNoteValue):
            #case 1: x is smaller than note: add ZERO into bestNotes
            #e.g x = 10 Note = 100
            bestNotes[i] += 0
        while (x >= currentNoteValue):   
            #case 2: x is bigger than note: subtract note from x, ADD 1 
            #to bestNotesAND loop until case
            #e.g x = 100 Note = 10
            x -= currentNoteValue
            bestNotes[i] += 1
    calcRemainder = x

def displayResult():
    display = ""
    for i in range(0, len(notesAvailable)):
        currentNoteValue = notesAvailable[i]
        currentNoteAmt = bestNotes[i]
        if(currentNoteAmt != 0):
            display += str(currentNoteAmt) + " x " + getSymboledText(currentNoteValue / 100) + "\n"            
    if(calcRemainder != 0):
        display += "and an extra " + getSymboledText(calcRemainder / 100)
    print(display)

def getSymboledText(amount):
    if(amount < 1) and (amount > 0):
        return(str(int(amount * 100)) + "c coin")
    elif (amount >= 1) and (amount <= 2):
        return("$" + str(int(amount)) + " coin")
    else:
        return("$" + str(int(amount)) + " note")
        

def STARTUP():
    bestNotes.clear()
    for i in range(0, len(notesAvailable)):
        bestNotes.append(0)

Main()
