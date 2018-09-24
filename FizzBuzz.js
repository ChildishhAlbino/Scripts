var fizzNumbers = [3, 4]; //a list of numbers that multiples of will be replaced by Fizz e.g. 6 is a multiple of 3 so it'd be Fizz
var buzzNumbers = [2]; //a list of numbers that multiples of will be replaced by Buzz e.g. 6 is a multiple of 2 so it'd be Fizz + Buzz
var multipleOf = [] // an empty list that stores the multiples of for the given number (will make sense later)
var len = 30; // the length of the output, how high you want it to count
Main() // calls the function Main()

function Main() {
    for (i = 1; i < len + 1; i++) { //a loop which runs the code between the {}, increments the value "i" by 1 (i++), then checks if i is still less than len + 1 (31)
        multipleOf = [] // clears the multipleOf list that I made earlier, makes sure that any values that might've been added from the prev # are removed
        output = ""; // a string that will be our output text, right now it's empty
        output += FizzOrBuzz(i, fizzNumbers, "Fizz"); // calls the result of the method FizzOrBuzz, telling it what number to use, which numbers to compare to, and what...
        output += FizzOrBuzz(i, buzzNumbers, "Buzz"); // string to return if the number if a multiple of any one of the provided numbers. This is added to our output 
        //(Read line 29 and below and then return to here)
        if (output == "") {
            output = i;
        } else if (multipleOf.length > 0) {
            output += " (" + i + " is a multiple of "
            for (y = 0; y < multipleOf.length; y++) {
                output += multipleOf[y];
                if (multipleOf.length > 1 && y < multipleOf.length - 1) {
                    output += ", "
                }
            }
            output += ")";
        }
        console.log(output);
    }
}

function FizzOrBuzz(number, list, string) {
    var isMultipleOf = false; // a T/F statement (called a boolean) that states whether or not the value is a multiple of any of the provided numbers, set to false by default
    for (x = 0; x <= list.length; x++) { // a loop (same as on line 8) but it starts from 0 and checks if x is less than the length of the list provided... 
        //We're checking each item in the list provided   
        if (number % list[x] == 0) { // runs the code between the {} if the condition (number % list[x] == 0) is true. % means modulus or what is the remainder after dividing one number 
        //by another. If the remainder is 0, then the number is a multiple of w/e we divided by. e.g. 6 / 3 = 2 therefore 6 is a multiple of 3
            multipleOf.push(list[x]); // this adds the number we divided by into the multiplesOf list (so we can keep track of that later)
            isMultipleOf = true;           
        }
    }
    if(isMultipleOf){
        return string;
    }
    return ""
}