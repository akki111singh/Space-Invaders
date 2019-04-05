import pygame
from random import randint
from pygame import time
from pygame.sprite import Sprite
from pygame.locals import *
img1 = pygame.image.load('images/alien.bmp')
img2 = pygame.image.load('images/alien.bmp')


class Alien(Sprite):
    def __init__(self, set_screen, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.set_screen = set_screen

        self.image = pygame.image.load('images/alien1.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 8)*self.rect.width
        self.rect.y = randint(0, 1)*self.rect.height

    def blitme(self):
        self.screen.blit(self.image, self.rect)
