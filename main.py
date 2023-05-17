import pygame, sys
from settings import *
from level import *

class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption('RPixelsG')
		self.clock = pygame.time.Clock()
		self.level = Level()
	# ============================================ EVENT LOOP ================
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
			pygame.display.update()
			self.clock.tick(FPS)
   # ============================================ EVENT LOOP ================

if __name__ == '__main__':
	game = Game()
	game.run()	