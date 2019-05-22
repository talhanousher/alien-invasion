import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions
from pygame.sprite import Group


def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.scree_height))
    pygame.display.set_caption(game_settings.game_caption)
    ship = Ship(game_settings, screen)
    alien = Alien(game_settings, screen)
    bullets = Group()
    while True:
        game_functions.check_events(game_settings, screen, ship, bullets)
        ship.update()
        game_functions.update_bullets(bullets)
        game_functions.update_screen(
            game_settings, screen, ship, alien, bullets)


run_game()
