from tkinter import Tk, BOTH, Canvas
from cell import Cell
import random
import time

class Maze():
	def __init__(
			self,
			x1,
			y1,
			num_rows,
			num_cols,
			cell_size_x,
			cell_size_y,
			win,
	):
		self._cells = []
		self._x1 = x1
		self._y1 = y1
		self._num_rows = num_rows
		self._num_cols = num_cols
		self._cell_size_x = cell_size_x
		self._cell_size_y = cell_size_y
		self._win = win

		self._create_cells()

	def _create_cells(self):
		for i in range(self._num_cols):
			col_cells = []
			for j in range(self._num_rows):
				col_cells.append(Cell(self._win))
			self._cells.append(col_cells)
		for i in range(self._num_cols):
			for j in range(self._num_rows):
				self._draw_cell(i, j)
	
	def _draw_cell(self, i , j):
		if self._win is None:
			return
		x1 = self._x1 + i * self._cell_size_x
		y1 = self._y1 + j * self._cell_size_y
		x2 = x1 + self._cell_size_x
		y2 = y1 + self._cell_size_y
		self._cells[i][j].draw(x1, y1, x2, y2)
		self._animate()

	def _animate(self):
		self._win.redraw()
		time.sleep(0.05)

		# current_y1 = self._y1
		# # fill list of lists
		# for col in range(self._num_cols):
		# 	self._cells.append([])
		# 	current_x1 = self._x1
		# 	current_y1 = self._y1 + self._cell_size_y
		# 	for row in range(self._num_rows):
		# 		new_cell = Cell(self._win)
		# 		new_cell._x1 = current_x1
		# 		new_cell._y1 = current_y1
		# 		current_x1 = self._x1 + self._cell_size_x
		# 		new_cell._x2 = current_x1
		# 		new_cell._y2 = current_y1 + self._cell_size_y
		# 		self._cells[col].append(new_cell)
		# for column in self._cells:
		# 	for cell in column:
		# 		self._draw_cell(cell)