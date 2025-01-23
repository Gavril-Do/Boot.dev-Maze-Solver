from tkinter import Tk, BOTH, Canvas

class Window(Tk):
	def __init__(self, width=800, height=600):
		self.__root = Tk()
		self.title = "Title"
		self.canvas = Canvas(self.__root, width=width, height=height)
		self.canvas.pack(fill=BOTH, expand=True)
		self.running = False
		self.__root.protocol("WM_DELETE_WINDOW", self.close)

	def redraw(self):
		self.__root.update_idletasks()
		self.__root.update()
	
	def wait_for_close(self):
		self.running = True
		while self.running == True:
			self.redraw()
		
	def close(self):
		self.running = False

	def draw_line(self, line, fill_color="black"):
		line.draw(self.canvas, fill_color)