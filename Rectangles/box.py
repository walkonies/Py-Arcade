import pygame
import random
from config import *

class Box:
	bounce = 1.25
	def __init__(self, win, x, y, color):
		self.surface = win
		self.x = x
		self.y = y
		self.size = size
		self.setRect()
		self.velX = speed[0]
		self.velY = speed[1]
		self.color = color
		self.gravity = False
		self.selected = False
		self.floor = False

	def changeColor(self):
		rgb = 0
		color = list(self.color)
		color[rgb] += 2
		color[rgb] = color[rgb]%256
		self.color = color

	def lightenColor(self):
		color = list(self.color)
		for i in range(len(color)):
			color[i] += 2
			color[i] = color[i]%256
		self.color = color

	def setRandomColor(self):
		max = 256
		random.seed()
		self.color = ([random.randrange(max) for i in range(3)])

	def setRect(self):
		self.rect = pygame.Rect((self.x,self.y),(self.size, self.size))

	def setGravity(self):
		if self.gravity:
			self.velY = 0
		self.gravity = not self.gravity

	def applyGravity(self):
		self.velY += G/FPS

	def select(self):
		self.selected = True

	def unselect(self):
		self.selected = False

	def getInput(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.x -= 1 * move_speed
		if keys[pygame.K_RIGHT]:
			self.x += 1 * move_speed

	def checkCollisionX(self):
		if self.x < 0:
			self.velX *= -self.bounce
			self.x = 0
			self.setRandomColor()
		elif self.x+size > s_width:
			self.velX *= -self.bounce
			self.x = s_width - self.size
			self.setRandomColor()

		if self.velX > max_vel_x:
			self.velX = max_vel_x
		elif self.velX < -max_vel_x:
			self.velX = -max_vel_x

	def checkCollisionY(self):
		if self.y + size > s_height and self.floor:
			self.velY = 0
			self.y = s_height-self.size


	def update(self):
		self.lightenColor()
		#self.changeColor()

		if not self.selected:
			self.x += self.velX
			self.checkCollisionX()
		else:
			self.getInput()


		if self.gravity:
			self.applyGravity()

		self.y += self.velY
		self.checkCollisionY()

		self.setRect()

	def draw(self):
		pygame.draw.rect(self.surface, self.color, self.rect)

		if self.selected:
			pygame.draw.rect(self.surface, red, self.rect, 2)