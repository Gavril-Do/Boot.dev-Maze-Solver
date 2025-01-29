from tkinter import Tk, BOTH, Canvas
from line import Line, Point

class Cell():
	def __init__(self, win=None):
		self.coords = None
		self.visited = False
		self.has_left = True
		self.has_right = True
		self.has_top = True
		self.has_bottom = True
		self.north = None
		self.south = None
		self.east = None
		self.west = None
		self._x1 = None
		self._x2 = None
		self._y1 = None
		self._y2 = None
		self._win = win

	def draw(self, x1, y1, x2, y2):
		if self._win is None:
			return
		self._x1 = x1
		self._x2 = x2
		self._y1 = y1
		self._y2 = y2
		if self.has_left == True:
			line = Line(Point(x1, y1), Point(x1, y2))
			self._win.draw_line(line)
		if self.has_right == True:
			line = Line(Point(x2, y1), Point(x2, y2))
			self._win.draw_line(line)
		if self.has_top == True:
			line = Line(Point(x1, y1), Point(x2, y1))
			self._win.draw_line(line)
		if self.has_bottom == True:
			line = Line(Point(x1, y2), Point(x2, y2))
			self._win.draw_line(line)
		
		if self.has_left == False:
			line = Line(Point(x1, y1), Point(x1, y2))
			self._win.draw_line(line, "white")
		if self.has_right == False:
			line = Line(Point(x2, y1), Point(x2, y2))
			self._win.draw_line(line, "white")
		if self.has_top == False:
			line = Line(Point(x1, y1), Point(x2, y1))
			self._win.draw_line(line, "white")
		if self.has_bottom == False:
			line = Line(Point(x1, y2), Point(x2, y2))
			self._win.draw_line(line, "white")
			

	def draw_move(self, to_cell, undo=False):
		half_length = abs(self._x2 - self._x1) // 2
		x_center = half_length + self._x1
		y_center = half_length + self._y1

		half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
		x_center2 = half_length2 + to_cell._x1
		y_center2 = half_length2 + to_cell._y1

		fill_color = "red"
		if undo:
			fill_color = "gray"

		line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
		self._win.draw_line(line, fill_color)
