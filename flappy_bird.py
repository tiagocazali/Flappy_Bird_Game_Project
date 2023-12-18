import pygame
import random
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

        self.bird = Bird(self, 100, int(self.settings.screen_height/2))
        self.bird_group.add(self.bird)

        self.reset_button = Button(self, self.settings.screen_width/2, self.settings.screen_height/2) 


    
    def run_game(self):

        running = True
        while running:
        
            self.check_events()
                        

            # Add de Background Image
            self.screen.blit(self.bg, (0,-150))
            
            #add the Bird
            self.bird_group.draw(self.screen)
            
            #add pipes
            self.pipe_group.draw(self.screen)
            
            #add Floor
            self.screen.blit(self.ground, (self.settings.ground_pos_x,(self.settings.screen_height-70)))

            #self.draw_text(str(score), int(self.settings.screen_width/2), 20)


            if self.game_active: 

                #make bird move
                self.bird_group.update()
                self.pipe_group.update() #make pipes move

                if pygame.sprite.groupcollide(self.bird_group, self.pipe_group, False, False):
                    self.game_active = False
                    

                #Create new pipes
                time_now = pygame.time.get_ticks()
                if time_now - last_pipe > self.settings.pipe_frequency:
                    random_height = random.randint(-130, 130)
                    pipe_bottom = Pipe(self.settings.screen_width, int(self.settings.screen_height/2)+random_height, -1)
                    pipe_top = Pipe(self.settings.screen_width, int(self.settings.screen_height/2)+random_height, 1)
                    self.pipe_group.add(pipe_bottom)
                    self.pipe_group.add(pipe_top)
                    last_pipe = time_now
            
                if len(self.pipe_group) >0:
                    if self.bird_group.sprites()[0].rect.left > self.pipe_group.sprites()[0].rect.left\
                    and self.bird_group.sprites()[0].rect.right < self.pipe_group.sprites()[0].rect.right\
                    and pass_pipe == False:
                        pass_pipe = True
                
                    if pass_pipe == True:
                        if self.bird_group.sprites()[0].rect.left > self.pipe_group.sprites()[0].rect.right:
                            score += 1
                            pass_pipe = False

                #If bird hit the floor, Stop the Game
                if self.bird.rect.bottom > self.settings.screen_height-75:
                    game_active = False


                #make the floor move
                ground_pos_x -= self.settings.game_speed # move the floor a little to Letf - NEGATIVA VALUE
                if abs(ground_pos_x) > 100:
                    ground_pos_x = 0

            if self.game_active == False:
                pass
                #self.reset_button.draw()

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()

    def check_events(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_q) or (event.key == pygame.K_ESCAPE):
                    running = False
                if event.key == pygame.K_SPACE:
                    self.bird.gravity = -10 #Make the bird Jump
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if game_active == False:
                    game_active, score = self.reset_button.check_click_in_Reset(mouse_position)
                    self.bird.gravity = -10 #Make the bird Jump


    def draw_text(self, text, x, y):
        font = pygame.font.SysFont("Arial", 60)
        font_color = (255,255,255) #White
        img = font.render(text, True, font_color)
        self.screen.blit(img, (x,y))

    def check_click_in_Reset(self, mouse_position):
        if self.rect.collidepoint(mouse_position):
            pipe_group.empty()
            bird.rect.x = 100
            bird.rect.y = int(screen_height/2)
            return (True, 0)

if __name__ == "__main__":
    ai = FlappBird()
    ai.run_game()
