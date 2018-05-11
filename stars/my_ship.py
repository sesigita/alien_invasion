import pygame

class Ship():

  def __init__(self, ai_settings, screen):
    self.screen = screen
    self.ai_settings = ai_settings
    img_location = r"C:\Users\Sigita\Desktop\python_work\Part II\alien_invasion\sideways_shooter\images\rocket.bmp"
    self.image = pygame.image.load(img_location)
    self.rect = self.image.get_rect()
    self.screen_rect = self.screen.get_rect()

    self.rect.left = self.screen_rect.left
    self.rect.centery = self.screen_rect.centery
    self.center = float(self.rect.centerx)
    self.centeringy = float(self.rect.centery)
    self.moving_up = False
    self.moving_down = False
  
  def update(self):
    if self.moving_up and self.rect.top > self.screen_rect.top:
      self.centeringy -= self.ai_settings.ship_speed
    if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
      self.centeringy += self.ai_settings.ship_speed
    self.rect.centerx = self.center
    self.rect.centery = self.centeringy
      

  def blitme(self):
    self.screen.blit(self.image, self.rect)