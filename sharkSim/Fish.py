from graphics import *
import random
import math
class Fish:

    def __init__(self, win):

        self.pos = [random.randint(0,19),random.randint(0,19)]
        self.pic = Image(Point((self.pos[0] * 20) + 60, (self.pos[1] * 20) + 110), "Fish.png")
        self.pic.draw(win)
        self.win = win
        
    def setPosition(self, x, y):
        self.pos = [x, y]

    def getPosition(self):
        return self.pos

    ''' This is how you reset the fish position'''
    def Reset(self, l):
        while True:
            d = []
            for i in l:
                d.append(i.getPosition())
            k = 0
            for j in range(len(d)):
                if d.count(d[j]) > 1:
                    l[j].setPosition(random.randint(0,19),random.randint(0,19))
                    continue
                k += 1
            print(k)
            if k == len(d):
                break 
        self.pic.undraw()
        self.pos = [random.randint(0,19),random.randint(0,19)]
        self.pic = Image(Point((self.pos[0] * 20) + 60, (self.pos[1] * 20) + 110), "Fish.png")
        self.pic.draw(self.win)

    '''using the location of all sharks and fishes moves the fish away
    from sharks when they are within 6 blocks of the fish in a way that
    does not allow them to collide with other fishes'''
    def Move(self, sharks, fishes):
        '''makes a list 's' using the list sharks that contains the position
        values of the items in the 'sharks' list'''
        s = []
        for i in sharks:
            s.append(i.getPosition())
        '''makes a list 'f' using the list 'fishes' that contains the position
        values of the items in the 'fishes' list'''
        f = []
        for i in fishes:
            f.append(i.getPosition())
        #undraws fish image
        self.pic.undraw()
        '''finds the nearest fish to the shark using distance formula
        (sqrt(x^2 + y^2))'''
        distances = []
        p = self.pos
        for i in s:
            j = s.index(i)
            x = s[j][0] - p[0]
            y = s[j][1] - p[1]
            d = math.sqrt(x*x + y*y)
            distances.append(d)
        m = min(distances)
        t = s[distances.index(m)]
        '''This makes sure that x^2 + y^2 = 1 (Normalizing Vector)'''
        if m < 6:
            x = t[0] - p[0]
            y = t[1] - p[1]
            d = (math.sqrt(x*x + y*y))
            x /= d
            y /= d
            x *= -1
            y *= -1
            '''This rounds x and y up if above 0 and down if below 0'''
            if x > 0:    
                x = math.ceil(x)
            else:
                x = math.floor(x)
            if y > 0:
                y = math.ceil(y)
            else:
                y = math.floor(y)
            '''flips the sign of the number because the fish wants to go away
                from the shark'''
            if abs(x) == abs(y):
                x = (x/abs(x))
                y = y/abs(y)
            self.pos = [p[0] + x, p[1] + y]
        #this makes the fish move randomly when the shark
        #is more then 6 blocks away
        else:
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)
            self.pos = [p[0] + x, p[1] + y]
        #This makes sure that the fish stays in the grid
        if self.pos[0] < 0:
            self.pos[0] = 0
            x = 0
        elif self.pos[0] > 19:
            self.pos[0] = 19
            x = 0
        if self.pos[1] < 0:
            self.pos[1] = 0
            y = 0
        elif self.pos[1] > 19:
            self.pos[1] = 19
            y = 0
        #Makes sure the fish don't go on top of each other
        if f.count(self.pos) > 0:
            self.pos[0] -= x
        if f.count(self.pos) > 0:
            self.pos[1] -= y
        #this redraws the image at the new coordinates
        self.pic = Image(Point((self.pos[0] * 20) + 60, (self.pos[1] * 20) + 110), "Fish.png")
        self.pic.draw(self.win)
        return
    #Checks if there dead and makes them disappear if they are
    def CheckDie(self, sharks):
        l = []
        for i in sharks:
            l.append(i.getPosition())
        p = self.pos
        for i in l:
            if i == p:
                self.pic.undraw()
                return True
    
    
