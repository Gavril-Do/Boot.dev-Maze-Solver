from tkinter import Tk, BOTH, Canvas

class Window(Tk):
	def __init__(self, width=800, height=600):
		self.__root = Tk()
		self.__root.title("Maze Solver")
		self.__root.protocol("WM_DELETE_WINDOW", self.close)
		self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
		self.__canvas.pack(fill=BOTH, expand=1)
		self.__running = False

	def redraw(self):
		self.__root.update_idletasks()
		self.__root.update()
	
	def wait_for_close(self):
		self.__running = True
		while self.__running == True:
			self.redraw()
		print("window closed...")
		
	def close(self):
		self.__running = False

	def draw_line(self, line, fill_color="black"):
		line.draw(self.__canvas, fill_color)