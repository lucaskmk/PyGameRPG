import pygame
from pygame.sprite import _Group
from Settings import *

# pos = posicao
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('prites\Rock Pile.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)