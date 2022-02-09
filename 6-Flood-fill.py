# Flood fill Algorithm
from graphics import *

import sys
sys.setrecursionlimit(1000000)

win = GraphWin("Flood fill Algorithm", 500, 500)

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


def drawSomeFigure():
    p = Polygon(Point(a,b), Point(c,b), Point(c,d), Point(a,d))
    p.draw(win)


def floodFill(x, y, fillColor, interiorColor):
    
    if x<=a or x>=c or y<=b or y>=d or color[x][y]==fillColor:
        return

    putPixel(win,x,y,fillColor)
    color[x][y] = fillColor
    
    for i in range(4):
        floodFill(x+dx[i], y+dy[i], fillColor, interiorColor)


def main():
    
    fillColor = "yellow"
    interiorColor = "white"
    drawSomeFigure()
    
    interior_x = 250
    interior_y = 250
    
    floodFill(interior_x, interior_y, fillColor, interiorColor)
    win.getMouse()

main()