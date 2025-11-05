#Detain file
#this code is sectioned into 3 parts 

#These are the variables
characters = ["Dr. Zog", "Kraen", "Captain Rhen Darrow", "SC1", "SC2", "SC3", "SC4", "SC5", "SC6", "SC7"]
current_character_index = 0
# Detain button position
detain_button_rect = pygame.Rect(650, 200, 120, 60)  
detain_timer = 0
 # Length of detain animation in miliseconds
detain_duration = 2000 

# Guard placeholder movement
guard_pos_x = -100
guard_pos_y = 350


#This is part a the Border control screen and add it inside the main "while running" loop
elif game_state == "border_control":
    screen.fill((50, 50, 50))

    # Show character name
    character_name = characters[current_character_index]
    font = pygame.font.Font(None, 40)
    name_text = font.render(character_name, True, "white")
    screen.blit(name_text, (350, 200))

    # Character placeholder
    pygame.draw.rect(screen, "blue", pygame.Rect(370, 260, 60, 80))

    # DETAIN button
    pygame.draw.rect(screen, "white", detain_button_rect)
    font2 = pygame.font.Font(None, 32)
    detain_text = font2.render("DETAIN", True, "black")
    screen.blit(detain_text, (detain_button_rect.x + 10, detain_button_rect.y + 15))

    # Button click → Start detain animation
    if pygame.mouse.get_pressed()[0] and detain_button_rect.collidepoint(mouse_x, mouse_y):
        game_state = "detain_animation"
        detain_timer = pygame.time.get_ticks()
        guard_pos_x = -100


#This is the detain animation part 
elif game_state == "detain_animation":
    screen.fill((50, 50, 50))

    elapsed = pygame.time.get_ticks() - detain_timer
    guard_pos_x = int((elapsed / detain_duration) * 1000)

    # Draw guard
    pygame.draw.rect(screen, "red", pygame.Rect(guard_pos_x, guard_pos_y, 70, 110))

    # Draw character 
    pygame.draw.rect(screen, "blue", pygame.Rect(370, 260, 60, 80))

    # Animation finished → load next character
    if elapsed >= detain_duration:
        current_character_index = (current_character_index + 1) % len(characters)
        game_state = "border_control"
