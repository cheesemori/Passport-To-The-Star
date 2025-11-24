import pygame
import sys
import random
from MicButton import MicButton
from DialogueManager import DialogueManager

pygame.init()

game_version = "v0.3"
screen_size = (1000, 800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(f'Passport To The Star {game_version}')

dev = True

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

character_list = [character_1, character_2, character_3]

CHARACTER_DIALOGUE_MAP = {
    0: "CaptainDarrow",
    1: "JacksonB",
    2: "Karea"
}

passport_details_1 = Image('image/passport_details_1.png', (420, 280), 255, show=False)
passport_details_2 = Image('image/passport_details_2.png', (420, 280), 255, show=False)
passport_details_3 = Image('image/passport_details_3.png', (420, 280), 255, show=False)

passport_details_list = [passport_details_1, passport_details_2, passport_details_3]

entry_permit = Image('image/entry_permit.png',(101,143.0625),255, show=False)
entry_permit_1 = Image('image/entry_permit_1.png',(236,344),255, show=False)
entry_permit_2 = Image('image/entry_permit_2.png',(236,344),255, show=False)
entry_permit_3 = Image('image/entry_permit_3.png',(236,344),255, show=False)

entry_permit_list = [entry_permit_1,entry_permit_2,entry_permit_3]

xray_1 = Image('image/character_1_xray.jpg',(256,384),255)
xray_2 = Image('image/character_2_xray.jpg',(256,384),255)
xray_3 = Image('image/character_3_xray.jpg',(256,384),255)
xray_background = Image('image/xray_background.png',(256,384),255)

xray_list = [xray_1,xray_2,xray_3]

tutorial = Image('image/tutorial.png', (984, 660), 255, show=False)
# guard image
guard = Image('image/guard.png', (500, 500), 255, show=False)

# stamp image
stamp_1 = Image('image/stamp.png',(80,80),255)
stamp_2 = Image('image/stamp.png',(80,80),255)

# accepted Image
accept = Image('image/accept.png',(270,270),255, show=False)
# rejected Image
reject = Image('image/reject.png',(270,270),255, show=False)
# mic Image
mic_button = MicButton("image/mic.png", (30, 630))
dialogue_manager = DialogueManager()

# xray button
xray_button = Image('image/xray_button.png', (115,53.5),255, show=False)

# states
mouse_clicked = False
splash_state = "fade_in"
menu_state = ""
game_state = "splash"
game_screen = "fade_in"
button_pressed = ""

# big change: do NOT start with a character; wait for NEXT click
go_next_round = False          # was True before
last_character_index = None
selected_character_index = -1

# will store the current character weight
current_weight = None

# guard / detain animation state
guard_active = False      # guard is walking in
guard_fading = False      # character should start fading
guard_pos_x = -200        # start off-screen on the left
guard_target_x = 250      # x position near the character
guard_speed = 3           # slower movement

# ranges
start_button_range = ((131.25, 582.5), (293.75, 667.5))
quit_button_range = ((131.25, 695), (285, 780))
passport_range = ((302, 570), (396, 711))
accept_stamp_range = ((580,690),(630,740))
reject_stamp_range = ((685,690),(735,740))
entry_permit_range = ((125,568),(225,712))
xray_button_range = ((410,658),(525,712))

# (468, 685) (115,53.5)

# next button rectangle (bottom right)
next_button_range = ((800, 650), (1000, 730))

# detain button centered at (911, 144) with width=80, height=50
button_width = 80
button_height = 50
center_x, center_y = 960, 144
detain_button_range = (
    (center_x - button_width // 2, center_y - button_height // 2),
    (center_x + button_width // 2, center_y + button_height // 2)
)

start_button = [start_button_normal.image, start_button_hover.image, start_button_pressed.image]
start_button_index = 0

quit_button = [quit_button_normal.image, quit_button_hover.image, quit_button_pressed.image]
quit_button_index = 0

font_size = 50
target_size = 50
pixel_font = pygame.font.Font('font/GamePocket-Regular.ttf', font_size)
detain_font = pygame.font.Font('font/GamePocket-Regular.ttf', 25)  # smaller text for detain button


def pixel_font_resize(font_size_resize: int):
    font = pygame.font.Font('font/GamePocket-Regular.ttf', font_size_resize)
    return font

clock = pygame.time.Clock()

if dev:
    game_state = "main_game"
    game_screen = "fade_in"

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


def mouse_in_detain_button(x, y):
    return detain_button_range[0][0] <= x <= detain_button_range[1][0] and \
           detain_button_range[0][1] <= y <= detain_button_range[1][1]


def mouse_in_accept_stamp(x, y):
    return accept_stamp_range[0][0] <= x <= accept_stamp_range[1][0] and \
           accept_stamp_range[0][1] <= y <= accept_stamp_range[1][1]

def mouse_in_reject_stamp(x, y):
    return reject_stamp_range[0][0] <= x <= reject_stamp_range[1][0] and \
           reject_stamp_range[0][1] <= y <= reject_stamp_range[1][1]

def mouse_in_entry_permit(x, y):
    return entry_permit_range[0][0] <= x <= entry_permit_range[1][0] and \
           entry_permit_range[0][1] <= y <= entry_permit_range[1][1]

def mouse_in_xray_button(x, y):
    return xray_button_range[0][0] <= x <= xray_button_range[1][0] and \
           xray_button_range[0][1] <= y <= xray_button_range[1][1]

def any_character_showing():
    return any(c.show for c in character_list)


def new_round(last_index):
    global passport_details_list, current_weight, selected_character_index
    global guard_active, guard_fading, guard_pos_x

    accept.show = False
    reject.show = False

    # hide all passports and characters
    for p in passport_list:
        p.show = False
    for c in character_list:
        c.show = False
        c.alpha = 255
        c.image.set_alpha(c.alpha)

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



    # generate random weight for this character
    selected_character_index = character_index
    current_weight = character_weight()

    dialogue_manager.set_character(CHARACTER_DIALOGUE_MAP[character_index])

    # reset guard state
    guard_active = False
    guard_fading = False
    guard_pos_x = -200
    guard.show = False

    # hide details for new round
    for d in passport_details_list:
        d.show = False

    return character_index


def character_weight():
    character_weight_dict = {0:"70",1:"13",2:"27"}
    return character_weight_dict[selected_character_index]


running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True
            if mic_button.is_clicked(event.pos):
                dialogue_manager.ask_next()
            print(f"mouse position: {event.pos}")

            # next / detain clicks in main game
            if event.button == 1 and game_state == "main_game" and game_screen == "hold":
                # NEXT: always allowed, this is what spawns the character
                if mouse_in_next_button(event.pos[0], event.pos[1]):
                    go_next_round = True
                    dialogue_manager.reset_dialogue()

                # DETAIN: only if a character is actually present
                elif mouse_in_detain_button(event.pos[0], event.pos[1]) and any_character_showing():
                    guard_active = True
                    guard_fading = False
                    guard_pos_x = -200
                    guard.show = True

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
    elif game_state == "main_game":
        screen.fill("black")
        game_background.image.set_alpha(game_background.alpha)
        screen.blit(game_background.image, (0, 0))
        # fade in game background
        if game_screen == "fade_in":
            if game_background.alpha < 255:
                game_background.alpha += 5
                # game_background.image.set_alpha(game_background.alpha)
            elif game_background.alpha >= 255:
                game_screen = "tutorial"
        elif game_screen == "tutorial":
            screen.blit(tutorial.image, tutorial.image.get_rect(center=(500,400)))
            if mouse_clicked:
                game_screen = "hold"
        elif game_screen == "hold":
            # only spawn character after NEXT clicked
            if go_next_round:
                last_character_index = new_round(last_character_index)
                go_next_round = False
            # draw passport
            for passport in passport_list:
                if passport.show:
                    screen.blit(passport.image, passport.image.get_rect(center=(350, 640)))
                    screen.blit(entry_permit.image, entry_permit.image.get_rect(center=(175, 640)))
                    if mouse_in_passport(mouse_x, mouse_y) and mouse_clicked:
                        passport_details_list[selected_character_index].show = not passport_details_list[selected_character_index].show
                    elif mouse_in_entry_permit(mouse_x, mouse_y) and mouse_clicked:
                        entry_permit_list[selected_character_index].show = not entry_permit_list[selected_character_index].show

            # draw character (fade only AFTER guard reaches character)
            for idx, character in enumerate(character_list):
                if character.show:
                    if guard_fading and idx == selected_character_index:
                        if character.alpha > 0:
                            character.alpha -= 3  # slower fade
                            if character.alpha < 0:
                                character.alpha = 0
                            character.image.set_alpha(character.alpha)
                    screen.blit(character.image, character.image.get_rect(center=(250, 260)))

            # draw weight label
            if current_weight is not None:
                weight_text = pixel_font.render(f"{current_weight}kg", True, (0, 0, 0))
                screen.blit(weight_text, weight_text.get_rect(center=(471, 413)))

            # draw next button
            btn_x1, btn_y1 = next_button_range[0]
            btn_x2, btn_y2 = next_button_range[1]
            btn_width = btn_x2 - btn_x1
            btn_height = btn_y2 - btn_y1

            if mouse_in_next_button(mouse_x, mouse_y):
                rect_color = (255, 255, 255)
            else:
                rect_color = (200, 200, 200)

            pygame.draw.rect(screen, rect_color, (btn_x1, btn_y1, btn_width, btn_height))
            pygame.draw.rect(screen, (0, 0, 0), (btn_x1, btn_y1, btn_width, btn_height), 3)

            next_text = pixel_font.render("NEXT", True, (0, 0, 0))
            next_text_rect = next_text.get_rect(center=((btn_x1 + btn_x2) // 2, (btn_y1 + btn_y2) // 2))
            screen.blit(next_text, next_text_rect)

            # draw detain button
            db_x1, db_y1 = detain_button_range[0]
            db_x2, db_y2 = detain_button_range[1]
            db_width = db_x2 - db_x1
            db_height = db_y2 - db_y1

            pygame.draw.rect(screen, (255, 0, 0), (db_x1, db_y1, db_width, db_height))
            pygame.draw.rect(screen, (0, 0, 0), (db_x1, db_y1, db_width, db_height), 2)

            detain_text = detain_font.render("DETAIN", True, (0, 0, 0))
            detain_text_rect = detain_text.get_rect(center=((db_x1 + db_x2) // 2, (db_y1 + db_y2) // 2))
            screen.blit(detain_text, detain_text_rect)

            # guard animation: from left to right, lower on screen (y = 260)
            if guard_active:
                guard_pos_x += guard_speed
                if guard_pos_x >= guard_target_x:
                    guard_pos_x = guard_target_x
                    guard_active = False
                    guard_fading = True  # only now start fading character
                screen.blit(guard.image, guard.image.get_rect(center=(guard_pos_x, 250)))

            # finish detain once character fully faded
            if guard_fading and character_list[selected_character_index].alpha <= 0:
                character_list[selected_character_index].show = False
                for p in passport_list:
                    p.show = False
                passport_details_list[selected_character_index].show = False
                current_weight = None
                go_next_round = False  # wait again for NEXT click
                guard_fading = False
                guard.show = False
                guard_pos_x = -200  # reset for next detain

            # show passport details if toggled
            if passport_details_list[selected_character_index].show:
                screen.blit(
                    passport_details_list[selected_character_index].image,
                    passport_details_list[selected_character_index].image.get_rect(center=(759, 381))
                )

            if entry_permit_list[selected_character_index].show:
                screen.blit(
                    entry_permit_list[selected_character_index].image,
                    entry_permit_list[selected_character_index].image.get_rect(center=(880, 381))
                )

            if mouse_in_accept_stamp(mouse_x, mouse_y) and mouse_clicked and character_list[selected_character_index].show and not reject.show:
                accept.show = True
            if mouse_in_reject_stamp(mouse_x, mouse_y)and mouse_clicked and character_list[selected_character_index].show and not accept.show:
                reject.show = True

            screen.blit(stamp_1.image, stamp_1.image.get_rect(center=(605, 715)))
            accept_text = pixel_font_resize(20).render("Accept", True, (184,223,106))
            screen.blit(accept_text, accept_text.get_rect(center=(605, 755)))

            screen.blit(stamp_2.image, stamp_2.image.get_rect(center=(710, 715)))
            accept_text = pixel_font_resize(20).render("Reject", True, (191,64,147))
            screen.blit(accept_text, accept_text.get_rect(center=(710, 755)))

            if accept.show:
                screen.blit(accept.image, accept.image.get_rect(center=(767, 132)))
            elif reject.show:
                screen.blit(reject.image, reject.image.get_rect(center=(767, 132)))

            screen.blit(xray_button.image, xray_button.image.get_rect(center=(468, 685)))

            mic_button.draw(screen)
            dialogue_manager.draw(screen)

            if mouse_in_xray_button(mouse_x,mouse_y) and pygame.mouse.get_pressed()[0]:
                if selected_character_index == -1:
                    screen.blit(xray_background.image, xray_background.image.get_rect(center=(490, 182)))
                else:
                    screen.blit(xray_list[selected_character_index].image, xray_list[selected_character_index].image.get_rect(center=(490, 182)))



    if mouse_clicked:
        mouse_clicked = False

    pygame.display.update()
    clock.tick(60)
