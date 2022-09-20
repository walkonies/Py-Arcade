import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from utilities.colors import colors as COLORS
import pygame as pg
from utilities.pg_driver import GameDriver
from players import X, O
from square import Square
from board import Board
pg.init()

class tictactoe:
	FONT = pg.font.SysFont('comicsans', 40)
	WIDTH = 400
	HEIGHT = 500
	def __init__(self, flags):
		self.win = pg.display.set_mode((self.WIDTH,self.HEIGHT), flags)
		pg.display.set_caption("Tic-Tac-Toe  -AW®")
		self.driver = GameDriver(self.win,30)
		self.board = Board(self.win)
		self.driver.add(self)
		self.players = []
		self.turn = 0
		self.playing = False
		self.text = None

	def handleKey(self, k):
		if k == 'c':
			self.reset()
		else:
			return

	def run(self):
		self.playing = True
		self.start()
		self.driver.run()

	def start(self):
		self.playing = True
		self.setText('Player 1 ready...', COLORS['red'])

	def addPlayer(self, player):
		if len(self.players < 2):
			self.players.append(player)

	def click(self, pos):
		sq = self.board.getSquare(pos)
		if not sq or not self.playing:
			return
		if sq.isTaken():
			return
		if self.text and self.playing:
			self.clearText()
		if self.turn == 0:
			self.board.click(sq, X(self.win))
		else:
			self.board.click(sq, O(self.win))
		if self.board.isFull():
			self.winner(None)
		elif self.evaluate():
			self.winner(self.turn+1)
		else:
			self.nextTurn()
		self.board.show()
		
	def nextTurn(self):
		self.turn += 1
		self.turn %= 2
		print(self.turn)
		self.setText(f'Player {self.turn+1} turn', COLORS['blue'] if self.turn else COLORS['red'])
	def inRange(self):
		return self.board.inRange()
	def draw(self):
		self.board.draw()
		if self.text:
			self.display(self.text)
	def setText(self, message, color):
		text = self.FONT.render(message,1,color)
		self.text= text
	def clearText(self):
		self.text = None
	def evaluate(self):
		board = self.board.getSquares()
		rows = [[i+(j*3) for i in range(3)] for j in range(3)]
		cols= [[i+j for i in range(0,7,3)] for j in range(3)]
		diag = [[0,4,8], [2,4,6]]
		check = [rows, cols, diag]
		for c in check:
			for section in c:
				if not board[section[0]].isTaken():
					continue
				elif board[section[0]].getToken() == board[section[1]].getToken() == board[section[2]].getToken():
					return True
		return False
	def winner(self, player):
		color  = COLORS['white']
		if player:
			text = f'Player {player} wins!!'
			color = COLORS['green']
		else:
			text = 'Draw!'
		self.setText(text, color)
		self.playing = False
	def display(self, text):
		w,h = text.get_width(), text.get_height()
		padding = 30
		x = self.WIDTH//2 - w//2
		y = self.HEIGHT - padding - h
		self.win.blit(text, (x,y))
	def reset(self):
		self.board.setup()
		self.turn = 0
		self.playing = False
		self.clearText()
		self.start()


def main():
	flags = pg.RESIZABLE if 0 else 0
	game = tictactoe(flags)
	game.run()

	
	
if __name__ == '__main__':
	main()