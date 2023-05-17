import pygame
from settings import *
class Level:
    def __init__(self):
        # superficie do display
        self.display_surface = pygame.display.get_surface()
        # gropos das sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        #sprite setup
        self.create_map()
    def create_map(self):
        for row in WORLD_MAP:
            print(row)
    def run_game(self):
        pass
    