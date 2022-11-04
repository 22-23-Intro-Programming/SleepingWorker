def con7(l):
    for i in range(len(l) - 1):
        if l[i] == 7 and l[i+1] == 7:
            print("hello")
            return True
    return False


def sumNot0(l):
    total = 0
    for i in l:
        if i == 0:
            break
        total += i
    return total
    

def exclude2And3(l):
    e = True
    total = 0
    for i in l:
        if i == 2:
            e = False
        elif i == 3:
            e = True
            total += i
        elif e:
            total += i
    return total


def main():
    print(con7([1, 2, 3, 4, 5, 6, 9, 7, 8, 6, 7, 7]))
    print(sumNot0([1, 2, 3, 4, 5, 0, 5, 4, 3]))
    print(exclude2And3([1, 2, 4, 5, 3, 6, 2, 4, 3, 3]))


if __name__ == "__main__":
    main()
