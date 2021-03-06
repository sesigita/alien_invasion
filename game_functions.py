import sys
import pygame
import json
from bullet import Bullet
from alien import Alien
from time import sleep



def check_keydown_events(event, ai_settings, stats, sb, screen, ship, aliens, bullets):  
  if event.key == pygame.K_RIGHT:
    ship.moving_right = True
  elif event.key == pygame.K_LEFT:
    ship.moving_left = True
  elif event.key == pygame.K_SPACE:
    fire_bullets(ai_settings, screen, ship, bullets)
  elif event.key == pygame.K_q:     
    sys.exit()
  elif event.key == pygame.K_p:
    start_game(ai_settings, stats, sb, screen, ship, aliens, bullets)

def fire_bullets(ai_settings, screen, ship, bullets):
  bullet_sound = pygame.mixer.Sound(r"C:\Users\Sigita\Desktop\python_work\Part II\alien_invasion\Arrow_Swoosh_1.wav")
  if len(bullets) < ai_settings.bullets_allowed:
    new_bullet = Bullet(ai_settings, screen, ship)
    pygame.mixer.Sound.play(bullet_sound)
    bullets.add(new_bullet)

def check_keyup_events(event, ship):
  if event.key == pygame.K_RIGHT:
    ship.moving_right = False
  if event.key == pygame.K_LEFT:
    ship.moving_left = False

def check_event(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      filename = "scores.json"
      with open(filename, 'w') as f_obj:
        json.dump(stats.high_score, f_obj)
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      check_keydown_events(event, ai_settings, stats, sb, screen, ship, aliens, bullets)
    elif event.type == pygame.KEYUP:
      check_keyup_events(event, ship)
    elif event.type == pygame.MOUSEBUTTONDOWN:
      mouse_x, mouse_y = pygame.mouse.get_pos()
      check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

# Original f
# def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
#   button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
#   if button_clicked and not stats.game_active:
#     pygame.mouse.set_visible(False)
#     stats.reset_stats()
#     stats.game_active = True

#     aliens.empty()
#     bullets.empty()

#     create_fleet(ai_settings, screen, aliens, ship)
#     ship.center_ship()

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
  button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
  if button_clicked and not stats.game_active:
    start_game(ai_settings, stats, sb, screen, ship, aliens, bullets)

def start_game(ai_settings, stats, sb, screen, ship, aliens, bullets):
  pygame.mouse.set_visible(False)
  stats.reset_stats()
  # ai_settings.initialize_dynamic_settings()
  stats.game_active = True
  sb.prep_images()
  aliens.empty()
  bullets.empty()

  create_fleet(ai_settings, screen, aliens, ship)
  ship.center_ship()

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
  screen.fill(ai_settings.bg_color)
  for bullet in bullets.sprites():
    bullet.draw_bullet()
  ship.blitme()
  aliens.draw(screen)
  # draw the score info
  sb.show_scores()
  if not stats.game_active:
    play_button.draw_button()
  # Make the most recently drawn screen visible.
  pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, bullets, aliens):
  bullets.update()
  for bullet in bullets.copy():
    if bullet.rect.bottom <= 0:
      bullets.remove(bullet)
  check_bullet_alien_collision(ai_settings, screen, stats, sb, aliens, ship, bullets)

def check_bullet_alien_collision(ai_settings, screen, stats, sb, aliens, ship, bullets):
  """Respond to bullet-alien collisions."""
  # Remove any bullets and aliens that have collided.
  collision = pygame.sprite.groupcollide(bullets, aliens, True, True) 
  if collision:
    for aliens in collision.values():
      stats.score += ai_settings.alien_points * len(aliens)
      sb.prep_score()
    check_high_score(stats, sb)
  start_new_level(ai_settings, screen, stats, ship, aliens, bullets, sb)

def start_new_level(ai_settings, screen, stats, ship, aliens, bullets, sb):
  if len(aliens) == 0:
    # Destroy existing bullets, speed up game, and create new fleet.
    bullets.empty()
    ai_settings.increase_speed()
    stats.level +=1
    sb.prep_level()
    create_fleet(ai_settings, screen, aliens, ship)

def get_number_aliens_x(ai_settings, alien_width):
  """Determine the number of aliens that fit in a row."""
  available_space_x = ai_settings.screen_width - (alien_width * 2)
  number_aliens_x = int(available_space_x / (alien_width*2))
  return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
  """Determine the number of rows of aliens that fit on the screen."""
  available_space_y = (ai_settings.screen_height - 
    (3 * alien_height) - ship_height)
  number_rows = int(available_space_y / (alien_height *2))
  return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
  """Create an alien and place it in the row."""
  alien = Alien(ai_settings, screen)
  alien_width = alien.rect.width
  alien.x = alien_width + 2 * alien_width * alien_number
  alien.rect.x = alien.x
  alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
  aliens.add(alien)

def create_fleet(ai_settings, screen, aliens, ship):
  """Create a full fleet of aliens."""
  # Create an alien and find the number of aliens in a row.
  alien = Alien(ai_settings, screen)
  number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
  number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
  # Create the fleet of aliens.
  for row_number in range(number_rows): 
    for alien_number in range(number_aliens_x):
      create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
  for alien in aliens.sprites():
    if alien.check_edges():
      change_fleet_direction(ai_settings, aliens)
      break

def change_fleet_direction(ai_settings, aliens):
  for alien in aliens.sprites():
    alien.rect.y += ai_settings.fleet_drop_speed
  ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
  check_fleet_edges(ai_settings, aliens)
  aliens.update()
  # Look for alien-ship collisions.
  if pygame.sprite.spritecollideany(ship, aliens):
    ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
  check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)
  
def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
  if stats.ships_left > 0:
    stats.ships_left -= 1

    sb.prep_ships()

    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings, screen, aliens, ship)
    ship.center_ship()

    sleep(0.5)
  else:
    stats.game_active = False
    pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
  for alien in aliens.sprites():
    if alien.rect.bottom >= ai_settings.screen_height:# or define screen_rect = screen.get_rect & check if its bottom is more than alien rect bottom
      ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
      break

def check_high_score(stats, sb):
  if stats.score > stats.high_score:
    stats.high_score = stats.score

    
    sb.prep_high_score()