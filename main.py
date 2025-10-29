import pygame
import sys

pygame.init()

game_version = "v0.1"
screen = pygame.display.set_mode((800, 640))
pygame.display.set_caption(f'Passport To The Star {game_version}')

class Image:
    def __init__(self,path:str,size:tuple[int,int],alpha:int=0):
        self.path = path
        self.size = size
        self.alpha = alpha
        self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), size)



background = Image('image/background.png', (800, 640), 0)
start_logo = Image('image/start_logo.png', (600, 600), 0)
title_logo = Image('image/title_logo.png', (512, 64), 0)
start_button_normal = Image('image/start.png', (150, 80), 0)
start_button_hover = Image('image/start_hover.png', (150, 80), 0)
start_button_pressed = Image('image/start_pressed.png', (150, 80), 0)
quit_button_normal = Image('image/quit.png', (150, 80), 0)
quit_button_hover = Image('image/quit_hover.png', (150, 80), 0)
quit_button_pressed = Image('image/quit_pressed.png', (150, 80), 0)
"""
background_image = pygame.image.load('image/background.png').convert_alpha()
background = pygame.transform.scale(background_image, (800, 640))

start_logo_image = pygame.image.load('image/start_logo.png').convert_alpha()
start_logo = pygame.transform.scale(start_logo_image, (600,600))

title_logo_image = pygame.image.load('image/title_logo.png').convert_alpha()
title_logo = pygame.transform.scale(title_logo_image, (512,64))

start_button_normal_image = pygame.image.load('image/start.png').convert_alpha()
start_button_normal = pygame.transform.scale(start_button_normal_image, (150, 80))
credit_button_image = pygame.image.load('image/credit.png').convert_alpha()
credit_button = pygame.transform.scale(credit_button_image, (150,80))
quit_button_normal_image = pygame.image.load('image/quit.png').convert_alpha()
quit_button_normal = pygame.transform.scale(quit_button_normal_image, (150, 80))

start_button_hover_image = pygame.image.load('image/start_hover.png').convert_alpha()
start_button_hover = pygame.transform.scale(start_button_hover_image, (150,80))
quit_button_hover_image = pygame.image.load('image/quit_hover.png').convert_alpha()
quit_button_hover = pygame.transform.scale(quit_button_hover_image, (150,80))

start_button_pressed_image = pygame.image.load('image/start_pressed.png').convert_alpha()
start_button_pressed = pygame.transform.scale(start_button_pressed_image, (150,80))
quit_button_pressed_image = pygame.image.load('image/quit_pressed.png').convert_alpha()
quit_button_pressed = pygame.transform.scale(quit_button_pressed_image, (150,80))
"""
"""
start_logo.alpha = 0
background.alpha = 0
title_logo_alpha = 0
start_button_alpha = 0
credit_button_alpha = 0
quit_button_alpha = 0
"""
splash_state = "fade_in"
menu_state = ""
game_state = "splash"
title_state = "off"

start_button_range = ((105,466),(235,534))
quit_button_range = ((105,556),(228,624))

start_button = [start_button_normal.image, start_button_hover.image, start_button_pressed.image]
start_button_index = 0


quit_button = [quit_button_normal.image,quit_button_hover.image,quit_button_pressed.image]
quit_button_index = 0


def mouse_in_start_button():
    return start_button_range[0][0] <= mouse_x <= start_button_range[1][0] and start_button_range[0][1] <= mouse_y <= start_button_range[1][1]

def mouse_in_quit_button():
    return quit_button_range[0][0] <= mouse_x <= quit_button_range[1][0] and quit_button_range[0][1] <= mouse_y <= quit_button_range[1][1]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(f"mouse position: {event.pos}")

    mouse_x, mouse_y = pygame.mouse.get_pos()

    if game_state == "splash":

        screen.fill("black")
        start_logo.image.set_alpha(start_logo.alpha)
        screen.blit(start_logo.image, start_logo.image.get_rect(center=(800 // 2, 640 // 2)))

        if splash_state == "fade_in":
            start_logo.alpha += 3
            if start_logo.alpha >= 255:
                start_logo.alpha = 255
                splash_state = "hold"
                hold_start_time = pygame.time.get_ticks()
        elif splash_state == "hold":
            current_time = pygame.time.get_ticks()
            if current_time - hold_start_time >= 1250:
                splash_state = "fade_out"
        elif splash_state == "fade_out":
            start_logo.alpha -= 3
            if start_logo.alpha <= 0:
                game_state = "main_menu"
                menu_state = "fade_in"

    elif game_state == "main_menu":
        if menu_state == "fade_in":
            if background.alpha < 255:
                background.alpha += 5
            elif background.alpha >= 255:
                title_state = "on"
                if title_logo.alpha < 255:
                    title_logo.alpha += 5
                    start_button_normal.alpha += 5
                    # credit_button_alpha += 5
                    quit_button_normal.alpha += 5

        if mouse_in_start_button():
            if not pygame.mouse.get_pressed()[0]:
                start_button_index = 1

            elif pygame.mouse.get_pressed()[0]:
                start_button_index = 2
        elif mouse_in_quit_button():
            if not pygame.mouse.get_pressed()[0]:
                quit_button_index = 1
            elif pygame.mouse.get_pressed()[0]:
                quit_button_index = 2
        else:
            start_button_index = 0
            quit_button_index = 0

    background.image.set_alpha(background.alpha)
    title_logo.image.set_alpha(title_logo.alpha)
    start_button_normal.image.set_alpha(start_button_normal.alpha)
    # credit_button.set_alpha(credit_button_alpha)
    quit_button_normal.image.set_alpha(quit_button_normal.alpha)

    screen.blit(background.image, (0, 0))
    screen.blit(title_logo.image, title_logo.image.get_rect(center=(230, 70)))
    screen.blit(start_button[start_button_index], start_button_normal.image.get_rect(center=(170, 500)))
    screen.blit(quit_button[quit_button_index], quit_button_normal.image.get_rect(center=(170, 590)))












    pygame.display.update()
    pygame.time.Clock().tick(60)





