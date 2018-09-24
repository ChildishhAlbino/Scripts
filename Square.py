def PrintSquare(x):
    y = x - 2
    z = 2 * x
    print(str("* "*(x-1)) + "*")

    while y > 0:
        print ("*" + (" " * (z - 3) + "*"))
        y -= 1

    print(str("* "*(x-1)) + "*")


def setLen():
    x = int(input("Enter Side Length: "))
    PrintSquare(x)
    setLen()

setLen()


    


    


