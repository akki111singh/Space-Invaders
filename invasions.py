import pygame
from settings import setting
from ship import Ship
import newgf as gf
from alien import Alien
from pygame.sprite import Group
from pygame import time
from scoreboard import Scoreboard


def run_game():

    pygame.init()

    set_screen = setting()
    screen = pygame.display.set_mode((set_screen.width, set_screen.height))
    pygame.display.set_caption(set_screen.caption)
    ship = Ship(screen)
    sb = Scoreboard(set_screen, screen)
    bullets = Group()
    bullets2 = Group()
    aliens = Group()

    while True:
        gf.check_events(set_screen, screen, ship, bullets, bullets2)
        ship.update()
        gf.update_screen(set_screen, screen, ship,
                         aliens, bullets, bullets2, sb)
        gf.update_bullets(set_screen, screen, aliens, bullets, bullets2, sb)


run_game()
