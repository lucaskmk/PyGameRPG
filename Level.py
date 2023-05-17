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
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TITLESIZE
                y = row_index * TITLESIZE
    def run_game(self):
        pass
    