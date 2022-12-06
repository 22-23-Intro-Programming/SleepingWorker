from button import *

def darken(im, b):
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            pix = im.getPixel(j, i)
            if pix != b:
                p = color_rgb(int(pix[0]*.75), int(pix[1]*.75), int(pix[2]*.75))
                im.setPixel(j, i, p)

def lighten(im, b):
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            pix = im.getPixel(j, i)
            if pix != b: 
                rgb = [(255 - pix[0]) / 2, (255 - pix[1]) / 2, (255 - pix[2]) / 2]
                p = color_rgb(int(pix[0] + rgb[0]), int(pix[1] + rgb[1]), int(pix[2] + rgb[2]))
                im.setPixel(j, i, p)

def grayScale(im, b):
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            pix = im.getPixel(j, i)
            if pix != b:
                av = (pix[0] + pix[1] + pix[2])/3
                p = color_rgb(int(av), int(av), int(av))
                im.setPixel(j, i, p)
def contrast(im, b):
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            pix = im.getPixel(j, i)
            if pix != b:
                av = (pix[0] + pix[1] + pix[2])/3
                p = color_rgb(int(av), int(av), int(av))
                if av > 127:
                    rgb = [(255 - pix[0]) / 2, (255 - pix[1]) / 2, (255 - pix[2]) / 2]
                    p = color_rgb(int(pix[0] + rgb[0]), int(pix[1] + rgb[1]), int(pix[2] + rgb[2]))
                    im.setPixel(j, i, p)
                else:
                    p = color_rgb(int(pix[0]*.75), int(pix[1]*.75), int(pix[2]*.75))
                    im.setPixel(j, i, p)

def superContrast(im, b):
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            pix = im.getPixel(j, i)
            if pix != b:
                av = (pix[0] + pix[1] + pix[2])/3
                '''if av < 86:
                    im.setPixel(j, i, color_rgb(0, 0, 0))
                elif av < 171:
                    im.setPixel(j, i, color_rgb(127, 127, 127))
                else:
                    im.setPixel(j, i, color_rgb(225, 225, 225))'''
                if av > 127:
                    im.setPixel(j, i, color_rgb(225, 225, 225))
                else:
                    im.setPixel(j, i, color_rgb(0, 0, 0))

def redBoost(im, b):
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            pix = im.getPixel(j, i)
            if pix != b:
                if (pix[0] > (pix[1] + 25)) and (pix[0] > (pix[2] + 25)):
                    continue
                else:
                    av = (pix[0] + pix[1] + pix[2])/3
                    p = color_rgb(int(av), int(av), int(av))
                    im.setPixel(j, i, p)

def greenBoost(im, b):
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            pix = im.getPixel(j, i)
            if pix != b:
                if (pix[1] > (pix[0])) and (pix[1] > (pix[2])):
                    continue
                else:
                    av = (pix[0] + pix[1] + pix[2])/3
                    p = color_rgb(int(av), int(av), int(av))
                    im.setPixel(j, i, p)

def blueBoost(im, b):
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            pix = im.getPixel(j, i)
            if pix != b:
                if (pix[2] > (pix[0] + 25)) and (pix[2] > (pix[1] + 25)):
                    print("found one")
                    continue
                else:
                    av = (pix[0] + pix[1] + pix[2])/3
                    p = color_rgb(int(av), int(av), int(av))
                    im.setPixel(j, i, p)

def blur(im, b):
    colors = []
    k = 0
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            pix = im.getPixel(j, i)
            if pix != b:
                try:
                    up = im.getPixel(j+1, i)
                except:
                    up = im.getPixel(j, i)
                try:
                    down = im.getPixel(j-1, i)
                except:
                    down = im.getPixel(j, i)
                try:
                    right = im.getPixel(j, i+1)
                except:
                    right = im.getPixel(j, i)
                try:
                    left = im.getPixel(j, i-1)
                except:
                    left = im.getPixel(j, i)
                av1 = int((up[0] + down[0] + right[0] + left[0])/4)
                av2 = int((up[1] + down[1] + right[1] + left[1])/4)
                av3 = int((up[2] + down[2] + right[2] + left[2])/4)
                av4 = [av1, av2, av3]
                colors.append(av4)
            else:
                colors.append(b)
    for i in range(im.getHeight()):
        for j in range(im.getWidth()):
            im.setPixel(j, i, color_rgb(colors[k][0], colors[k][1], colors[k][2]))
            k += 1

