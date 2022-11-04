def factorial(num):
    num = 1
    for i in range(1, num + 1):
        num *= i
    print(num)


def doubleIt():
    word = input("word: ")
    total = ""
    for i in range(len(word)):
        total += word[i] + word[i]
    print(total)


def camel_case():
    name = input("name: ")
    name = name.title()
    name = name.replace("/", "-")
    name = name.replace(" ", "")
    if ord(name[0]) > 64 and ord(name[0]) < 91:
        x = chr(ord(name[0]) + 32)
        if name[0] == name[len(name) - 1]:
            y = name[0]
        else:
            y = ""
        name = name.strip(name[0])
        name = x + name + y
    print(name)
    

def main():
    factorial(7)
    factorial(8)
    factorial(9)
    doubleIt()
    camel_case()


main()
