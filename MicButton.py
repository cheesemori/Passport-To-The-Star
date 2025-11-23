import pygame

class MicButton:
    def __init__(self, path, pos):
        self.raw_image = pygame.image.load(path).convert_alpha()

        # make the mic BIGGER — adjust size here
        self.image = pygame.transform.scale(self.raw_image, (55, 90))

        self.rect = self.image.get_rect()
        self.rect.topleft = pos  # bottom-left position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)