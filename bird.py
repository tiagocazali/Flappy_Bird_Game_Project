import pygame
from pygame.sprite import Sprite

class Bird(Sprite):
    """A class to manage the Bird."""

    def __init__(self, ai_game):
        """ Initialize the Bird and set it starting position"""

        super().__init__() # Initialize the Sprite
        self.settings = ai_game.settings
        self.screen = ai_game.screen

        self.images_collection = [
            pygame.image.load("img/bird1.png"),
            pygame.image.load("img/bird2.png"),
            pygame.image.load("img/bird3.png")
        ]
        
        self.index = 0
        self.counter = 0    # Used to Count the frames before change the image
        self.gravity = 0
        
        self.image = self.images_collection[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 70
        self.rect.y = self.settings.screen_height/2 # Start in the center of the Screen
    

    def jump(self):
        """Make the bird Jump (move UP) by increasing the Gravity"""

        self.gravity = -10 
    

    def update(self):
        """Make the Bird move Down and give animation"""

        self.gravity += 0.5     #add Gravity - Move the bird Down
        if self.gravity > 8:
            self.gravity = 8
       
        self.rect.y += int(self.gravity)    # Move the bird Y position  

        #ANIMATION
        self.counter += 1 

        # Only after 10 frames the image will change
        if self.counter > 10: 
            self.index += 1
            self.counter = 0

        # After use all the images, start again from the first    
        if self.index >= len(self.images_collection):
            self.index = 0

        self.image = self.images_collection[self.index]

        # Rotate the image
        self.image = pygame.transform.rotate(self.image, self.gravity*-3) 