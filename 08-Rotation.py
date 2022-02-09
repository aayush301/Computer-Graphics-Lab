# Rotation

from graphics import*
import numpy as np


def rotate(pointsA, t, xp, yp):
	
	t = t*np.pi/180
	
	pointsB = []
	for x,y in pointsA:
		xf = int((x-xp)*np.cos(t)-(y-yp)*np.sin(t)) + xp
		yf = int((x-xp)*np.sin(t)+(y-yp)*np.cos(t)) + yp
		pointsB.append((xf,yf))
	
	return pointsB


def plot(pointsA, pointsB, isClosed):
	
	win = GraphWin("Rotation", 500, 500)
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
	
	pointsA = [(50,50), (100,100), (150,100), (100,50)]
	isClosed = True
	t = 60
	xp = 50
	yp = 50
	
	pointsB = rotate(pointsA, t, xp, yp)
	print(pointsB)
	plot(pointsA, pointsB, isClosed)


main()
