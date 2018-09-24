
def Calc(x):

    # x = base rate

    y = input("Enter your hours @ base rate: ")
    if y == "":
        y = 0
    else:
        y = float(y)
    z = input("Enter your hours @ Saturday rates: ")
    if z == "":
        z = 0
    else:
        z = float(z)
    a = input("Enter your hours @ Sunday rates: ")
    if a == "":
        a = 0
    else:
        a = float(a)

    pay = ((y*x) + (1.25 * x * z) + (1.5 * x * a))   # calculates pay
    rounded_Pay = "%.2f" % pay   # rounded to 2 decimal places
    print("You will approx. earn: $" + str(rounded_Pay))   # prints to screen


def Startup():
    x = float(input("Enter your base rate: "))
    Calc(x)


while True:
    Startup()
