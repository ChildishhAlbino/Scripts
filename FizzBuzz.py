#FIZZBUZZ by Connor Williams

fizzNumbers = [3, 4, 7] #multiples of these numbers will become Fizz
buzzNumbers = [5] #multiples of these numbers will become Buzz
length = 100


def Main():
    #loop through numbers
    for i in range(1, length + 1):
        output = ""
        #check if multiple of fizzNumbers
        for x in range(0, len(fizzNumbers)):
            if(i % fizzNumbers[x] == 0):
                output += "Fizz"
                break            
        #check if multiple of buzzNumbers
        for x in range(0, len(buzzNumbers)):
            if(i % buzzNumbers[x] == 0):
                output += "Buzz"
                break
        #checks to see if fizz or buzz has been applied.    
        if(output == ""):
            output = str(i)
        print(output)

print("""
Playing FizzBuzz up until value = """ + str(length))      
Main()
