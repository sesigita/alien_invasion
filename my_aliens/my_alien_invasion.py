import pygame
from pygame.sprite import Group
from my_settings import Settings
from my_ship import Ship
import my_game_functions as mgf
from my_game_stats import MyGameStats


def run_game():
  pygame.init()#initiation of pygame
  mai_settings = Settings()
  screen = pygame.display.set_mode((mai_settings.screen_width, mai_settings.screen_height))#creating display window of given dimentions
  pygame.display.set_caption("MY GAME")

  stats = MyGameStats(mai_settings)
  my_ship = Ship(mai_settings, screen)
  
  bullets = Group()
  balls = Group()
  mgf.create_balls(mai_settings, screen, balls)
  
  while True:
    mgf.check_events(mai_settings, screen, my_ship, bullets)
    if stats.game_active:
      my_ship.update()      
      mgf.update_bullets(mai_settings, screen, balls, bullets)
      mgf.update_balls(mai_settings, stats, my_ship, screen, balls)
    mgf.update_screen(mai_settings, stats, screen, my_ship, balls, bullets)  

run_game()