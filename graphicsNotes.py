from  graphics import *

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


def inside(point, rectangle):
    p1 = rectangle.getP1()
    p2 = rectangle.getP2()

    return  p1.getX() <= point.getX() <= p2.getX() and p1.getY() <= point.getY() <= p2.getY()


def window(c):
    print(c)
    win = GraphWin("Currency Converter", 600, 600)
    c = []
    for i in range(len(c) - 1):
        print(i)
        c = c.append(Rectangle(Point(180, (((600/range(len(c))) * (i + 1)) - 20)), Point(220, (((600/range(len(c))) * (i + 1)) + 20))))
    for i in c:
        i.drawWin()
    p = win.getMouse()
    #for i in range(le                         
    #    if not inside(p, 
    win.close()



def main():
    currencies = {"United States Dollar":1, "Euro":.99, "Peso":.055, "Chinese Yuan":.14, "Turkish Lira":.054}
    converter()
    window(currencies)


main()
    
