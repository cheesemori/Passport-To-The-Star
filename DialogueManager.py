import pygame

class DialogueManager:
    def __init__(self):
        self.staff_questions = [
            "State your purpose for entering.",
            "Where are you arriving from?",
            "How long do you plan to stay?",
            "Do you have any items to declare?",
            "Is this your identification document?",
            "Have you been to this station before?",
            "Are you carrying any restricted materials?",
            "Why did you choose to travel today?"
        ]

        self.display_names = {
            "CaptainDarrow": "Captain Darrow",
            "Karea": "Karea",
            "JacksonB": "Jackson B",
        }

        self.answers = {
            "CaptainDarrow": [
                "Inspection duties. Classified.",
                "Sector 7 Forward Command.",
                "As long as command requires.",
                "Nothing to declare.",
                "Standard-issue military identification.",
                "Multiple times. Routine audits.",
                "Negative. Cleared by protocol Alpha-3.",
                "Orders were issued this morning.",
            ],
            "Karea": [
                "I seek refuge… please.",
                "The Eldran Wastes. Nothing remains there.",
                "I pray you allow me to stay permanently.",
                "Only my memories and what I could carry.",
                "It was damaged in the storms, but it is mine.",
                "No… I never made it this far before.",
                "Nothing dangerous. Only clothes.",
                "Today was my only chance to escape.",
            ],
            "JacksonB": [
                "Uhh… sightseeing? Yeah! Sightseeing.",
                "Um… a shuttle… from… somewhere?",
                "Just a tiny bit! Maybe!",
                "Noooo… definitely not! Why do you ask?",
                "Yep! That’s my passport! 100% mine.",
                "I think? Maybe? I don’t remember…",
                "Restricted? Me? Never! …Never.",
                "Because the shuttle guy said it was safe today!",
            ],
        }

        self.current_character = None
        self.staff_index = 0
        self.staff_text = ""
        self.character_text = ""

        self.font = pygame.font.Font(None, 26)

    def set_character(self, name: str):
        self.current_character = name
        self.reset_dialogue()

    def reset_dialogue(self):
        self.staff_index = 0
        self.staff_text = ""
        self.character_text = ""

    def ask_next(self):
        if self.current_character not in self.answers:
            self.staff_text = "STAFF: (no character selected)"
            self.character_text = ""
            return

        i = self.staff_index
        if i >= len(self.staff_questions):
            i = len(self.staff_questions) - 1

        # staff line
        self.staff_text = f"STAFF: {self.staff_questions[i]}"

        # character answer
        answer_list = self.answers[self.current_character]
        answer = answer_list[i] if i < len(answer_list) else "…"
        display_name = self.display_names.get(self.current_character, self.current_character)
        self.character_text = f"{display_name}: {answer}"

        # increment
        if self.staff_index < len(self.staff_questions) - 1:
            self.staff_index += 1

    
    def draw(self, screen):

        if not self.staff_text and not self.character_text:
            return

        width, height = screen.get_size()

        # CHARACTER BUBBLE — starts at (33, 509)
        if self.character_text:
            # CHARACTER bubble
            char_rect = pygame.Rect(33, 510, width // 2 - 100, 60)
            pygame.draw.rect(screen, (60, 40, 40), char_rect)
            pygame.draw.rect(screen, (220, 180, 180), char_rect, 2)
            surface = self.font.render(self.character_text, True, (255, 235, 235))
            screen.blit(surface, (char_rect.x + 10, char_rect.y + 10))

        # STAFF BUBBLE — starts at (527, 553)
        if self.staff_text:
            staff_rect = pygame.Rect(527, 553, width//2 - 60, 70)
            pygame.draw.rect(screen, (40, 40, 70), staff_rect)
            pygame.draw.rect(screen, (200, 200, 220), staff_rect, 2)
            surface = self.font.render(self.staff_text, True, (235, 235, 250))
            screen.blit(surface, (staff_rect.x + 10, staff_rect.y + 10))