import pygame
import sys

pygame.init()

game_version = "v0.2"
screen_size = (1000, 800)
# (800,640)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(f'Passport To The Star {game_version}')


class Image:
    def __init__(self, path: str, size: tuple[float, float], alpha: int = 0, show: bool = True):
        self.path = path
        self.size = size
        self.alpha = alpha
        self.show = show
        self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), size)


background = Image('image/background.png', screen_size, 0)
start_logo = Image('image/start_logo.png', (750, 750), 0)
title_logo = Image('image/title_logo.png', (640, 80), 0)
start_button_normal = Image('image/start.png', (187.5, 100), 0)
start_button_hover = Image('image/start_hover.png', (187.5, 100), 0)
start_button_pressed = Image('image/start_pressed.png', (187.5, 100), 0)
quit_button_normal = Image('image/quit.png', (187.5, 100), 0)
quit_button_hover = Image('image/quit_hover.png', (187.5, 100), 0)
quit_button_pressed = Image('image/quit_pressed.png', (187.5, 100), 0)
game_background = Image('image/game_background.png', screen_size, 0)
passport_1 = Image('image/passport_1.png', (96,143.0625), 255)
passport_1_hover = Image('image/passport_1_hover.png', (187.5, 100), 255)
passport_1_pressed = Image('image/passport_1_pressed.png', (187.5, 100), 255)
passport_2 = Image('image/passport_2.png', (96,143.0625), 255)
passport_2_hover = Image('image/passport_1_hover.png', (187.5, 100), 255)
passport_2_pressed = Image('image/passport_1_pressed.png', (187.5, 100), 255)
passport_3 = Image('image/passport_3.png', (96,143.0625), 255)
passport_4 = Image('image/passport_4.png', (96,143.0625), 255)
passport_5 = Image('image/passport_5.png', (96,143.0625), 255)
# passport_hover = Image('image/passport_hover.png', (96,143.0625), 255)

passport = [passport_1,passport_2,passport_3,passport_4,passport_5,passport_5]

passport_details = Image('image/passport_details.png', (96,143.0625), 255)

splash_state = "fade_in"
menu_state = ""
game_state = "splash"
game_state = "main_game"
# title_state = "off"
button_pressed = ""

start_button_range = ((131.25, 582.5), (293.75, 667.5))
quit_button_range = ((131.25, 695), (285, 780))


start_button = [start_button_normal.image, start_button_hover.image, start_button_pressed.image]
start_button_index = 0

quit_button = [quit_button_normal.image, quit_button_hover.image, quit_button_pressed.image]
quit_button_index = 0

# passport_1 = [passport_1_normal.image, passport_1_hover.image, passport_1_pressed.image]
passport_1_index = 0

font_size = 50
target_size = 50
pixel_font = pygame.font.Font('font/GamePocket-Regular.ttf', font_size)

def mouse_in_start_button():
    return start_button_range[0][0] <= mouse_x <= start_button_range[1][0] and start_button_range[0][1] <= mouse_y <= \
        start_button_range[1][1]


def mouse_in_quit_button():
    return quit_button_range[0][0] <= mouse_x <= quit_button_range[1][0] and quit_button_range[0][1] <= mouse_y <= \
        quit_button_range[1][1]



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
        screen.blit(start_logo.image, start_logo.image.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2)))

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
        screen.fill("black")
        if menu_state == "fade_in":
            if background.alpha < 255:
                background.alpha += 5
            elif background.alpha >= 255:

                if title_logo.alpha < 255:
                    title_logo.alpha += 5
                    start_button_normal.alpha += 5
                    # credit_button_alpha += 5
                    quit_button_normal.alpha += 5
                elif title_logo.alpha >= 255:
                    menu_state = "hold"

        elif menu_state == "hold":
            if mouse_in_start_button():
                if not pygame.mouse.get_pressed()[0]:
                    start_button_index = 1
                    quit_button_index = 0
                elif pygame.mouse.get_pressed()[0]:
                    start_button_index = 2
                    quit_button_index = 0
                    button_pressed = "start"
                    
            elif mouse_in_quit_button():
                if not pygame.mouse.get_pressed()[0]:
                    quit_button_index = 1
                    start_button_index = 0
                elif pygame.mouse.get_pressed()[0]:
                    quit_button_index = 2
                    start_button_index = 0
                    button_pressed = "quit"
            else:
                start_button_index = 0
                quit_button_index = 0
                button_pressed = ""

        elif menu_state == "fade_out":
            if background.alpha > 0:
                background.alpha -= 3
                title_logo.alpha -= 3
                start_button_normal.alpha -= 3
                quit_button_normal.alpha -= 3
            elif button_pressed == "start":
                button_pressed = ""
                game_state = "main_game"
                game_screen = "fade in"
            elif button_pressed == "quit":
                button_pressed = ""
                pygame.quit()
                sys.exit()

        if not pygame.mouse.get_pressed()[0]:
            if mouse_in_start_button() and button_pressed == "start":
                start_button_index = 0
                quit_button_index = 0
                menu_state = "fade_out"
            elif mouse_in_quit_button() and button_pressed == "quit":
                start_button_index = 0
                quit_button_index = 0
                menu_state = "fade_out"

        background.image.set_alpha(background.alpha)
        title_logo.image.set_alpha(title_logo.alpha)
        start_button_normal.image.set_alpha(start_button_normal.alpha)
        # credit_button.set_alpha(credit_button_alpha)
        quit_button_normal.image.set_alpha(quit_button_normal.alpha)

        screen.blit(background.image, (0, 0))
        screen.blit(title_logo.image, title_logo.image.get_rect(center=(287.5, 87.5)))
        screen.blit(start_button[start_button_index], start_button_normal.image.get_rect(center=(212.5, 625)))
        screen.blit(quit_button[quit_button_index], quit_button_normal.image.get_rect(center=(212.5, 737.5)))

    if game_state == "main_game":
        if game_screen == "fade_in":
            if game_background.alpha < 255:
                game_background.alpha += 5
                game_background.image.set_alpha(game_background.alpha)
            elif game_background.alpha >= 255:
                game_screen = "hold"
        elif game_screen == "hold":
            pass

        if font_size != target_size:
            font_size = target_size



        screen.blit(game_background.image, (0, 0))
        for passport in passport:
            if passport.show:
                screen.blit(passport.image, passport.image.get_rect(center=(350, 640)))







    pygame.display.update()
    pygame.time.Clock().tick(60)
