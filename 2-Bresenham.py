# Bresenham's Algorithm

from graphics import *


def putPixel(win, x, y):
	pt = Point(x,y)
	pt.draw(win)


def Bresenham(x1,y1,x2,y2):
	
	win = GraphWin("Bresenham's Algorithm", 500, 500)

	dx = x2-x1
	dy = y2-y1
	
	x=x1
	y=y1
	P= 2*dy-dx

	while x<=x2:
		# print(x,y)
		putPixel(win,x,y)
		
		if P<0:
			P = P+2*dy
			x = x+1
		else:
			P = P+2*dy-2*dx
			x = x+1
			y = y+1
	
	win.getMouse()
	
	
def main():
	print("Enter starting point")
	x1 = int(input("Enter startX: "))
	y1 = int(input("Enter startY: "))

	print("\nEnter ending point")
	x2 = int(input("Enter endX: "))
	y2 = int(input("Enter endY: "))
	
	Bresenham(x1,y1,x2,y2)

main()
