import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import pygame as pg
from utilities.colors import colors as COLORS
class Square:
	BORDER = COLORS['grey']
	def __init__(self, win, pos, color, size):
		self.win = win
		self.pos = pos					# topleft x,y
		self.color = color
		self.size = size        # width, height
		self.rect = self.getRect()
		self.token = None
	def getRect(self):
		rect = pg.Rect(self.pos,self.size)
		return rect
	def getToken(self):
		if self.token:
			return self.token.symbol
		return None
	def getBoundary(self):
		x1 = self.rect.left
		x2 = self.rect.right
		y1 = self.rect.top
		y2 = self.rect.bottom
		return(x1,x2,y1,y2)
	def draw(self):
		pg.draw.rect(self.win, self.color, self.rect)
		pg.draw.rect(self.win, self.BORDER, self.rect,3)
		if self.token:
			self.token.draw()
	def click(self, token):
		if not self.token:
			self.token = token
			x,y = self.pos
			x += self.size[0] // 2
			y += self.size[1] // 2
			token.pos = (x,y)
	def update(self, vel):
		vX,vY = vel
		self.rect = self.rect.move(vX,vY)
		self.pos = self.rect.topleft
	def inRange(self, pos):
		return self.rect.collidepoint(pos)
	def isTaken(self):
		return True if self.token else False
	def __str__(self):
		return self.token.symbol if self.isTaken() else '-'