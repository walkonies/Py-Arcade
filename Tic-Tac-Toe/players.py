import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import pygame as pg
from utilities.colors import colors as COLORS
pg.init()
class Token:
	FONT = pg.font.SysFont('comicsans', 40)
	COLOR = COLORS['grey']
	def __init__(self, win):
		self.win = win
		self.symbol = ''
		self.pos = (0,0)
	def draw(self):
		text = self.FONT.render(self.symbol, 1, self.COLOR)
		w,h = text.get_width(), text.get_height()
		x,y = self.pos
		x -= w//2
		y -= h//2
		self.win.blit(text, (x,y))
class X(Token):
	def __init__(self, win):
		super(X, self).__init__(win)
		self.symbol = 'X'
class O(Token):
	def __init__(self, win):
		super(O,self).__init__(win)
		self.symbol = 'O'

class Player:
	def __init__(self, num):
		self.player_num = num
		self.isTurn = False