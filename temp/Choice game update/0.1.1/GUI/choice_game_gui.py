import tkinter as tk
from path import Path
import widgets

title = 'Choice Game'
size = '1200x800'

class Gui:
	def __init__(self):
		# Set up window
		self.root = tk.Tk()
		self.root.title(title)
		self.root.geometry(size)

	def clear(self):
	# Clear all widgets
		for widget in self.root.pack_slaves():
			widget.destroy()

	def setPath(self, path):
		pass
	def start(self, intro):
		widgets.startScreen(self.root, intro)
	def gameOver(self):
		pass
