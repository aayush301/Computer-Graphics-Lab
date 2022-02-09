# Scaling

from graphics import*
import numpy as np

def scale(pointsA, sx, sy, xp, yp):
	
	pointsB = []
	for x,y in pointsA:
		xf = int((x-xp)*sx) + xp
		yf = int((y-yp)*sy) + yp
		pointsB.append((xf,yf))
	
	return pointsB



def plot(pointsA, pointsB, isClosed):
	
	win = GraphWin("scaling", 500, 500)
	win.setCoords(-250,-250,250,250)
	
	l = Line(Point(0,-250), Point(0,250))
	l.draw(win)
	l = Line(Point(-250,0), Point(250,0))
	l.draw(win)
	
	
	if isClosed:
		pointsA.append(pointsA[0])
		pointsB.append(pointsB[0])
	
	
	for i in range(len(pointsA)-1):
		(x1,y1) = pointsA[i]
		(x2,y2) = pointsA[i+1]
		
		l = Line(Point(x1,y1), Point(x2,y2))
		l.setOutline("green")
		l.setWidth(5)
		l.draw(win)
		
		
	for i in range(len(pointsB)-1):
		(x1,y1) = pointsB[i]
		(x2,y2) = pointsB[i+1]
		
		l = Line(Point(x1,y1), Point(x2,y2))
		l.setOutline("blue")
		l.setWidth(3)
		l.draw(win)
	
	win.getMouse()


def main():
	
	pointsA = [(50,50), (100,50), (100,100), (50,100)]
	isClosed = True
	sx = 2.0
	sy = 2.0
	xp = 75
	yp = 75

	pointsB = scale(pointsA, sx, sy, xp, yp)
	print(pointsB)
	plot(pointsA, pointsB, isClosed)

main()
