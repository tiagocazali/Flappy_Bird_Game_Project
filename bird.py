import pygame
from pygame.sprite import Sprite

class Bird(Sprite):

    def __init__(self, ai_game, x, y):

        super().__init__() #Initialize the Sprite
        self.settings = ai_game.settings
        self.screen = ai_game.screen

        self.images = [
            pygame.image.load("img/bird1.png"),
            pygame.image.load("img/bird2.png"),
            pygame.image.load("img/bird3.png")
        ]
        
        self.index = 0
        self.counter = 0 #used to Count the frames before change the image
        self.image = self.images[self.index]
        
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.gravity = 0
    
    def jump(self):
        self.gravity = -10 #Make the bird Jump
    
    def update(self):
        
        #add Gravity - Move the bird Down
        self.gravity += 0.5
        if self.gravity > 8:
            self.gravity = 8
       
        if self.rect.bottom <= self.settings.screen_height-75:
            self.rect.y += int(self.gravity) 

        #ANIMATION
        self.counter += 1 

        if self.counter > 10: #Only after 10 frames that the image will change
            self.index += 1
            self.counter =0
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

        #rotate the image
        self.image = pygame.transform.rotate(self.image, self.gravity*-3) 