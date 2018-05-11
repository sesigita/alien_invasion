import pygame
from pygame.sprite import Sprite

class Star(Sprite):

  def __init__(self, ai_settings, screen):
    super().__init__()
    self.screen = screen
    self.ai_settings = ai_settings

    star_image = r'C:\Users\Sigita\Desktop\python_work\Part II\alien_invasion\stars\images\raindrop.bmp'
    self.image = pygame.image.load(star_image)
    self.rect = self.image.get_rect()
    self.screen_rect = self.screen.get_rect()

    self.rect.x = self.rect.width
    self.rect.y = self.rect.height

    self.y = float(self.rect.y)

  def blitme(self):
    """Draw the alien at its current location."""
    self.screen.blit(self.image, self.rect)

  def update(self):
    """makes all drops to be placed at the top ???? """
    self.y += self.ai_settings.raindrops_speed_factor 
    self.rect.y = self.y
   