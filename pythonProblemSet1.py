#method that creates a user input line and checks the result to make sure it
#casts to an inputed type
def inputAndCast(targetType, message):
    while True:
        try:
            i = targetType(input(message))
            break
        except ValueError:
            print("Invalid entry")
    return i

#When called gives takes user input in the shell and outputs the inputed name
#and a greeting
def problem1():
    i = inputAndCast(str, "Enter Name ")
    print("Hello " + i + " Have a good day.")

#takes user input of 2 numbers and checks if the first one us divisible
    #by the second
def problem2():
    x = inputAndCast(int, "input first number ")
    y = inputAndCast(int, "input second number ")
    if (x % y) == 0:
        print(str(x) + " is divisible by " + str(y))
    else:
        print(str(x) + " is not divisible by " + str(y))

#takes user input and checks if it is a palindrome
#painfully
def problem3hardWay():
    first = ""
    second = ""
    input = inputAndCast(str, "input sequence to be checked ")
    length = len(input)/2
    i = 0
    while i < length:
        print(i)
        first = input[i] + first
        print(first)
        i += 1
    if (len(input) % 2) == 0:
        while i < len(input):
            print(i)
            second += input[i]
            print(second)
            i += 1
    else:
        i -= 1
        while i < len(input):
            print(i)
            second += input[i]
            print(second)
            i += 1
    if first == second:
        print("that was a palindrome")
    else:
        print("that was not a palindrome")

#not painfully takes user input and checks if its a palindrom
def problem3easyWay():
    input = inputAndCast(str, "input sequence to be checked ")
    if(input[::-1] == input):
        print("that was a palindrome")
    else:
        print("that wasn't a palindrome")
    
        
def main():
    problem1()
    problem2()
    problem3easyWay()
    problem3hardWay()


main()
    
