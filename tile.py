import pygame
from settings import *

# pos = posicao
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = self.image = pygame.image.load('sprites\RockPile.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)