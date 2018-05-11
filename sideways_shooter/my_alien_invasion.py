import pygame
from pygame.sprite import Group

import my_game_functions as mgf
from my_game_stats import GameStats
from my_settings import Settings
from my_ship import Ship
from rectangular import Rectangular
from button import Button


def run_game():
  pygame.init()#initiation of pygame
  mai_settings = Settings()
  screen = pygame.display.set_mode((mai_settings.screen_width, mai_settings.screen_height))#creating display window of given dimentions
  pygame.display.set_caption("SIDEWAY SHOOTER")
  play_button = Button(mai_settings, screen, "Play!")

  stats = GameStats(mai_settings)
  my_ship = Ship(mai_settings, screen)
  # Make a group to store bullets
  bullets = Group()
  rectangulars = Group()

  mgf.create_rect(mai_settings, stats, screen, rectangulars)

  while True:
    mgf.check_events(mai_settings, screen, stats, my_ship, bullets, play_button, rectangulars)
    if stats.game_active:
      my_ship.update()
      mgf.update_bullets(rectangulars, bullets, screen, mai_settings, stats, my_ship)
      mgf.update_rect(mai_settings, rectangulars)
    mgf.update_screen(mai_settings, screen, stats, my_ship, rectangulars, bullets, play_button)  

run_game()  

