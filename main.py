import pygame
import sys

pygame.init()

game_version = "v0.1"
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption(f'Passport To The Star {game_version}')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


