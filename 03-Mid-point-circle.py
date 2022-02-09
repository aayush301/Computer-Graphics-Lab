# Mid point Circle drawing Algorithm

from graphics import *


def putPixel(win, x, y):
    pt = Point(x,y)
    pt.draw(win)


def midpointCircle(cx,cy,r):
	
	win = GraphWin("Mid point circle drawing algorithm", 500, 500)


	x=0
	y=r
	P= 1-r

	while x<=y:
		# print(x,y)
		putPixel(win,x+cx,y+cy)
		putPixel(win,y+cx,x+cy)
		putPixel(win,-x+cx,y+cy)
		putPixel(win,-y+cx,x+cy)
		putPixel(win,-x+cx,-y+cy)
		putPixel(win,-y+cx,-x+cy)
		putPixel(win,x+cx,-y+cy)
		putPixel(win,y+cx,-x+cy)
		
		if P<0:
			x = x+1
			P = P+2*x+1
		else:
			x = x+1
			y = y-1
			P = P+2*(x-y)+1
	
	win.getMouse()
	
	
def main():
	print("Enter centre of circle")
	cx = int(input("Enter x: "))
	cy = int(input("Enter y: "))

	r = int(input("Enter radius of circle: "))
	
	midpointCircle(cx,cy,r)

main()
