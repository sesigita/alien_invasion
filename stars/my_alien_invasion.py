import pygame
from pygame.sprite import Group
from my_settings import Settings
import my_game_functions as mgf


def run_game():
  pygame.init()#initiation of pygame
  mai_settings = Settings()
  screen = pygame.display.set_mode((mai_settings.screen_width, mai_settings.screen_height))#creating display window of given dimentions
  pygame.display.set_caption("STARS")

  stars = Group()
  mgf.create_fleet(mai_settings, screen, stars)

  while True:
    mgf.check_events(mai_settings, screen)
    mgf.update_raindrops(mai_settings, screen, stars)
    mgf.update_screen(mai_settings, screen, stars)  

run_game()  