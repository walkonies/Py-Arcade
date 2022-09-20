import tkinter as tk


class pathButton:
	color = 'black'
	bg = 'white'
	ipad = 10    # for both x, y
	fill = 'both'
	def __init__(self, pathDirection, side):
		self.side = side
		self.text = pathDirection

	def click(self):
		pass



class startScreen:
	color = 'black'
	bg = 'red'
	ipad = 10
	fill = 'both'

	def __init__(self, root, text):
		self.labl = tk.Label(root, text=text, fg=self.color, bg=self.bg)
		self.labl.pack(ipadx=self.ipad, ipady=self.ipad, expand=True, fill=self.fill)
		