import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import pygame as pg
from square import Square
from utilities.colors import colors as COLORS

class Board:
	padding = 10
	def __init__(self, win):
		self.win = win
		self.sq_size = self.getSqSize(3)
		self.squares = []
		self.rect = None
		self.setup()
	def getSqSize(self, num):
		sq_size = (self.win.get_size()[0]-self.padding*2)//num
		return (sq_size, sq_size)
	def setup(self):
		# make grid
		x = [self.padding + i*self.sq_size[0] for i in range(0,3)]
		y = [self.padding + i*self.sq_size[1] for i in range(0,3)]
		self.squares = []
		for yval in y:
			for xval in x:
				self.squares.append(Square(self.win, (xval,yval), COLORS['white'], self.sq_size))
		self.rect = pg.Rect((x[0],y[0]), (self.sq_size[0] * len(x), self.sq_size[1] * len(y)))
	def getSquares(self):
		return self.squares
	def click(self, target, token):
		for sq in self.getSquares():
			if sq == target:
				sq.click(token)
	def inRange(self, pos):
		return self.rect.collidepoint(pos)
	def draw(self):
		for sq in self.getSquares():
			sq.draw()
	def isFull(self):
		for sq in self.getSquares():
			if not sq.token:
				return False
		return True
	def getSquare(self,pos):
		for sq in self.getSquares():
			if sq.inRange(pos):
				return sq
		return None
	def show(self):
		for i, sq in enumerate(self.getSquares()):
			print(sq, end=' ')
			if not (i+1)%3:
				print()
		print()