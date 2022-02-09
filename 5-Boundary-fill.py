# Boundary fill Algorithm
from graphics import *

import sys
sys.setrecursionlimit(1000000)

win = GraphWin("Boundary fill Algorithm", 500, 500)

dx=[0,1,0,-1,-1,1,1,-1]
dy=[-1,0,1,0,-1,-1,1,1]

a = 230
b = a
c = 280
d = c

color = [["white" for j in range(d+1)] for i in range(c+1)]

def putPixel(win, x, y, fillColor):
    pt = Point(x,y)
    pt.setFill(fillColor)
    pt.draw(win)


def drawSomeFigure(borderColor):
    p=Polygon(Point(a,b), Point(c,b), Point(c,d), Point(a,d))
    p.setOutline(borderColor)
    p.draw(win)


def boundaryFill(x, y, fillColor, borderColor):
    
    if x<=a or x>=c or y<=b or y>=d or color[x][y]==fillColor:
        return
    
    putPixel(win,x,y,fillColor)
    color[x][y] = fillColor
    
    for i in range(4):
        boundaryFill(x+dx[i], y+dy[i], fillColor, borderColor)


def main():
    
    borderColor = "blue"
    fillColor = "yellow"
    drawSomeFigure(borderColor)
    
    interior_x = 250
    interior_y = 250
    
    boundaryFill(interior_x, interior_y, fillColor, borderColor)
    win.getMouse()

main()

