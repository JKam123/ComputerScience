from graphics import *
import random
import math

Frequency = []
MaxFrequency = 0
for i in range(10):
    Frequency.append(0)
    
Array = []
Sum = 0

for i in range(1000):
    Sum = 0
    for x in range(10):
        Num = random.uniform(0,1)
        Sum = Sum + Num
        if x == 9:
            Array.append(Sum)

for i in range(len(Array)):
    Num = int(Array[i])
    Frequency[Num] = Frequency[Num] + 1
   
print Frequency
for i in range(len(Frequency)):
    if Frequency[i] > MaxFrequency:
        MaxFrequency = Frequency[i]

Win = GraphWin()
Win.setCoords(0,0,20,MaxFrequency+40)

for i in range(len(Frequency)):
    X = Point((i)*2+0.2,5)
    Y = Point(X.getX()+2, 5+Frequency[i])
    Col = color_rgb(random.uniform(20,255),random.uniform(20,255),random.uniform(20,255))
    Rect = Rectangle(X,Y)
    Rect.setFill(Col)
    Rect.draw(Win)
    T = Text(Point(X.getX()+1,X.getY()+Frequency[i]+10), str(Frequency[i]))
    T.draw(Win)
    T.setSize(8)
    
Win.getMouse()
Win.close()
