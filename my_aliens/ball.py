import pygame
from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):
  def __init__(self, mai_settings, screen):
    super().__init__()
    self.screen = screen
    self.mai_settings = mai_settings

    image_path = r'C:\Users\Sigita\Desktop\python_work\Part II\alien_invasion\my_aliens\images\ball.bmp'
    self.image = pygame.image.load(image_path)
    self.rect = self.image.get_rect()

   
   
    random_location = randint(0, self.mai_settings.screen_width)
    self.rect.x = random_location
    self.rect.y = self.rect.height

    self.y = float(self.rect.top)
  
  def blitme(self):
    self.screen.blit(self.image, self.rect)

  def update(self):
    self.y += self.mai_settings.ball_speed_factor
    self.rect.y = self.y