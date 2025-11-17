import pygame
import sys
import random

pygame.init()

game_version = "v0.2"
screen_size = (1000, 800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(f'Passport To The Star {game_version}')


class Image:
    def __init__(self, path: str, size: tuple[float, float], alpha: int = 0, show: bool = True):
        self.path = path
        self.size = size
        self.alpha = alpha
        self.show = show
        self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), size)
        self.rect = self.image.get_rect()


# images
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

passport_1 = Image('image/passport_1.png', (96, 143.0625), 255, show=False)
passport_1_hover = Image('image/passport_1_hover.png', (187.5, 100), 255)
passport_1_pressed = Image('image/passport_1_pressed.png', (187.5, 100), 255)

passport_2 = Image('image/passport_2.png', (96, 143.0625), 255, show=False)
passport_2_hover = Image('image/passport_1_hover.png', (187.5, 100), 255)
passport_2_pressed = Image('image/passport_1_pressed.png', (187.5, 100), 255)

passport_3 = Image('image/passport_3.png', (96, 143.0625), 255, show=False)
passport_4 = Image('image/passport_4.png', (96, 143.0625), 255, show=False)
passport_5 = Image('image/passport_5.png', (96, 143.0625), 255, show=False)

passport_list = [passport_1, passport_2, passport_3, passport_4, passport_5]

character_1 = Image('image/character_1.png', (500, 500), 255, show=False)
character_2 = Image('image/character_2.png', (500, 500), 255, show=False)
character_3 = Image('image/character_3.png', (500, 500), 255, show=False)
character_4 = Image('image/character_4.png', (500, 500), 255, show=False)
character_5 = Image('image/character_5.png', (500, 500), 255, show=False)
character_6 = Image('image/character_6.png', (500, 500), 255, show=False)
character_7 = Image('image/character_7.png', (500, 500), 255, show=False)
character_list = [character_1, character_2, character_3, character_4, character_5, character_6, character_7]

passport_details = Image('image/passport_details.png', (420, 280), 255, show=False)






# states
mouse_clicked = False
splash_state = "fade_in"
menu_state = ""
game_state = "splash"
game_screen = "fade_in"
button_pressed = ""
go_next_round = True
last_character_index = None

# game_state = "main_game"
# game_screen = "fade_in"


# will store the current character weight
current_weight = None

# ranges
start_button_range = ((131.25, 582.5), (293.75, 667.5))
quit_button_range = ((131.25, 695), (285, 780))
passport_range = ((302, 570), (396, 711))

# next button rectangle (bottom right)
next_button_range = ((800, 650), (1000, 730))

start_button = [start_button_normal.image, start_button_hover.image, start_button_pressed.image]
start_button_index = 0

quit_button = [quit_button_normal.image, quit_button_hover.image, quit_button_pressed.image]
quit_button_index = 0

passport_1_index = 0

font_size = 50
target_size = 50
pixel_font = pygame.font.Font('font/GamePocket-Regular.ttf', font_size)

clock = pygame.time.Clock()


def mouse_in_start_button(x, y):
    return start_button_range[0][0] <= x <= start_button_range[1][0] and \
           start_button_range[0][1] <= y <= start_button_range[1][1]


def mouse_in_quit_button(x, y):
    return quit_button_range[0][0] <= x <= quit_button_range[1][0] and \
           quit_button_range[0][1] <= y <= quit_button_range[1][1]


def mouse_in_passport(x, y):
    return passport_range[0][0] <= x <= passport_range[1][0] and \
           passport_range[0][1] <= y <= passport_range[1][1]


def mouse_in_next_button(x, y):
    return next_button_range[0][0] <= x <= next_button_range[1][0] and \
           next_button_range[0][1] <= y <= next_button_range[1][1]


def new_round(last_index):
    global passport_details, current_weight

    # hide all passports and characters
    for p in passport_list:
        p.show = False
    for c in character_list:
        c.show = False

    # close details when new round starts
    passport_details.show = False

    # choose character (not same as last one if possible)
    if last_index is None:
        character_index = random.randint(0, len(character_list) - 1)
    else:
        while True:
            character_index = random.randint(0, len(character_list) - 1)
            if character_index != last_index:
                break

    # choose random passport
    passport_index = random.randint(0, len(passport_list) - 1)

    passport_list[passport_index].show = True
    character_list[character_index].show = True

    # generate random weight for this character (you can change range later)
    current_weight = random.randint(50, 90)  # e.g. 50–120 kg

    return character_index


