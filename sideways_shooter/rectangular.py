import pygame
from pygame.sprite import Sprite
from random import randint

class Rectangular(Sprite):
  def __init__(self, ai_settings, screen):
    super().__init__()
    self.screen = screen
    self.ai_settings = ai_settings
    self.rect = pygame.Rect( 0, 0, ai_settings.rectangular_width, ai_settings.rectangular_height)
    self.rect.x = ai_settings.screen_width - self.rect.width * 1.5
    self.x = self.rect.x
    ## Rendom Y coordinate
    # self.rect.y = randint(0, ai_settings.screen_height - self.rect.height)

    # Top of the screen (Y coordinate)
    self.rect.y = self.rect.height * 0.5

    self.y = float(self.rect.y)
  
    self.color = ai_settings.rectangular_color
    self.speed_factor = ai_settings.rectangular_speed_factor

  def draw_rect(self):
    pygame.draw.rect(self.screen, self.color, self.rect)

  def update(self):
    self.y += self.speed_factor * self.ai_settings.rect_direction
    self.rect.y = self.y
  
  def check_edges(self):
    screen_rect = self.screen.get_rect()
    if self.rect.top <= 0:
      return True
    if self.rect.bottom >= screen_rect.bottom:
      return True