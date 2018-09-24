#Kapreka numbers test by Connor Williams

def Init():
    Loop(100000)

def Kaprekar(i):
    print("Test for int i =", i)
    l = len(str(i))
    j = i**2
    len_J = len(str(j))
    if(len_J == (2*l)):
        a = ExtractLastDigits(j)
        b = ExtractFirstDigits(j)
        if(a < i):
            print("Last", l, "digit(s):", a, "is/are less than", i)
            if(b < i):
                print("First", l, "digit(s):", b, "is/are less than", i)
                if(a + b == i and (len(str(a)) + len(str(b)) == 2*l)):
                    print("I =", i, "J =", j)
                    return True
    return False
       
def ExtractLastDigits(x):
    length = len(str(x))
    length = int(length / 2)
    z = int(str(x)[(-length):])
    #print(z)
    return z

def ExtractFirstDigits(x):
    length = len(str(x))
    length = int(length / 2)
    z = int(str(x)[0:length])
    #print(z)
    return z

def Loop(k):
    for i in range(0, k):
        result = Kaprekar(i)
        if(result == True):
            print("Test Passed\n")
            x = input("")
            SaveRes(i)
        else:
            print("Test Failed\n")
        i += 1

def SaveRes(i):
    s = "\n"+str(i)
    file = open("E:\Documents\GitHub\Python-Scripts\Results\Kaprekar.txt", "a")
    file.write(s)
    file.close()
Init()


