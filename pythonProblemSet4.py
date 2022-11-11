from button import *


class person:

    def __init__(self, win):
        self.self = self
        self.win = win
        self.eye = RectButton(self.win, Point(10, 10), Point(90, 50))
        self.face = RectButton(self.win, Point(110, 10), Point(190, 50))
        self.mouth = RectButton(self.win, Point(210, 10), Point(290, 50))
        self.nose = RectButton(self.win, Point(310, 10), Point(390, 50))
        self.QUIT = RectButton(self.win, Point(350, 350), Point(390, 390))
        self.dict = {self.eye:"eye", self.face:"face", self.mouth:"mouth", self.nose:"nose", self.QUIT:"quit"}
        self.dFace = Circle(Point(200, 200), 100)
        self.dEyeL = Circle(Point(150, 150), 25)
        self.dEyeR = Circle(Point(250, 150), 25)
        self.dNose = Rectangle(Point(175, 175), Point(225, 215))
        self.dMouth = Rectangle(Point(150, 250), Point(250, 275))
        self.eyeC = 0
        self.mouthC = 0
        self.noseC = 0
        self.faceC = 0
        

    def start(self):
        for i in [self.dFace, self.dEyeL, self.dEyeR, self.dNose, self.dMouth]:
            i.draw(self.win)
        for i in self.dict:
            i.Draw()
            i.Text(self.dict.get(i))
        self.QUIT.Color("red")
        t = Text(Point(200, 390), "Click on buttons to cycle through options")
        t.draw(self.win)
        t.setFill("blue")

    def checkClick(self, p):
        for i in self.dict:
            if(i.IsClicked(p)):
                return self.dict.get(i)
    def changeEyes(self):
        eyes = ["blue", "red", "green"]
        if self.eyeC == 2:
            self.eyeC = -1
        self.eyeC += 1
        self.dEyeR.setFill(eyes[self.eyeC])
        self.dEyeL.setFill(eyes[self.eyeC])

    def changeNose(self):
        self.dNose.undraw()
        nose = [Rectangle(Point(175, 175), Point(225, 215)), Rectangle(Point(190, 175), Point(210, 215))]
        self.noseC += 1
        if self.noseC == 2:
            self.noseC = 0
        self.dNose = nose[self.noseC]
        self.dNose.draw(self.win)
        

    def changeMouth(self):
        self.dMouth.undraw()
        mouth = [Rectangle(Point(150, 250), Point(250, 275)), Circle(Point(200, 260), 15)]
        self.mouthC += 1
        if self.mouthC == 2:
            self.mouthC = 0
        self.dMouth = mouth[self.mouthC]
        self.dMouth.draw(self.win)

    def changeFace(self):
        self.dFace.undraw()
        face = [Circle(Point(200, 200), 100), Circle(Point(200, 200), 150)]
        self.faceC += 1
        if self.faceC == 2:
            self.faceC = 0
        self.dFace = face[self.faceC]
        self.dFace.draw(self.win)

    def QUITwin(self):
        self.win.close()

        

def main():
    win = GraphWin("person", 400, 400)
    p = person(win)
    p.start()
    funcs = {'eye':p.changeEyes, 'nose':p.changeNose, 'mouth':p.changeMouth, 'face':p.changeFace, 'quit':p.QUITwin}
    while True:
        i = win.getMouse()
        j = p.checkClick(i)
        funcs.get(j)()
        if funcs.get(j) == p.QUITwin:
            break
    
        
        
        
        


main()
    
