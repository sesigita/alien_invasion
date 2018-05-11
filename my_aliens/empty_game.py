import sys
import pygame

def game_fun():
  pygame.init()
  screen = pygame.display.set_mode((1000, 1000))

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        print(event.key)
    pygame.display.flip()


game_fun()