from tkinter import Tk, BOTH, Canvas
from window import Window
from line import Line, Point

def main():
	win = Window(400, 300)
	p1 = Point(10, 10)
	p2 = Point(200, 200)
	l1 = Line(p1, p2)
	win.draw_line(l1)
	p3 = Point(200, 10)
	p4 = Point(10, 200)
	l2 = Line(p3, p4)
	win.draw_line(l2, "red")
	win.wait_for_close()



if __name__ == "__main__":
	main()