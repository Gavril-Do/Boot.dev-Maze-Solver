from tkinter import Tk, BOTH, Canvas
from cell import Cell
import random
import time

class Maze:
	def __init__(
			self,
			x1,
			y1,
			num_rows,
			num_cols,
			cell_size_x,
			cell_size_y,
			win=None,
			seed=None
	):
		self._cells = []
		self._x1 = x1
		self._y1 = y1
		self._num_rows = num_rows
		self._num_cols = num_cols
		self._cell_size_x = cell_size_x
		self._cell_size_y = cell_size_y
		self._win = win
		if seed:
			random.seed(seed)

		self._create_cells()
		self._break_entrance_and_exit()
		self._break_walls_r(0, 0)
		self._reset_cells_visited()

	def _create_cells(self):
		for i in range(self._num_cols):
			col_cells = []
			for j in range(self._num_rows):
				col_cells.append(Cell(self._win))
			self._cells.append(col_cells)
		for i in range(self._num_cols):
			for j in range(self._num_rows):
				self._cells[i][j].coords = [i, j]
				if i > 0:
					self._cells[i][j].west = self._cells[i - 1][j]
				if i < self._num_cols - 1:
					self._cells[i][j].east = self._cells[i + 1][j]
				if j > 0:
					self._cells[i][j].north = self._cells[i][j - 1]
				if j < self._num_rows - 1:
					self._cells[i][j].south = self._cells[i][j + 1]
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
		if self._win is None:
			return
		self._win.redraw()
		time.sleep(0.05)

	def _break_entrance_and_exit(self):
		self._cells[0][0].has_top = False
		self._draw_cell(0, 0)
		self._cells[-1][-1].has_bottom = False
		self._draw_cell((self._num_cols-1), (self._num_rows-1))

	def _break_walls_r(self, i, j):
		# mark current cell as visited
		cell = self._cells[i][j]
		cell.visited = True
		# loop:
		while True:
			next_index_list = []

			# determine which cell(s) to visit next
			# left
			if i > 0  and not self._cells[i - 1][j].visited:
				next_index_list.append((i - 1, j))
			# right
			if i < self._num_cols -1 and not self._cells[i + 1][j].visited:
				next_index_list.append((i + 1, j))
			# up
			if j > 0 and not self._cells[i][j - 1].visited:
				next_index_list.append((i, j - 1))
			# down
			if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
				next_index_list.append((i, j + 1))
			# if there is nowhere to go from here
			# just break out
			if len(next_index_list) == 0:
				self._draw_cell(i, j)
				return
			
			# randomly choose the next direction to go
			direction_index = random.randrange(len(next_index_list))
			next_index = next_index_list[direction_index]

			# knock out walls between cells
			# right
			if next_index[0] == i + 1:
				self._cells[i][j].has_right = False
				self._cells[i + 1][j].has_left = False
			# left
			if next_index[0] == i - 1:
				self._cells[i][j].has_left = False
				self._cells[i - 1][j].has_right = False
			# down
			if next_index[1] == j + 1:
				self._cells[i][j].has_bottom = False
				self._cells[i][j + 1].has_top = False
			# up
			if next_index[1] == j - 1:
				self._cells[i][j].has_top = False
				self._cells[i][j - 1].has_bottom = False
			
			# recursively visit the next cell
			self._break_walls_r(next_index[0], next_index[1])

	def _reset_cells_visited(self):
		for list in self._cells:
			for cell in list:
				cell.visited = False

	def solve(self):
		return self._solve_r(0, 0)
	
	def _solve_r(self, i, j):
		self._animate()

		# vist the current cell
		# self._cells[i][j].visited = True

		cell = self._cells[i][j]
		cell.visited = True
			# if we are at the end cell, we are done!
		# if i == self._num_cols - 1 and j == self._num_rows - 1:
		# 	return True
		if cell == self._cells[-1][-1]:
			return True

		# move left if there is no wall and it hasn't been visited
		if (
			i > 0
			and not cell.has_left
			and not cell.west.visited
		):
			cell.draw_move(cell.west)
			if self._solve_r(i - 1, j):
				return True
			else:
				cell.draw_move(cell.west, True)

		# move right if there is no wall and it hasn't been visited
		if (
			i < self._num_cols - 1
			and not cell.has_right
			and not cell.east.visited
		):
			cell.draw_move(cell.east)
			if self._solve_r(i + 1, j):
				return True
			else:
				cell.draw_move(cell.east, True)

		# move up if there is no wall and it hasn't been visited
		if (
			j > 0
			and not cell.has_top
			and not cell.north.visited
		):
			cell.draw_move(cell.north)
			if self._solve_r(i, j - 1):
				return True
			else:
				cell.draw_move(cell.north, True)

		# move down if there is no wall and it hasn't been visited
		if (
			j < self._num_rows - 1
			and not cell.has_bottom
			and not cell.south.visited
		):
			cell.draw_move(cell.south)
			if self._solve_r(i, j + 1):
				return True
			else:
				cell.draw_move(cell.south, True)

		# we went the wrong way let the previous cell know by returning False
		return False

	
	# def _solve_r(self, i, j):
	# 	self._animate()
	# 	cell = self._cells[i][j]
	# 	cell.visited = True
	# 	if cell == self._cells[-1][-1]:
	# 		return True
		
	# 	direction = []
	# 	if cell.north != None:
	# 		direction.append(cell.north)
	# 	if cell.south != None:
	# 		direction.append(cell.south)
	# 	if cell.west != None:
	# 		direction.append(cell.west)
	# 	if cell.east != None:
	# 		direction.append(cell.east)
		
	# 	while len(direction) > 0:
	# 		d = direction.pop(random.randrange(len(direction)))
	# 		if cell.has_top == False:
	# 			if d == cell.north and cell.north.visited == False:
	# 				cell.draw_move(cell.north)
	# 				solve = self._solve_r(i, j - 1)
	# 				if solve:
	# 					return True
	# 				else:
	# 					cell.draw_move(cell.north, True)
	# 		if cell.has_bottom == False:
	# 			if d == cell.south and cell.south.visited == False:
	# 				cell.draw_move(cell.south)
	# 				if self._solve_r(i, j + 1):
	# 					return True
	# 				else:
	# 					cell.draw_move(cell.south, True)
	# 		if cell.has_left == False:
	# 			if d == cell.west and cell.west.visited == False:
	# 				cell.draw_move(cell.west)
	# 				if self._solve_r(i - 1, j):
	# 					return True
	# 				else:
	# 					cell.draw_move(cell.west, True)
	# 		if cell.has_right == False:
	# 			if d == cell.east and cell.east.visited == False:
	# 				cell.draw_move(cell.east)
	# 				if self._solve_r(i + 1, j):
	# 					return True
	# 				else:
	# 					cell.draw_move(cell.east, True)
	# 	return False

