import pygame

class Balls():

  def __init__(self, ai_settings, screen):
    self.screen = screen
    self.ai_settings = ai_settings
    img_location = r"C:\Users\Sigita\Desktop\python_work\Part II\alien_invasion\my_aliens\images\ball.bmp"
    self.image = pygame.image.load(img_location)
    self.rect = self.image.get_rect()
    self.screen_rect = self.screen.get_rect()

    self.rect.centerx = self.screen_rect.centerx
    self.rect.top = self.screen_rect.top
    #self.rect.centery = self.screen_rect.centery
    self.center = float(self.rect.centerx)
    self.y = float(self.rect.top)
   
  
  def update(self):
    self.rect.centerx = self.center
    self.rect.top = self.y
      

  def blitme(self):
    self.screen.blit(self.image, self.rect)