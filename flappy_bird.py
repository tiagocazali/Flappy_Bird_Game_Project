import pygame
import random
import sys
from bird import Bird
from pipe import Pipe
from button import Button
from settings import Settings

class FlappBird():

    def __init__(self):
        
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Flappy Bird - By TCM")

        #Load Imagem
        self.bg = pygame.image.load("img/bgg.png")
        self.ground = pygame.image.load("img/ground.png")

        self.pipe_group = pygame.sprite.Group()
        self.bird_group = pygame.sprite.Group()

        self.game_active = False
        self.score = 0

        self.bird = Bird(self, 100, int(self.settings.screen_height/2))
        self.bird_group.add(self.bird)

        self.last_pipe = pygame.time.get_ticks() 
        self.pass_pipe = False

        self.reset_button = Button(self, self.settings.screen_width/2, self.settings.screen_height/2) 


    
    def run_game(self):

        running = True
        while running:
            
            self.check_events()
            self.screen.blit(self.bg, (0,-150))  # Add de Background Image      
            self.bird_group.draw(self.screen)  #add the Bird            
            self.pipe_group.draw(self.screen) #add pipes
            self.screen.blit(self.ground, (self.settings.ground_pos_x,(self.settings.screen_height-70)))
            self.draw_text(str(self.score), int(self.settings.screen_width/2), 20)

            if self.game_active:
                self.bird_group.update() #make bird move
                self.pipe_group.update() #make pipes move
                self.create_new_pipe()
                self.check_for_point()
                self.check_for_colision()
                self.move_floor()
                

            if self.game_active == False:
                self.reset_button.draw()

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()

    def check_events(self):
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_q) or (event.key == pygame.K_ESCAPE):
                    running = True
                    sys.exit()

                if event.key == pygame.K_SPACE:
                    self.bird.gravity = -10 #Make the bird Jump
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if self.game_active == False:
                   self.game_active, self.score = self.check_click_in_Reset(mouse_position)
                   self.bird.gravity = -10 #Make the bird Jump

    def create_new_pipe(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.last_pipe > self.settings.pipe_frequency:
            random_height = random.randint(-130, 130)
            pipe_bottom = Pipe(self, self.settings.screen_width, int(self.settings.screen_height/2)+random_height, -1)
            pipe_top = Pipe(self, self.settings.screen_width, int(self.settings.screen_height/2)+random_height, 1)
            self.pipe_group.add(pipe_bottom)
            self.pipe_group.add(pipe_top)
            self.last_pipe = time_now

    def move_floor(self):
        self.settings.ground_pos_x -= self.settings.game_speed # move the floor a little to Letf - NEGATIVA VALUE
        if abs(self.settings.ground_pos_x) > 100:
            self.settings.ground_pos_x = 0

    def check_for_point(self):
        if len(self.pipe_group) >0:
            if self.bird_group.sprites()[0].rect.left > self.pipe_group.sprites()[0].rect.left\
            and self.bird_group.sprites()[0].rect.right < self.pipe_group.sprites()[0].rect.right\
            and self.pass_pipe == False:
                self.pass_pipe = True
        
            if self.pass_pipe == True:
                if self.bird_group.sprites()[0].rect.left > self.pipe_group.sprites()[0].rect.right:
                    self.score += 1
                    self.pass_pipe = False

    def check_for_colision(self):
        #If bird hit the floor, Stop the Game
        if self.bird.rect.bottom > self.settings.screen_height-75:
            self.game_active = False
        
        if pygame.sprite.groupcollide(self.bird_group, self.pipe_group, False, False):
            self.game_active = False
        
    def draw_text(self, text, x, y):
        font = pygame.font.SysFont("Arial", 60)
        font_color = (255,255,255) #White
        img = font.render(text, True, font_color)
        self.screen.blit(img, (x,y))

    def check_click_in_Reset(self, mouse_position):
        if self.reset_button.rect.collidepoint(mouse_position):
            self.pipe_group.empty()
            self.bird.rect.x = 100
            self.bird.rect.y = int(self.settings.screen_height/2)
            return (True, 0)
        return(False, 0)

if __name__ == "__main__":
    ai = FlappBird()
    ai.run_game()
