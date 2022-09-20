import os, sys
import pygame as pg
from utilities.keys import keys
from utilities.colors import colors as COLORS

class GameDriver:
	COLORS = COLORS
	KEYS = keys
	def __init__(self, win, fps):
		pg.init()
		self.window = win
		self.window_size = self.window.get_size()
		self.fps = fps
		self.clock = pg.time.Clock()
		self.setup()
	def quit(self):
		self.running = False
	def setup(self):
		self.assets = []
		self.running = False
	def add(self, asset):
		self.assets.append(asset)
	def draw(self):
			for ass in self.assets:
				ass.draw()
			pg.display.update()
			self.clearWindow(self.COLORS['black'])
	def clearWindow(self, color):
		self.window.fill(color)
	def run(self):
		self.running = True
		while self.running:
			self.clock.tick(self.fps)
			self.getEvents()
			self.draw()
	def getEvents(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.quit()
				break
			# mouse down
			if event.type == pg.MOUSEBUTTONDOWN:
				self.handleClick(event)
			# key down
			if event.type == pg.KEYDOWN:
				self.handleKey(event)
	def handleKey(self, key):
		keys = self.KEYS
		k_val = key.key
		m = key.mod  	# to capture shift or cmd
		k = None
		if k_val in self.KEYS:
			k = self.KEYS[k_val]
		else:
			print(f'UNREGISTERED [{k_val} - {key.unicode}]')
			return
		if m & pg.KMOD_SHIFT:
			k = k.upper()
		if m & pg.KMOD_LMETA: # Mac specific; LCMD
			k = 'CMD+' + k if k != 'LCMD' else 'CMD'
		for ass in self.assets:
			ass.handleKey(k)
		print(k)
	def handleClick(self, event):
		pos = event.pos
		for ass in self.assets:
			ass.click(pos)

def main():
	window = pg.display.set_mode((400,500))
	game = GameDriver(window,30)
	game.run()

if __name__ == '__main__':
	main()
	pg.quit()