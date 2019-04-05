import sys
import pygame
from bullet import Bullet
from bullet import Bullet2
from alien import Alien
from pygame import time
from time import *

start_ticks = pygame.time.get_ticks()
second = [0]
flag = [0]
current = [0]
check = [0]


def check_keydown_events(event, set_screen, screen, ship, bullets, bullets2):
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(set_screen, screen, ship)
        bullets.add(new_bullet)
    elif event.key == pygame.K_s:
        new_bullet = Bullet2(set_screen, screen, ship)
        bullets2.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, set_screen, screen, ship, bullets):
    if event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False


def check_events(set_screen, screen, ship, bullets, bullets2):
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, set_screen, screen,
                                 ship, bullets, bullets2)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, set_screen, screen, ship, bullets)


def update_bullets(set_screen, screen, aliens, bullets, bullets2, sb):
    bullets.update()
    bullets2.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for bullet in bullets2.copy():
        if bullet.rect.bottom <= 0:
            bullets2.remove(bullet)

    collision = pygame.sprite.groupcollide(aliens, bullets, True, True)
    seconds = (pygame.time.get_ticks()-start_ticks)/1000
    current[0] = seconds
    for bullet in bullets2.sprites():
        for alien in aliens:
            if alien.rect.colliderect(bullet.rect):
                alien.image = pygame.image.load('images/alien2.bmp')
                flag[0] = 1
                second[0] = pygame.time.get_ticks()/1000
#	print second[0]

    if current[0]-second[0] == 5 and flag[0] == 1:
        flag[0] = 0
        aliens.empty()

    if len(aliens) == 0 and seconds % 10 == 0:
        create_fleet(set_screen, screen, aliens)

    if seconds % 10 == 8 and flag[0] == 0:
        aliens.empty()
    if collision:
        sb.score += set_screen.alien_points
        sb.prep_score()


#	print seconds
def create_fleet(set_screen, screen, aliens):
    alien = Alien(set_screen, screen)
    aliens.add(alien)


def update_screen(set_screen, screen, ship, aliens, bullets, bullets2, sb):
    screen.fill(set_screen.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for bullet in bullets2.sprites():
        bullet.draw_bullet()
    ship.blitme()
    sb.show_score()

    aliens.draw(screen)

    pygame.display.flip()
