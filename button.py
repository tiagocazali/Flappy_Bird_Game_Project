import pygame

class Button():
    def __init__(self, x, y, image) -> None:
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):

        screen.blit(self.image, (self.rect.x-50, self.rect.y))

    def check_click_in_Reset(self, mouse_position):
        if self.rect.collidepoint(mouse_position):
            pipe_group.empty()
            bird.rect.x = 100
            bird.rect.y = int(screen_height/2)
            return (True, 0)