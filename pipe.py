import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("img/pipe.png")
        self.rect = self.image.get_rect()

        #If position is 1 = TOP Pipe, -1 is bottom pipe
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y-pipe_espace]
        if position == -1:    
            self.rect.topleft = [x, y+pipe_espace]

    def update(self):
        #Move de pipe to Left
        self.rect.x -= game_speed
        
        #remove pipe that is out of screen
        if self.rect.right < 0:
            self.kill()