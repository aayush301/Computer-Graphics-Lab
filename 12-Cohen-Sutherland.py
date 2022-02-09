# Cohen-Sutherland Line Clipping Algorithm

from graphics import*
import numpy as np

win1 = GraphWin("Cohen-Sutherland Algorithm: Initial lines", 500, 500)
win2 = GraphWin("Cohen-Sutherland Algorithm: Clipped lines", 500, 500)



def	findRegionCode(xmin, xmax, ymin, ymax, x, y):
	code=0
	b1 = ((x-xmin)>>27)&1
	b2 = ((xmax-x)>>27)&1
	b3 = ((y-ymin)>>27)&1
	b4 = ((ymax-y)>>27)&1
	code = code | b1 | (b2<<1) | (b3<<2) | (b4<<3)
	return code
	


def cohen(xmin, xmax, ymin, ymax, x0, y0, x1, y1):
	
	while(True):
		
		code1 = findRegionCode(xmin, xmax, ymin, ymax, x0, y0)
		code2 = findRegionCode(xmin, xmax, ymin, ymax, x1, y1)
		

		if((code1 | code2)==0):
			return (True,x0,y0,x1,y1)
		elif((code1 & code2)!=0):
			return (False,-1,-1,-1,-1)
		else:
			if(code1==0):
				(x0,x1)=(x1,x0)
				(y0,y1)=(y1,y0)
				(code1,code2) = (code2,code1)
			
			m=0
			if(x0 != x1):
				m = (y1-y0)/(x1-x0)
			
			if(code1 & 1):
				y0 = y0 + m*(xmin-x0)
				x0 = xmin
			elif(code1 & 2):
				y0 = y0 + m*(xmax-x0)
				x0 = xmax
			elif(code1 & 4):
				if(x0!=x1):
					x0 = x0 + (ymin-y0)/m
				y0 = ymin
			elif(code1 & 8):
				if(x0!=x1):
					x0 = x0 + (ymax-y0)/m
				y0 = ymax
			
		x0 = round(x0); y0=round(y0)
		x1 = round(x1); y1=round(y1)
		


def main():
	
	xmin=150; xmax=350; ymin=150; ymax=350
	lines = [(100,250,200,250), (250,100,400,250), (50,175,200,80), (230,400,230,120), (320,250,250,330)]
	colors = ["green", "red", "gray", "purple", "orange"]
	
	
	r1=Polygon(Point(xmin,ymin), Point(xmin,ymax), Point(xmax,ymax), Point(xmax,ymin))
	r1.setOutline("blue")
	r1.setWidth(5)
	r1.draw(win1)
	
	r2=r1.clone()
	r2.draw(win2)


	for line,color in zip(lines,colors):
		(x0,y0,x1,y1) = line
		l1 = Line(Point(x0,y0), Point(x1,y1))
		l1.setOutline(color)
		l1.setWidth(5)
		l1.draw(win1)
		
		(exist,x0f,y0f,x1f,y1f) = cohen(xmin, xmax, ymin, ymax, x0, y0, x1, y1)
		if(exist):
			l2 = Line(Point(x0f,y0f), Point(x1f,y1f))
			l2.setOutline(color)
			l2.setWidth(5)
			l2.draw(win2)
		
	win1.getMouse()
	win2.getMouse()


main()
