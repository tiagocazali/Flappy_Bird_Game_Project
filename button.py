import pygame

class Button():
    """A class to manage the Reset Button."""

    def __init__(self, ai_game) -> None:

        self.screen = ai_game.screen
        self.settings = ai_game.settings   
           
        self.image = pygame.image.load("img/restart.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.settings.screen_width/2
        self.rect.y = self.settings.screen_height/2

    def draw(self):
        """Draw the Button RESET"""

        self.screen.blit(self.image, (self.rect.x-50, self.rect.y))

    