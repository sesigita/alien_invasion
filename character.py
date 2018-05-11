import pygame

class Character():
  def __init__(self, screen):
    self.screen = screen
    self.character = r'C:\Users\Sigita\Desktop\python_work\Part II\alien_invasion\images\rocket.bmp'
    self.image = pygame.image.load(self.character)
    self.rect = self.image.get_rect()
    self.screen_rect = self.screen.get_rect()

    self.rect.centerx = self.screen_rect.centerx
    self.rect.centery = self.screen_rect.centery

  def blitme(self):
    self.screen.blit(self.image, self.rect)