import sys
import pygame
from bullet import Bullet
from rectangular import Rectangular
from time import sleep

def check_keydown_events(event, ai_settings, screen, stats, ship, bullets, rectangulars):
  if event.key == pygame.K_RIGHT:
    ship.moving_right = True
  elif event.key == pygame.K_LEFT:
    ship.moving_left = True
  elif event.key == pygame.K_UP:
    ship.moving_up = True
  elif event.key == pygame.K_DOWN:
    ship.moving_down = True
  elif event.key == pygame.K_SPACE:
    fire_bullet(bullets, ai_settings, screen, ship)
  elif event.key == pygame.K_q:
    sys.exit()
  elif event.key == pygame.K_p and not stats.game_active:
    play_clicked(ai_settings, screen, stats, ship, bullets, rectangulars)

def check_keyup_events(event, ship):
  if event.key == pygame.K_RIGHT:
    ship.moving_right = False
  elif event.key == pygame.K_LEFT:
    ship.moving_left = False
  elif event.key == pygame.K_UP:
    ship.moving_up = False
  elif event.key == pygame.K_DOWN:
    ship.moving_down = False

def check_events(ai_settings, screen, stats, ship, bullets, play_button, rectangulars):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()   
    elif event.type == pygame.KEYDOWN:
      check_keydown_events(event, ai_settings, screen, stats, ship, bullets, rectangulars)
    elif event.type == pygame.KEYUP:
      check_keyup_events(event, ship)
    elif event.type == pygame.MOUSEBUTTONDOWN:
      mouse_x, mouse_y = pygame.mouse.get_pos()
      check_play_button(ai_settings, screen, stats, ship, bullets, rectangulars, play_button, mouse_x, mouse_y)  

def check_play_button(ai_settings, screen, stats, ship, bullets, rectangulars, play_button, mouse_x, mouse_y):
  button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y) 
  if button_clicked and not stats.game_active:
    play_clicked(ai_settings, screen, stats, ship, bullets, rectangulars)

def play_clicked(ai_settings, screen, stats, ship, bullets, rectangulars):
  stats.reset_stats()
  rectangulars.empty()
  bullets.empty()
  create_rect(ai_settings, stats, screen, rectangulars)
  ship.center_ship()
  pygame.mouse.set_visible(False)
  stats.game_active = True

def update_screen(mai_settings, screen, stats, ship, rectangulars, bullets, play_button):
  screen.fill(mai_settings.bg_color)
  for bullet in bullets.sprites():
    bullet.draw_bullet()
  ship.blitme()
  for rectangular in rectangulars.sprites():
    rectangular.draw_rect()

  if not stats.game_active:
    play_button.draw_button()
  pygame.display.flip()

def update_bullets(rectangulars, bullets, screen, mai_settings, stats, ship):
  bullets.update()
  for bullet in bullets.copy():
    if bullet.rect.left >= mai_settings.screen_width:
      bullets.remove(bullet)
      missed_target(mai_settings,stats, rectangulars, bullets, ship)
  check_collision(rectangulars, bullets, stats, screen, mai_settings, ship)


def missed_target(mai_settings, stats, rectangulars, bullets, ship):
  if stats.bullets_left > 0:
    stats.bullets_left -= 1
    print(stats.bullets_left)
    ship.center_ship()
    sleep(2)
  else:
    rectangulars.empty()
    stats.game_active = False
    mai_settings.init_dynamic_settings()
    pygame.mouse.set_visible(True)
    
def check_collision(rectangulars, bullets, stats, screen, mai_settings, ship ):
  collision = pygame.sprite.groupcollide(bullets, rectangulars, True, True)
  if collision:
    stats.reset_stats()
    ship.center_ship()
  if len(rectangulars) == 0:
    bullets.empty()
    mai_settings.increase_speed()
    create_rect(mai_settings, stats, screen, rectangulars)

def fire_bullet(bullets, ai_settings, screen, ship):
  if len(bullets) < ai_settings.bullets_allowed:
      new_bullet = Bullet(ai_settings, screen, ship)
      bullets.add(new_bullet)

def create_rect(ai_settings, stats, screen, rectangulars):
  if stats.bullets_left > 0:
    my_rect = Rectangular(ai_settings, screen)
    rectangulars.add(my_rect)

def update_rect(ai_settings, rectangulars):
  check_rect_edges(ai_settings, rectangulars)
  rectangulars.update()

def check_rect_edges(ai_settings, rectangulars):
  for rectangular in rectangulars.sprites():
    if rectangular.check_edges():
      change_rect_direction(ai_settings, rectangulars)
      break

def change_rect_direction(ai_settings, rectangulars):
  ai_settings.rect_direction *= -1