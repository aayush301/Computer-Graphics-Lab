# Polygon drawing Algorithm

from graphics import *

win = GraphWin("Polygon drawing Algorithm", 500, 500)

def putPixel(win, x, y):
	pt = Point(x,y)
	pt.draw(win)


def drawLine(x1,y1,x2,y2):
	
	dx = abs(x2-x1)
	dy = abs(y2-y1)
	length = max(dx,dy)

	dx = (x2-x1)/length
	dy = (y2-y1)/length

	x=x1
	y=y1

	for i in range(length+1):
		# print(round(x),round(y))
		putPixel(win,round(x),round(y))
		x = x+dx
		y = y+dy


def main():
	points = [(250,125),(125,250), (175,275), (240,175)]

	points.append(points[0])
	
	for i in range(len(points)-1):
		(x1,y1) = points[i]
		(x2,y2) = points[i+1]
		drawLine(x1,y1,x2,y2)
	
	win.getMouse()


main()
