import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

  def __init__(self, ai_settings, screen):
    """Initialize the ship and set its starting position."""
    super().__init__()
    self.screen = screen
    self.ai_settings = ai_settings

    # Load the ship image and get its rect.
    ship_file = r'C:\Users\Sigita\Desktop\python_work\Part II\alien_invasion\images\ship.bmp'
    self.image = pygame.image.load(ship_file)
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    # Start each new ship at the bottom center of the screen.
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom

    # Store a decimal value for the ship's center.
    self.center = float(self.rect.centerx)

    # Movement flag
    self.moving_right = False
    self.moving_left = False

  def update(self):
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.center += self.ai_settings.ship_speed_factor
    if self.moving_left and self.rect.left > 0:
      self.center -= self.ai_settings.ship_speed_factor
    
    self.rect.centerx = self.center

  def blitme(self):
    self.screen.blit(self.image, self.rect)

  def center_ship(self):
    self.center = self.screen_rect.centerx