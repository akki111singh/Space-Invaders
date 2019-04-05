import pygame
from time import sleep


class setting():
    # game settings
    def __init__(self):
        self.width = 600
        self.height = 600
        self.caption = "Space-invaders"
        self.bg_color = (255, 255, 255)
        self.bullet_speed_factor = .06
        self.bullet2_speed_factor = .12
        self.bullet2_color = (153, 0, 0)
        self.bullet2_width = 3
        self.bullet2_height = 7
        self.bullet_width = 3
        self.bullet_height = 6
        self.bullet_color = (60, 60, 60)
        self.alien_points = 50
