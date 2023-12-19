import pygame

class Pipe(pygame.sprite.Sprite):
    """A class to manage the Pipes."""

    def __init__(self, ai_game, x, y, position):
        """Initialize the pipe and set it starting position - Top(1) or Bottom(-1) """
        
        pygame.sprite.Sprite.__init__(self)  #Initialize the Sprite

        # Use the settings that was imported in Main Game (flappy_bird)
        self.settings = ai_game.settings

        # Load the Pipe Image and gey the rect
        self.image = pygame.image.load("img/pipe.png")
        self.rect = self.image.get_rect()

        # The "opening distance" (pipe_espace) between the pipes, can be change in the Settings
        if position == 1:   # Top Pipe
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y-self.settings.pipe_espace]

        if position == -1:  # Bottom pipe 
            self.rect.topleft = [x, y+self.settings.pipe_espace]

    def update(self):
        """Make the pipe move to the Left and remove old ones."""
        
        self.rect.x -= self.settings.game_speed
        
        # Remove pipe that is out of screen
        if self.rect.right < 0:
            self.kill()