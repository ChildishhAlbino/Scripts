from random import randint
import os
#Game for Tash by Connor Williams

newAcommand = {"action", "a", "command", "newa"}
newPcommand = {"person", "p", "name", "newp"}

people = []
actions = []

def AskForAction():
    asking = True
    print("You are now editing the actions list. You can only ADD actions currently.")
    print("Enter as many actions as you'd like. Press enter to quit editing.")
    while(asking):   
        action = input("Please enter an action: ")
        if(action == ""):
            asking = False
        else:        
            actions.append(action)
            print(str(actions))


def AskForPerson():
    asking = True
    print("You are now editing the players list. You can only ADD players currently.")
    print("Enter as many names as you'd like. Press enter to quit editing.")
    while(asking):   
        person = input("Please enter an person's name: ")
        if(person == ""):
            asking = False
        else:        
            people.append(person)
            print(str(people))

def GenerateCommand():
    if(len(people) > 0 and len(actions) > 0):    
        p = randint(0, len(people)-1)
        a = randint(0, len(actions)-1)

        output = people[p] + " has to " + actions[a]
        print(output)
    else:
        print("Please supply some values.")
        print(str(actions))
        print(str(people))

def Main():
    command = input("Press enter to generate a new result: ")
    if(command == ""):
        os.system('cls' if os.name == 'nt' else 'clear')
        GenerateCommand()
    elif(command.lower() in newPcommand):
        AskForPerson()
    elif(command.lower() in newAcommand):
        AskForAction()
        


while(True):
    Main()
    
