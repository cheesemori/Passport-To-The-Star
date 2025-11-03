class DialogueManager:
    def __init__(self):
        # character dialogues (i can change these if you guys dont like them!)
        self.dialogues = {
            "DrZog": [
    "Dr Zog: Oh dear... they said the experiment was illegal!",
    "Border Staff: Illegal? You’d better explain that, doctor.",
    "Dr Zog: You don't understand, my work can save lives!",
    "Border Staff: Then why keep it secret? Sounds suspicious.",
    "Dr Zog: Please, don’t report me — I just need more time.",
    "Border Staff: Time isn’t something we hand out easily here.",
    "Dr Zog: My research could heal worlds, not destroy them!",
    "Border Staff: Every criminal says they’re saving the world.",
    "Dr Zog: You have to trust me, inspector... for everyone’s sake.",
    "Border Staff: Trust is earned, not requested at the border."
],

"Kraen": [
    "Kraen: The Memory Stone must be protected.",
    "Border Staff: Protected from who? You look nervous.",
    "Kraen: Truth fades when no one remembers.",
    "Border Staff: That sounds poetic... or dangerous.",
    "Kraen: My people were erased once. Never again.",
    "Border Staff: Then you understand why we check everyone.",
    "Kraen: Let me pass. History is more fragile than flesh.",
    "Border Staff: History doesn’t excuse forged documents.",
    "Kraen: If I fail, no one will know we ever existed.",
    "Border Staff: Then make sure your story is worth remembering."
],

"CaptainRhen": [
    "Captain Rhen: Papers, please. Regulations are clear.",
    "Border Staff: You sound just like me, Captain.",
    "Captain Rhen: Do you question my duty, citizen?",
    "Border Staff: Not your duty — your heart.",
    "Captain Rhen: Every day feels the same... inspect, approve, deny.",
    "Border Staff: That’s the price of order — repetition.",
    "Captain Rhen: Sometimes, I wonder if I’m the villain here.",
    "Border Staff: Only those with a conscience ever ask that.",
    "Captain Rhen: The rules keep us safe — or so they say.",
    "Border Staff: Safety’s just another word for control, isn’t it?"
],
         
           "Merchant": [
    "Merchant: I have travel permits right here — totally valid!",
    "Border Staff: Relax, I’ll be the judge of that.",
    "Merchant: Don’t open that crate, please. It’s... delicate cargo.",
    "Border Staff: Delicate or illegal, which is it?",
    "Merchant: Business is rough since the new inspection rules.",
    "Border Staff: Then follow them, and you’ll have nothing to worry about.",
    "Merchant: You know, a small tip could speed things up?",
    "Border Staff: Try that again and you’ll lose more than time."
],

"Refugee": [
    "Refugee: I escaped the outer colonies — please, let me through!",
    "Border Staff: Easy there. Start with your identification.",
    "Refugee: My family’s waiting inside the capital.",
    "Border Staff: Everyone says that. Where’s your proof?",
    "Refugee: I lost my papers during the storm!",
    "Border Staff: Then you’ll have to wait until we can verify you.",
    "Refugee: They said this border was safe... was that a lie?",
    "Border Staff: Safety depends on cooperation — yours included."
],

"Smuggler": [
    "Smuggler: Heh, it’s just medicine. For the children... sure.",
    "Border Staff: Medicine doesn’t usually come with hidden compartments.",
    "Smuggler: No need to search the bag, inspector. Waste of time.",
    "Border Staff: Then you won’t mind if I check it anyway.",
    "Smuggler: Relax, everyone brings a little something extra.",
    "Border Staff: Extra is fine — contraband isn’t.",
    "Smuggler: Come on, we both know how this works — credits talk.",
    "Border Staff: Not today they don’t."
],

"Tourist": [
    "Tourist: Is this the right line? I’m just visiting!",
    "Border Staff: You’re in the right place — now show your passport.",
    "Tourist: Wow, the guards here look... friendly?",
    "Border Staff: Flattery won’t make the line shorter.",
    "Tourist: Oh, my visa expired? That’s awkward.",
    "Border Staff: Awkward and illegal. Why are you still here?",
    "Tourist: I promise I’m not hiding anything! Well... maybe souvenirs.",
    "Border Staff: We’ll be the ones to decide what’s a souvenir."
],

"Worker": [
    "Worker: Another inspection? I’ll be late for my shift!",
    "Border Staff: Then you should’ve arrived earlier.",
    "Worker: Union said this checkpoint was fair. They lied.",
    "Border Staff: You can file a complaint once you’re cleared.",
    "Worker: It’s freezing out here — can we hurry?",
    "Border Staff: Cold doesn’t change procedure.",
    "Worker: All this for a simple work pass?",
    "Border Staff: The simple ones cause the biggest problems."
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
