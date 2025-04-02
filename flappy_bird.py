import pygame
import random
import sys
from bird import Bird
from pipe import Pipe
from button import Button
from settings import Settings

class FlappBird():
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""

        pygame.init()

        pygame.display.set_caption("Flappy Bird - By TCM")

        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        #Load Imagem
        self.bg = pygame.image.load("img/bgg.png")
        self.ground = pygame.image.load("img/ground.png")

        #Initialize groups
        self.pipe_group = pygame.sprite.Group()
        self.bird_group = pygame.sprite.Group()

        #Initialize Game variables
        self.game_active = False
        self.score = 0
        self.last_pipe = pygame.time.get_ticks() 
        self.pass_pipe = False

        #Initialize the Bird
        self.bird = Bird(self)
        self.bird_group.add(self.bird)

        #Create Reset Button
        self.reset_button = Button(self) 


    def run_game(self):
        """Start the main loop for the game."""
        
        while True:
            
            self.check_events()                     # Watch for keyboard and mouse events.
            self.screen.blit(self.bg, (0,-150))     # Draw the Background Image (never change)      
            self.bird_group.draw(self.screen)       # Draw the Bird            
            self.pipe_group.draw(self.screen)       # Draw the pipes
            self.screen.blit(self.ground, (self.settings.ground_pos_x,(self.settings.screen_height-70))) # Draw de Floor
            self.draw_points(str(self.score))       # Draw the Points

            if self.game_active:
                self.bird_group.update()    # Make bird move
                self.pipe_group.update()    # Make pipes move
                self.create_new_pipe()
                self.check_for_point()
                self.check_for_collisions()
                self.move_floor()
                
            if not self.game_active:
                self.reset_button.draw()    #Draw the Reset Button

            # Put all draws above in the Screen (Show the changes)
            pygame.display.flip() 

            #Frames per Second(FPS) - Can be change in Settings
            self.clock.tick(self.settings.fps)


    def check_events(self):
        """Respond to keypress and mouse events."""

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:   # When the user click in the X to close window.
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_q) or (event.key == pygame.K_ESCAPE):
                    sys.exit()

                if event.key == pygame.K_SPACE:
                    self.bird.jump() 
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self.check_click_in_Reset(mouse_position)   # Check if the mouse click was in Restart Button
                

    def create_new_pipe(self):
        """Create new pipe after pipe_frequency times (settings)"""

        time_now = pygame.time.get_ticks()
        if time_now - self.last_pipe > self.settings.pipe_frequency:
            
            #choose a random Hight for the pipes
            random_height = random.randint(-130, 130)

            #create the Bottom and Top pipes and add then in pipe_group
            pipe_bottom = Pipe(self, self.settings.screen_width, int(self.settings.screen_height/2) + random_height, -1)
            pipe_top = Pipe(self, self.settings.screen_width, int(self.settings.screen_height/2) + random_height, 1)
            self.pipe_group.add(pipe_bottom)
            self.pipe_group.add(pipe_top)
            self.last_pipe = time_now


    def move_floor(self):
        """Make the floor move to the Left"""

        self.settings.ground_pos_x -= self.settings.game_speed
        if abs(self.settings.ground_pos_x) > 100:
            self.settings.ground_pos_x = 0 # After 100 pixes, the floor go back to position zero


    def check_for_point(self):
        """Check if the bird passed through the pipe and add 1 point"""

        if len(self.pipe_group) > 0:    # It must have at least 1 pipe in the group

            # If the bird is in the middle of one pipe, but don't pass through completely
            if self.bird_group.sprites()[0].rect.left > self.pipe_group.sprites()[0].rect.left\
            and self.bird_group.sprites()[0].rect.right < self.pipe_group.sprites()[0].rect.right\
            and self.pass_pipe == False:
                self.pass_pipe = True
        
            #If the bird passed completely through the pipe 
            if self.pass_pipe == True:
                if self.bird_group.sprites()[0].rect.left > self.pipe_group.sprites()[0].rect.right:
                    self.score += 1
                    self.pass_pipe = False

    
    def check_for_collisions(self):
        """Check for Bird Collisions"""

        #If bird hit the floor, Stop the Game
        if self.bird.rect.bottom > self.settings.screen_height-75:
            self.game_active = False
        
        #if bird hit the pipe, Stop the Game
        if pygame.sprite.groupcollide(self.bird_group, self.pipe_group, False, False):
            self.game_active = False
        

    def draw_points(self, text):
        """Draw the current point in the screen"""

        font = pygame.font.SysFont("Arial", 60)
        img = font.render(text, True, "white")
        x = int(self.settings.screen_width/2)
        y = 20
        self.screen.blit(img, (x,y))


    def check_click_in_Reset(self, mouse_position):
        """Check if the user clicked in the RESET Button"""

        if self.reset_button.rect.collidepoint(mouse_position) and not self.game_active:
            self.pipe_group.empty()     # Restar the pipes - Empty the group
            self.bird.rect.y = int(self.settings.screen_height/2)   # Put the bird in the center of Screen
            self.score = 0              # Reset the Score
            self.game_active = True     # Active the game
            self.bird.jump()            # Make the bird Jump
            


if __name__ == "__main__":
    ai = FlappBird()
    ai.run_game()