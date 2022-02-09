# Mid point Ellipse drawing Algorithm

from graphics import *


def putPixel(win, x, y):
    pt = Point(x,y)
    pt.draw(win)


def midpointEllipse(cx,cy,a,b):
	
	win = GraphWin("Mid point ellipse drawing algorithm", 500, 500)


	x=0
	y=b
	P1= b**2+ (a**2)/4 - a*a*b

	while 2*b*b*x<=2*a*a*y:
		# print(x,y)
		putPixel(win,x+cx,y+cy)
		putPixel(win,-x+cx,y+cy)
		putPixel(win,-x+cx,-y+cy)
		putPixel(win,x+cx,-y+cy)
		
		if P1<0:
			x = x+1
			P1 = P1+b*b*(2*x+1)
		else:
			x = x+1
			y = y-1
			P1 = P1+b*b*(2*x+1)-2*a*a*y
	
	P2= b*b*(x+1/2)**2 + a*a*(y-1)**2 - a*a*b*b

	while y>=0:
		# print(x,y)
		putPixel(win,x+cx,y+cy)
		putPixel(win,-x+cx,y+cy)
		putPixel(win,-x+cx,-y+cy)
		putPixel(win,x+cx,-y+cy)
		
		if P2>=0:
			y = y-1
			P2 = P2+a*a*(1-2*y)
		else:
			x = x+1
			y = y-1
			P2 = P2+a*a*(1-2*y)+2*b*b*x
	
	win.getMouse()
	
	
def main():
	print("Enter centre of ellipse")
	cx = int(input("Enter x: "))
	cy = int(input("Enter y: "))
	
	print("\n")
	a = int(input("Enter radius along x-axis: "))
	b = int(input("Enter radius along y-axis: "))
	
	midpointEllipse(cx,cy,a,b)

main()
