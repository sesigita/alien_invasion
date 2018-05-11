import sys
import pygame
from bullets import Bullet
from ball import Ball
from time import sleep

def check_keydown_events(event, mai_settings, screen, ship, bullets):
  if event.key == pygame.K_RIGHT:
    ship.moving_right = True
  elif event.key == pygame.K_LEFT:
    ship.moving_left = True
  elif event.key == pygame.K_UP:
    ship.moving_up = True
  elif event.key == pygame.K_DOWN:
    ship.moving_down = True
  elif event.key == pygame.K_SPACE:
   fire_bullets(mai_settings, screen, ship, bullets)

def fire_bullets(mai_settings, screen, ship, bullets):
  if len(bullets) < mai_settings.bullets_allowed:
    new_bullet = Bullet(mai_settings, screen, ship)
    bullets.add(new_bullet)

def check_keyup_events(event, ship):
  if event.key == pygame.K_RIGHT:
    ship.moving_right = False
  elif event.key == pygame.K_LEFT:
    ship.moving_left = False
  elif event.key == pygame.K_UP:
    ship.moving_up = False
  elif event.key == pygame.K_DOWN:
    ship.moving_down = False

def check_events(mai_settings, screen, ship, bullets):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()   
    elif event.type == pygame.KEYDOWN:
      check_keydown_events(event, mai_settings, screen, ship, bullets)
    elif event.type == pygame.KEYUP:
      check_keyup_events(event, ship)

def update_screen(mai_settings,stats, screen, ship, balls, bullets):
  screen.fill(mai_settings.bg_color)
  # update_ball(ball)
  for bullet in bullets.sprites():
    bullet.draw_bullet()
  
  ship.blitme()
  balls.draw(screen)
  check_ship_ball_collision(ship, balls)
  pygame.display.flip()

def update_bullets(ai_settings, screen, balls, bullets):
  bullets.update()
  for bullet in bullets.copy():
    if bullet.rect.bottom <= 0:
      bullets.remove(bullet)
  check_bullet_ball_collision(ai_settings, screen, balls, bullets)

def create_balls(ai_settings, screen, balls):
  ball = Ball(ai_settings, screen)
  balls.add(ball)

def update_balls(ai_settings, stats, ship, screen, balls):
  balls.update()
  for ball in balls.copy():
    if ball.rect.bottom >= ai_settings.screen_height:
      balls.remove(ball)
      missing_ball(ai_settings, stats, ship, screen, balls)

def check_ship_ball_collision(ship, balls):
  collisions = pygame.sprite.spritecollide(ship, balls, True)

def check_bullet_ball_collision(ai_settings, screen, balls, bullets):
  collisions = pygame.sprite.groupcollide(balls, bullets, True, True)
  if len(balls) <= 0:
    create_balls(ai_settings, screen, balls)

def missing_ball(ai_settings, stats, ship, screen, balls):
  if stats.balls_left > 0:
    stats.balls_left -= 1

    create_balls(ai_settings, screen, balls)
    sleep(0.5)
  else:
    stats.game_active = False
    ai_settings.bg_color = (0, 0, 0)
    