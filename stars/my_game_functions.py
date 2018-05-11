import sys
import pygame
from star import Star
from random import randint

def check_keydown_events(event):
  if event.key == pygame.K_q:
    sys.exit()

def check_events(ai_settings, screen):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()   

def update_screen(mai_settings, screen, stars):
  screen.fill(mai_settings.bg_color)
  stars.draw(screen)
  
  pygame.display.flip()

def get_number_stars_x(mai_settings, star_width):
  available_space_x = mai_settings.screen_width - star_width
  number_of_stars_in_x = int(available_space_x / ( 2 * star_width))
  return number_of_stars_in_x

def get_number_rows(mai_settings, star_height):
  available_space_y = mai_settings.screen_height - star_height
  number_of_rows_in_y = int(available_space_y / (star_height*2))
  return number_of_rows_in_y


def create_star(mai_settings, screen, stars, star_number, row_number):
  star = Star(mai_settings, screen)
  star_width = star.rect.width
  #Star grid
  star.rect.x = star_width + 2 * star_width * star_number
  star.rect.y = star.rect.height + 2 * star.rect.height * row_number
  star.y = star.rect.y
  
  #Random star grid
  # star.rect.x = randint(0, mai_settings.screen_width - star.rect.width)
  # star.rect.y = randint(0, mai_settings.screen_height - star.rect.height)
  # star.y = star.rect.y

  stars.add(star)


def create_fleet(mai_settings, screen, stars):
  star = Star(mai_settings, screen)
  number_stars_x = get_number_stars_x(mai_settings, star.rect.width)
  number_rows = get_number_rows(mai_settings, star.rect.height)

  for row_number in range(number_rows):
    for star_number in range(number_stars_x):
      create_star(mai_settings, screen, stars, star_number, row_number)
    
def update_raindrops(mai_settings, screen, stars):
  stars.update()  
  for star in stars.copy():

    if star.rect.top >= (mai_settings.screen_height):
      star.y = star.rect.height
      star.rect.y = star.y
