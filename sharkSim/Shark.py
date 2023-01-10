from graphics import *
import random
import math
class Shark:

    def __init__(self, win):

        self.win = win
        self.pos = [random.randint(0,19),random.randint(0,19)]
        self.pic = Image(Point((self.pos[0] * 20) + 60, (self.pos[1] * 20) + 110), "Shark.png")
        self.pic.draw(self.win)

    def setPosition(self, x, y):
        self.pos = [x, y]

    def getPosition(self):
        return self.pos

    ''' This is how you reset the shark position'''
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
        self.pic = Image(Point((self.pos[0] * 20) + 60, (self.pos[1] * 20) + 110), "Shark.png")
        self.pic.draw(self.win)

    '''This is how the shark moves'''
    def Move(self, fishes, sharks):
        f = []
        for i in fishes:
            f.append(i.getPosition())
        s = []
        for i in sharks:
            s.append(i.getPosition())
        self.pic.undraw()
        distance = []
        p = self.pos
        for i in f:
            j = f.index(i)
            x = f[j][0] - p[0]
            y = f[j][1] - p[1]
            d = math.sqrt(x*x + y*y)
            distance.append(d)
        '''Checking for if any fish are left'''
        try:
            m = min(distance)
        except:
            self.pic.draw(self.win)
            return
        t = f[distance.index(m)]
        if m > math.sqrt(2):
            x = t[0] - p[0]
            y = t[1] - p[1]
            d = (math.sqrt(x*x + y*y)) / math.sqrt(2)
            x /= d
            y /= d
            if x > 0:    
                x = math.ceil(x)
            else:
                x = math.floor(x)
            if y > 0:
                y = math.ceil(y)
            else:
                y = math.floor(y)
            if abs(x) == abs(y):
                x = (x/abs(x))*2
                y = y/abs(y)
            self.pos = [p[0] + x, p[1] + y]
        else:
            self.pos = t
        for j in range(2):
            distance = []
            for i in f:
                j = f.index(i)
                x = f[j][0] - p[0]
                y = f[j][1] - p[1]
                d = math.sqrt(x*x + y*y)
                distance.append(d)
            if j == 1:
                '''if no fish left, returns error so instead it breaks'''
                try:
                    m = min(distance)
                    t = s[distance.index(m)]
                    if self.pos == t:
                        x = math.round(x/2 - .1)
                        y = math.round(y/2 - .1)
                        continue
                    else:
                        break
                except:
                    break
            else:
                x = -x
                y = -y
        self.pic = Image(Point((self.pos[0] * 20) + 60, (self.pos[1] * 20) + 110), "Shark.png")
        self.pic.draw(self.win)
        return
        
    
