class Settings():

  def __init__(self):
    """ constant setings """
    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (135, 206, 250)

    # Bullet Settings:
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = 60, 60, 60
    self.bullets_allowed = 3
    self.bullet_limit = 2

    # Rectangular Settings
    self.rectangular_width, self.rectangular_height = 100, 100
    self.rectangular_color = 255, 255, 51

    self.speedup_scale = 1.1
    self.init_dynamic_settings()

  
  def init_dynamic_settings(self):
    """ dynamic settings """
    self.ship_speed = 1.5
    self.bullet_speed_factor = 1
    self.rectangular_speed_factor = 0.1
    # rect_direction: 1 represents down; -1 represents up
    self.rect_direction = 1
  
  def increase_speed(self):
    self.ship_speed *= self.speedup_scale
    self.bullet_speed_factor *= self.speedup_scale
    self.rectangular_speed_factor *= self.speedup_scale
