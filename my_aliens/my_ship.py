import pygame

class Ship():

  def __init__(self, ai_settings, screen):
    self.screen = screen
    self.ai_settings = ai_settings
    img_location = r"C:\Users\Sigita\Desktop\python_work\Part II\alien_invasion\my_aliens\images\rocket.bmp"
    self.image = pygame.image.load(img_location)
    self.rect = self.image.get_rect()
    self.screen_rect = self.screen.get_rect()

    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom
    #self.rect.centery = self.screen_rect.centery
    self.center = float(self.rect.centerx)
    self.centeringy = float(self.rect.centery)
    self.moving_right = False
    self.moving_left = False
    self.moving_up = False
    self.moving_down = False
  
  def update(self):
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.center += self.ai_settings.ship_speed
    if self.moving_left and self.rect.left > 0:
      self.center -= self.ai_settings.ship_speed
    if self.moving_up and self.rect.top > self.screen_rect.top:
      self.centeringy -= self.ai_settings.ship_speed
    if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
      self.centeringy += self.ai_settings.ship_speed
    self.rect.centerx = self.center
    self.rect.centery = self.centeringy
      

  def blitme(self):
    self.screen.blit(self.image, self.rect)