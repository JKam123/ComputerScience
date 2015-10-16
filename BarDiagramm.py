from graphics import *
import random

Win = GraphWin()
Win.setCoords(0,0,20,20)

for i in range(10):
    Num = random.uniform(0,10)
    X = Point((i)*2+0.2,5)
    Y = Point(X.getX()+2, 5+Num)
    Col = color_rgb(random.uniform(20,255),random.uniform(20,255),random.uniform(20,255))
    Rect = Rectangle(X,Y)
    Rect.setFill(Col)
    Rect.draw(Win)
    #TPoint = Point(X.getX()+1,X.getY()+2)
    #T = Text(TPoint, Num)
    #T.draw(Win)
    print Num
