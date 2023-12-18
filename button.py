import pygame

class Button():
    def __init__(self, ai_game, x, y) -> None:

        self.screen = ai_game.screen      
        self.image = pygame.image.load("img/restart.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):

        self.screen.blit(self.image, (self.rect.x-50, self.rect.y))

    