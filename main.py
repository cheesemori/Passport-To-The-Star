import pygame
import sys

pygame.init()

game_version = "v0.1"
screen = pygame.display.set_mode((800, 640))
pygame.display.set_caption(f'Passport To The Star {game_version}')
background_image = pygame.image.load('image/background.jpg').convert()

background = pygame.transform.scale(background_image, (800, 640))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    pygame.display.update()


