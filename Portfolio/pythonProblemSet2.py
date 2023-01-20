#input a number when called and it prints the factorial of the number
def factorial(num):
    num = 1
    for i in range(1, num + 1):
        num *= i
    print(num)

#takes user input of a string and returns the string with every character twice
#ex.  hello  ->  hheelllloo
def doubleIt():
    word = input("word: ")
    total = ""
    for i in range(len(word)):
        total += word[i] + word[i]
    print(total)

#takes user input and returns it in camelCase format for files
#ex. Hello I am rowan/ -> helloIAmRowan-
def camel_case():
    name = input("name: ")
    name = name.title()
    name = name.replace("/", "-")
    name = name.replace(" ", "")
    #checks if first character is upper case and if it is it removes the first
    #character and replaces it with the lower case version
    if ord(name[0]) > 64 and ord(name[0]) < 91:
        x = chr(ord(name[0]) + 32)
        name = list(name)
        name.pop(0)
        new = ""
        for i in name:
            new += i
        new = x + new
    print(new)
    
#main function that runs the ones above
def main():
    print("----Problem Set 2----")
    factorial(7)
    factorial(8)
    factorial(9)
    doubleIt()
    camel_case()


if __name__ == "__main__":
    main()
