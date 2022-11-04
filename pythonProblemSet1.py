def inputAndCast(targetType, message):
    while True:
        try:
            i = targetType(input(message))
            break
        except ValueError:
            print("Invalid entry")
    return i


def problem1():
    i = inputAndCast(str, "Enter Name ")
    print("Hello " + i + " Have a good day.")


def problem2():
    x = inputAndCast(int, "input first number ")
    y = inputAndCast(int, "input second number ")
    if (x % y) == 0:
        print(str(x) + " is divisible by " + str(y))
    else:
        print(str(x) + " is not divisible by " + str(y))


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
    
