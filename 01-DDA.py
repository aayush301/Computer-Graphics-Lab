# DDA Algorithm

from graphics import *

def round(x):
	return int(x+0.5)

def putPixel(win, x, y):
	pt = Point(x,y)
	pt.draw(win)

def DDA(x1,y1,x2,y2):
	
	win = GraphWin("DDA Algorithm", 500, 500)

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
	
	win.getMouse()
	
	
def main():
	print("Enter starting point")
	x1 = int(input("Enter startX: "))
	y1 = int(input("Enter startY: "))

	print("\nEnter ending point")
	x2 = int(input("Enter endX: "))
	y2 = int(input("Enter endY: "))
	
	DDA(x1,y1,x2,y2)

main()
