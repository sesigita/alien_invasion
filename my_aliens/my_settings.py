class Settings():

  def __init__(self):
    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (135, 206, 250)
    self.ship_speed = 1.5
    # Bullets
    self.bullet_speed_factor = 1 
    self.bullet_width = 200
    self.bullet_height = 15
    self.bullet_color = 255, 40, 0
    self.bullets_allowed = 3

    # Ball
    self.ball_speed_factor = 1
    self.ball_limit = 2