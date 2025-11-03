class DialogueManager:
    def __init__(self):
        # character dialogues (i can change these if you guys dont like them!)
        self.dialogues = {
            "DrZog": [
                "Oh dear... they said the experiment was illegal!",
                "You don't understand, my work can save lives!",
                "Please, don’t report me — I just need more time.",
                "My research could heal worlds, not destroy them!",
                "You have to trust me, inspector... for everyone’s sake."
            ],
            "Kraen": [
                "The Memory Stone must be protected.",
                "Truth fades when no one remembers.",
                "My people were erased once. Never again.",
                "Let me pass. History is more fragile than flesh.",
                "If I fail, no one will know we ever existed."
            ],
            "CaptainRhen": [
                "Papers, please. Regulations are clear.",
                "Do you question my duty, citizen?",
                "Every day feels the same... inspect, approve, deny.",
                "Sometimes, I wonder if I’m the villain here.",
                "The rules keep us safe — or so they say."
            ],
            "Merchant": [
                "I have travel permits right here — totally valid!",
                "Don’t open that crate, please. It’s... delicate cargo.",
                "Business is rough since the new inspection rules.",
                "You know, a small tip could speed things up?"
            ],
            "Refugee": [
                "I escaped the outer colonies — please, let me through!",
                "My family’s waiting inside the capital.",
                "I lost my papers during the storm!",
                "They said this border was safe... was that a lie?"
            ],
            "Smuggler": [
                "Heh, it’s just medicine. For the children... sure.",
                "No need to search the bag, inspector. Waste of time.",
                "Relax, everyone brings a little something extra.",
                "Come on, we both know how this works — credits talk."
            ],
            "Tourist": [
                "Is this the right line? I’m just visiting!",
                "Wow, the guards here look... friendly?",
                "Oh, my visa expired? That’s awkward.",
                "I promise I’m not hiding anything! Well... maybe souvenirs."
            ],
            "Worker": [
                "Another inspection? I’ll be late for my shift!",
                "Union said this checkpoint was fair. They lied.",
                "It’s freezing out here — can we hurry?",
                "All this for a simple work pass?"
            ]
        }

        # track index for each character
        self.index = {name: 0 for name in self.dialogues}

        # dialogue display setup
        self.font = pygame.font.Font(None, 26)
        self.dialogue_text = ""
        self.current_character = None  # not set yet 

    def get_next_line(self):
        
        if not self.current_character or self.current_character not in self.dialogues:
            return "No character selected."
        name = self.current_character
        lines = self.dialogues[name]
        i = self.index[name]
        line = lines[i]
        self.index[name] = (i + 1) % len(lines)
        return line

    def handle_click(self, pos, mic_rect):
        
        if mic_rect.collidepoint(pos):
            self.dialogue_text = f"{self.current_character}: {self.get_next_line()}"

    def draw(self, screen):
        
        if self.dialogue_text:
            pygame.draw.rect(screen, (0, 0, 0), (0, 570, 800, 70))
            text_surface = self.font.render(self.dialogue_text, True, (255, 255, 255))
            screen.blit(text_surface, (30, 590))