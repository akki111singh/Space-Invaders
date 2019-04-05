import pygame
from time import sleep
from pygame.sprite import Sprite
update = [0]


class Bullet(Sprite):

    def __init__(self, set_screen, screen, ship):

        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, set_screen.bullet_width,
                                set_screen.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = self.rect.y
        self.x = self.rect.x

        self.color = set_screen.bullet_color
        self.speed_factor = set_screen.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Bullet2(Bullet):
    def __init__(self, set_screen, screen, ship):
        Bullet.__init__(self, set_screen, screen, ship)
        self.speed_factor = set_screen.bullet2_speed_factor
        self.color = set_screen.bullet2_color
        self.rect = pygame.Rect(0, 0, set_screen.bullet2_width,
                                set_screen.bullet2_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = self.rect.y
        self.x = self.rect.x
