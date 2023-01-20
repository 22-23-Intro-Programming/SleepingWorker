def inputCheck(t, x):
    while True:
        try:
            x = t(input(x))
            break
        except ValueError:
            print("Invalid Input")
            continue
    return x


def converter():
    amount = inputCheck(float, "amount: ")
    currencies = {"United States Dollar":1, "Euro":.99, "Peso":.055, "Chinese Yuan":.14, "Turkish Lira":.054}
    x = list(currencies.keys())
    for i in range (len(x)):
        print(str(i + 1) + ". " + x[i])
    while True:
        try:
            y = inputCheck (int, "First Currency: ")
            if y < 1:
                print("Unknown Currency")
                continue
            y2 = x[y-1]
            y3 = currencies.get(y2)
            break
        except IndexError:
            print("Unknown Currency")
            continue
    while True:
        try:
            z = inputCheck (int, "Second Currency: ")
            if z < 1:
                print("Unknown Currency")
                continue
            z2 = x[z-1]
            z3 = currencies.get(z2)
            break
        except IndexError:
            print("Unknown Currency")
            continue
    print("...calculating...")
    print("You have " + str(amount*y3*(1/z3)) + " " + z2)
    
    
def groceryList(x):
    groceries = {"banana":1, "apple":1.5, "orange":1, "bagel":25}
    stuff = ""
    total = 0
    for i in x:
        stuff += i + ", "
        total += groceries.get(i)
    stuff = stuff.strip(", ")
    print("You have purchased: " + stuff)
    print("Your total is: " + str(total))



def main():
    print("----Currency Converter----")
    converter()
    groceryList(["banana", "apple", "orange"])
    


if __name__ == "__main__":
    main()
