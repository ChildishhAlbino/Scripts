from random import randint
import os
# Game for Tash by Connor Williams

people = []
actions = []

listActions = ["ADD", "REMOVE", "EXIT"]
mainMenu = ["Generate", "Edit Names", "Edit Actions"]

def Add(items, item):
    if(item in items):
        print("Item: " + item + " already in list.")
    else:
        items.append(item)
        PrintList(items, False)


def Remove(items, item):
    if(item in items):
        items.remove(item)
    else:
        if(item != None):
            print("Item: " + item + " wasn't in list.")


def EditList(items):
    # print("You are now editing the players list.")
    response = PrintList(listActions, True)
    if(response == "ADD"):
        while(True):
            inp = input("Please enter the item you want to add: ")
            if(inp == ""):
                return
            else:
                Add(items, inp.capitalize())
    elif(response == "REMOVE"):
        asking = True
        while(asking):
            ret = PrintList(items, True)
            if(ret == ""):
                asking = False
            else:
                Remove(items, ret)

    elif(response == "EXIT"):
        return


def PrintList(items, ret):
    length = len(items)
    if(length > 0):
        i = 1
        for item in items:
            print(str(i) + ". " + item)
            i += 1
        if(ret):
            try:
                i = int(input(
                    "Input the numnber that corresponds to the item you want to select: "))
                return items[i - 1]
            except ValueError:
                return ""
    else:
        print("List was empty.")
        if(ret):
            return ""


def GenerateCommand():
    if(len(people) > 0 and len(actions) > 0):
        p = randint(0, len(people)-1)
        a = randint(0, len(actions)-1)

        output = people[p] + " has to " + actions[a]
        print(output)
    else:
        print("Please supply some values.")
        PrintList(people, False)
        PrintList(actions, False)


def Main():
    command = PrintList(mainMenu, True)
    if(command == "Generate"):
        os.system('cls' if os.name == 'nt' else 'clear')
        GenerateCommand()
    elif(command == "Edit Names"):
        EditList(people)
    elif(command == "Edit Actions"):
        EditList(actions)


while(True):
    Main()
    print("\n")
