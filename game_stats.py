import json
class GameStats():

  def __init__(self, ai_settings):
    self.ai_settings = ai_settings
    self.reset_stats()
    self.game_active = False
    #High score should newer be reset
    filename = "scores.json"
    # self.high_score = 0
  
    with open(filename) as f_obj:
      self.high_score = json.load(f_obj)
    
  
  def reset_stats(self):
    self.ships_left = self.ai_settings.ship_limit
    self.score = 0
    self.level = 1