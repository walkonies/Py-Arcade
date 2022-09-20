import os,sys
directory = os.path.join(os.getcwd(),os.path.dirname(__file__))
sys.path.append(directory)
from config import *
import pygame
from box import Box
pygame.init()
window = pygame.display.set_mode(s_size)
clock = pygame.time.Clock()

bg = pygame.image.load(os.path.join(directory, 'bg.jpg' ))
bg = pygame.transform.scale(bg, (300,300))

def main(mode):
	run = True
	selected = -1

	if mode == 0:
		boxes = [Box(window, 0, s_height/2, white)]
	if mode == 1:
		boxes = [Box(window, 0, size*i, white) for i in range(n_boxes)]
	if mode == 2:
		boxes = [Box(window,i*size,size*i, white) for i in range(n_boxes)]

	while run:
		clock.tick(FPS)
		rem = []
		num_boxes = len(boxes)

		window.blit(bg, (0,0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				break
			if event.type == pygame.KEYDOWN:
				key = event.key
				if key == pygame.K_r:				#Restart
					main(0)
					run = False
					break
				if key == pygame.K_UP:				#Select up
					boxes[selected].unselect()
					selected -= 1
					selected %= num_boxes
					boxes[selected].select()
				if key == pygame.K_DOWN:			#Select down
					boxes[selected].unselect()
					selected += 1
					selected %= num_boxes
					boxes[selected].select()
				if key == pygame.K_f:				#Box fall
					boxes[selected].setGravity()
				if key == pygame.K_BACKSPACE:		#Box deselect
					boxes[selected].unselect()
					selected = -1
				if key == pygame.K_c:				#Toggle floor
					for box in boxes:
						box.floor = not box.floor
				if key == pygame.K_SPACE:			#All fall
					for box in boxes:
						box.gravity = True

		for box in boxes:
			box.update()
			if box.y < s_height:
				box.draw()
			else:
				rem.append(box)

		for box in rem:
			if box.selected:
				box.unselect()
				selected = -1
			boxes.remove(box)

		if len(boxes) == 0:
			run = False

		pygame.display.update()
		window.fill(black)


if __name__ == '__main__':
	main(2)
	pygame.quit()


