import sys
import pygame
right = [0]
left = [0]
control = [0]


class Ship():

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            control[0] += 1
            if right[0] % 20 >= 15 and right[0] % 20 < 30:
                self.rect.centerx += 1
            right[0] = (right[0]+1) % 20
            if self.rect.centerx >= 580:
                self.rect.centerx = 580

        if self.moving_left:
            if left[0] % 20 >= 15 and left[0] % 20 < 30:
                self.rect.centerx -= 1
            left[0] = (left[0]+1) % 20
            if self.rect.centerx <= 20:
                self.rect.centerx = 20

    def blitme(self):
        self.screen.blit(self.image, self.rect)