def edge(im, b):
    #superContrast(im, b)
    colors = []
    k = 0
    for i in range(1, im.getHeight() - 1, 1):
        for j in range(1, im.getWidth() - 1, 1):
            pix = im.getPixel(j, i)
            if pix != b:
                av = (pix[0] + pix[1] + pix[2])/3
                up = im.getPixel(j+1, i)
                down = im.getPixel(j-1, i)
                right = im.getPixel(j, i+1)
                left = im.getPixel(j, i-1)
                if (abs(pix[0] - up[0]) > 25) or (abs(pix[0] - down[0]) > 25) or (abs(pix[0] - right[0]) > 25) or (abs(pix[0] - left[0]) > 25):
                    colors.append(1)
                elif (abs(pix[1] - up[1]) > 25) or (abs(pix[1] - down[1]) > 25) or (abs(pix[1] - right[1]) > 25) or (abs(pix[1] - left[1]) > 25):
                    colors.append(1)
                elif (abs(pix[2] - up[2]) > 25) or (abs(pix[2] - down[2]) > 25) or (abs(pix[2] - right[2]) > 25) or (abs(pix[2] - left[2]) > 25):
                    colors.append(1)
                else:
                    colors.append(0)
            else:
                colors.append(0)
    for i in range(1, im.getHeight() - 1, 1):
        for j in range(1, im.getWidth() - 1, 1):
            if colors[k] == 1:
                im.setPixel(j, i, color_rgb(0, 0, 0))
            else:
                im.setPixel(j, i, color_rgb(255, 255, 255))
            k+=1
                    
                
                
                
                
                
                
        

def main():
    background = color_rgb(50, 50, 100)
    b = [0, 0, 0]
    win = GraphWin("Image Editor", 800, 800)
    win.setBackground(background)

    I = Image(Point(400, 450), "ball.png")
    I.draw(win)

    D = RectButton(win, Point(200, 0), Point(300, 100))
    D.Draw()
    D.Color("blue")
    D.Text("darken")

    L = RectButton(win, Point(500, 0), Point(600, 100))
    L.Draw()
    L.Color("blue")
    L.Text("lighten")

    G = RectButton(win, Point(350, 0), Point(450, 100))
    G.Draw()
    G.Color("gray")
    G.Text("grayscale")

    C = RectButton(win, Point(50, 0), Point(150, 100))
    C.Draw()
    C.Color("yellow")
    C.Text("contrast")
    
    RB = RectButton(win, Point(650, 0), Point(750, 100))
    RB.Draw()
    RB.Color("orange")
    RB.Text("red boost")

    B = RectButton(win, Point(25, 150), Point(125, 250))
    B.Draw()
    B.Color("brown")
    B.Text("blur")

    N = RectButton(win, Point(675, 525), Point(775, 625))
    N.Draw()
    N.Color("green")
    N.Text("reset")

    BB = RectButton(win, Point(0, 400), Point(100, 500))
    BB.Draw()
    BB.Color("cyan")
    BB.Text("blue boost")

    GB = RectButton(win, Point(0, 550), Point(100, 650))
    GB.Draw()
    GB.Color("green")
    GB.Text("green boost")

    E = RectButton(win, Point(0, 700), Point(100, 800))
    E.Draw()
    E.Color("purple")
    E.Text("edge thing")

    Q = RectButton(win, Point(675, 675), Point(775, 775))
    Q.Draw()
    Q.Color("red")
    Q.Text("quit")


    while True:
        p = win.getMouse()
        if Q.IsClicked(p):
            break
        elif N.IsClicked(p):
            I = Image(Point(400, 450), "ball.png")
            I.draw(win)
        elif D.IsClicked(p):
            darken(I, b)
        elif L.IsClicked(p):
            lighten(I, b)
        elif G.IsClicked(p):
            grayScale(I, b)
        elif C.IsClicked(p):
            superContrast(I, b)
        elif RB.IsClicked(p):
            redBoost(I, b)
        elif BB.IsClicked(p):
            blueBoost(I, b)
        elif GB.IsClicked(p):
            greenBoost(I, b)
        elif B.IsClicked(p):
            blur(I, b)
        elif E.IsClicked(p):
            edge(I, b)


    win.close()

if __name__ == "__main__":
    main()
