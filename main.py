from tkinter import Tk, BOTH, Canvas
from window import Window
from line import Line, Point
from cell import Cell

def main():
	win = Window(800, 600)
	
	c = Cell(win)
	c.has_left = False
	c.draw(50, 50, 100, 100)

	c = Cell(win)
	c.has_right = False
	c.draw(125, 125, 200, 200)

	c = Cell(win)
	c.has_top = False
	c.draw(225, 225, 250, 250)

	c = Cell(win)
	c.has_bottom = False
	c.draw(300, 300, 500, 500)

	win.wait_for_close()



if __name__ == "__main__":
	main()