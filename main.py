import pygame
import sys

pygame.init()

game_version = "v0.1"
screen = pygame.display.set_mode((800, 640))
pygame.display.set_caption(f'Passport To The Star {game_version}')

background_image = pygame.image.load('image/background.png').convert_alpha()
background = pygame.transform.scale(background_image, (800, 640))

start_logo_image = pygame.image.load('image/start_logo.png').convert_alpha()
start_logo = pygame.transform.scale(start_logo_image, (600,600))

title_logo_image = pygame.image.load('image/title_logo.png').convert_alpha()
title_logo = pygame.transform.scale(title_logo_image, (512,64))

start_button_image = pygame.image.load('image/start.png').convert_alpha()
start_button = pygame.transform.scale(start_button_image, (150,80))
credit_button_image = pygame.image.load('image/credit.png').convert_alpha()
credit_button = pygame.transform.scale(credit_button_image, (150,80))
quit_button_image = pygame.image.load('image/quit.png').convert_alpha()
quit_button = pygame.transform.scale(quit_button_image, (150,80))

splash_logo_alpha = 0
background_alpha = 0
title_logo_alpha = 0
start_button_alpha = 0
credit_button_alpha = 0
quit_button_alpha = 0

splash_state = "fade_in"

game_state = "splash"

title_state = "off"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(f"鼠标点击坐标: {event.pos}")

    if game_state == "splash":

        screen.fill("black")
        start_logo.set_alpha(splash_logo_alpha)
        screen.blit(start_logo, start_logo.get_rect(center=(800 // 2, 640 // 2)))

        if splash_state == "fade_in":
            splash_logo_alpha += 3
            if splash_logo_alpha >= 255:
                splash_logo_alpha = 255
                splash_state = "hold"
                hold_start_time = pygame.time.get_ticks()
        elif splash_state == "hold":
            current_time = pygame.time.get_ticks()
            if current_time - hold_start_time >= 1250:
                splash_state = "fade_out"
        elif splash_state == "fade_out":
            splash_logo_alpha -= 3
            if splash_logo_alpha <= 0:
                game_state = "main_menu"


    elif game_state == "main_menu":
        if background_alpha < 255:
            background_alpha += 5
        elif background_alpha >= 255:
            title_state = "on"
            if title_logo_alpha < 255:
                title_logo_alpha += 5
                start_button_alpha += 5
                credit_button_alpha += 5
                quit_button_alpha += 5


        background.set_alpha(background_alpha)
        screen.blit(background, (0, 0))
        title_logo.set_alpha(title_logo_alpha)
        screen.blit(title_logo, title_logo.get_rect(center=(230,70)))
        start_button.set_alpha(start_button_alpha)
        credit_button.set_alpha(credit_button_alpha)
        quit_button.set_alpha(quit_button_alpha)
        screen.blit(start_button, start_button.get_rect(center=(170,500)))
        screen.blit(quit_button,quit_button.get_rect(center=(170,590)))


    pygame.display.update()
    pygame.time.Clock().tick(60)





