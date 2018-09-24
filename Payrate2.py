#WRITTEN BY CONNOR WILLIAMS github/ChildishhAlbino
#PROGRAM THAT CALCULATES A PAYCHECK GIVEN HOURS AND A PAYRATE

##DECLARATIONS##
basePay = 0
baseMlt = 0
satMlt = 0
sunMlt = 0
##DEFINITIONS##

#collects the hours worked by a person
#takes a message to prompt input
def collectHours(message):
    hours = input(message + ": ")
    if (hours == ""):
        hours = 0
    return float(hours)

#collects a base rate of pay from the user
def collectBaseRate():
    basePayRate = input("Please enter your base rate: ")
    if(basePayRate == ""):
        basePayRate = 22.76
    return float(basePayRate)

#calculates the pay for the given hours
def calcPayForHours(hours, payRate):
    pay = hours * payRate
    rounded_Pay = "%.2f" % pay 
    return rounded_Pay

def collectMultiplier(message, default):
    message = message + " (The default value is " + str(default) + ")" + ": "
    Mlt = input(str(message))
    if(Mlt == ""):
        return default
    return float(Mlt)

def Setup():
    global baseMlt
    global basePay
    global satMlt
    global sunMlt
    
    basePay = collectBaseRate()
    print("WELCOME to Payrate 2. Please enter your payrate multipliers ahead. Press enter to use the default.")
    baseMlt = collectMultiplier("Please enter your base rate", 1)
    satMlt = collectMultiplier("Please enter your Saturday rate", 1.25)
    sunMlt = collectMultiplier("Please enter your Sunday rate", 1.5)

def Main():
    global baseMlt
    global basePay
    global satMlt
    global sunMlt
    
    while(True):
        hours = 0
        hours += collectHours("Please enter your hours at base pay") * baseMlt
        hours += collectHours("Please enter your hours at Saturday pay") * satMlt
        hours += collectHours("Please enter your hours at Sunday pay") * sunMlt
        output = "You will approximately earn: $" + calcPayForHours(hours, basePay)
        print(output)

Setup()             
Main()
        