running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True
            print(f"mouse position: {event.pos}")

            # next button click in main game
            if event.button == 1 and game_state == "main_game" and game_screen == "hold":
                if mouse_in_next_button(event.pos[0], event.pos[1]):
                    go_next_round = True

    # splash screen
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

    # main menu
    elif game_state == "main_menu":
        screen.fill("black")

        if menu_state == "fade_in":
            if background.alpha < 255:
                background.alpha += 5
            elif background.alpha >= 255:
                if title_logo.alpha < 255:
                    title_logo.alpha += 5
                    start_button_normal.alpha += 5
                    quit_button_normal.alpha += 5
                elif title_logo.alpha >= 255:
                    menu_state = "hold"

        elif menu_state == "hold":
            if mouse_in_start_button(mouse_x, mouse_y):
                if not pygame.mouse.get_pressed()[0]:
                    start_button_index = 1
                    quit_button_index = 0
                elif pygame.mouse.get_pressed()[0]:
                    start_button_index = 2
                    quit_button_index = 0
                    button_pressed = "start"

            elif mouse_in_quit_button(mouse_x, mouse_y):
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
                game_screen = "fade_in"
            elif button_pressed == "quit":
                button_pressed = ""
                pygame.quit()
                sys.exit()

        if not pygame.mouse.get_pressed()[0]:
            if mouse_in_start_button(mouse_x, mouse_y) and button_pressed == "start":
                start_button_index = 0
                quit_button_index = 0
                menu_state = "fade_out"
            elif mouse_in_quit_button(mouse_x, mouse_y) and button_pressed == "quit":
                start_button_index = 0
                quit_button_index = 0
                menu_state = "fade_out"

        background.image.set_alpha(background.alpha)
        title_logo.image.set_alpha(title_logo.alpha)
        start_button_normal.image.set_alpha(start_button_normal.alpha)
        quit_button_normal.image.set_alpha(quit_button_normal.alpha)

        screen.blit(background.image, (0, 0))
        screen.blit(title_logo.image, title_logo.image.get_rect(center=(287.5, 87.5)))
        screen.blit(start_button[start_button_index], start_button_normal.image.get_rect(center=(212.5, 625)))
        screen.blit(quit_button[quit_button_index], quit_button_normal.image.get_rect(center=(212.5, 737.5)))

    # main game
    if game_state == "main_game":
        screen.fill("black")

        # fade in game background
        if game_screen == "fade_in":
            if game_background.alpha < 255:
                game_background.alpha += 5
                game_background.image.set_alpha(game_background.alpha)
            elif game_background.alpha >= 255:
                game_screen = "hold"

        elif game_screen == "hold":
            if go_next_round:
                last_character_index = new_round(last_character_index)
                go_next_round = False

        if font_size != target_size:
            font_size = target_size

        # draw game background
        screen.blit(game_background.image, (0, 0))

        # draw passport
        for passport in passport_list:
            if passport.show:
                screen.blit(passport.image, passport.image.get_rect(center=(350, 640)))
                if mouse_in_passport(mouse_x, mouse_y) and mouse_clicked:
                    passport_details.show = not passport_details.show

        # draw character
        for character in character_list:
            if character.show:
                screen.blit(character.image, character.image.get_rect(center=(250, 260)))

        # draw weight label (you can change position later)
        if current_weight is not None:
            weight_text = pixel_font.render(f"{current_weight} kg", True, (0, 0, 0))
            # placeholder position (right side, near top)
            screen.blit(weight_text, (419, 383))

        # draw next button
        btn_x1, btn_y1 = next_button_range[0]
        btn_x2, btn_y2 = next_button_range[1]
        btn_width = btn_x2 - btn_x1
        btn_height = btn_y2 - btn_y1

        # simple hover effect
        if mouse_in_next_button(mouse_x, mouse_y):
            rect_color = (255, 255, 255)  # white when hover
        else:
            rect_color = (200, 200, 200)  # light grey

        pygame.draw.rect(screen, rect_color, (btn_x1, btn_y1, btn_width, btn_height))
        pygame.draw.rect(screen, (0, 0, 0), (btn_x1, btn_y1, btn_width, btn_height), 3)  # black border

        next_text = pixel_font.render("NEXT", True, (0, 0, 0))
        next_text_rect = next_text.get_rect(center=((btn_x1 + btn_x2) // 2, (btn_y1 + btn_y2) // 2))
        screen.blit(next_text, next_text_rect)

        # show passport details if toggled
        if passport_details.show:
            screen.blit(passport_details.image, passport_details.image.get_rect(center=(759, 381)))



    if mouse_clicked:
        mouse_clicked = False
    pygame.display.update()
    clock.tick(60)
