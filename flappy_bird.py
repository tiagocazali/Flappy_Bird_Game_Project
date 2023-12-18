from typing import Any
import pygame
import random

# pygame setup
pygame.init()

screen_width = 600 
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()



#Load Imagem
bg = pygame.image.load("img/bgg.png")
ground = pygame.image.load("img/ground.png")
button_restart_img = pygame.image.load("img/restart.png")

#Game Variables
ground_pos_x = 0
game_speed = 4
game_active = False
pipe_espace = 75
pipe_frequency = 1500 #milliseconds
last_pipe = pygame.time.get_ticks()
score = 0
pass_pipe = False



def draw_text(text, x, y):
    font = pygame.font.SysFont("Arial", 60)
    font_color = (255,255,255) #White
    img = font.render(text, True, font_color)
    screen.blit(img, (x,y))

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




class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
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
    
    def update(self):
        
        #add Gravity - Move the bird Down
        self.gravity += 0.5
        if self.gravity > 8:
            self.gravity = 8
       
        if self.rect.bottom <= screen_height-75:
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

 
     

pipe_group = pygame.sprite.Group()
bird_group = pygame.sprite.Group()

bird = Bird(100, int(screen_height/2))
bird_group.add(bird)

reset_button = Button(screen_width/2, screen_height/2, button_restart_img) 

running = True
while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_q) or (event.key == pygame.K_ESCAPE):
                running = False
            if event.key == pygame.K_SPACE:
                bird.gravity = -10 #Make the bird Jump
                
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if game_active == False:
                game_active, score = reset_button.check_click_in_Reset(mouse_position)
                bird.gravity = -10 #Make the bird Jump
                

    # Add de Background Image
    screen.blit(bg, (0,-150))
    
    #add the Bird
    bird_group.draw(screen)
    
    #add pipes
    pipe_group.draw(screen)
    
    #add Floor
    screen.blit(ground, (ground_pos_x,(screen_height-70)))

    draw_text(str(score), int(screen_width/2), 20)


    if game_active: 

        #make bird move
        bird_group.update()
        pipe_group.update() #make pipes move

        if pygame.sprite.groupcollide(bird_group, pipe_group, False, False):
            game_active = False
            

        #Create new pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            random_height = random.randint(-130, 130)
            pipe_bottom = Pipe(screen_width, int(screen_height/2)+random_height, -1)
            pipe_top = Pipe(screen_width, int(screen_height/2)+random_height, 1)
            pipe_group.add(pipe_bottom)
            pipe_group.add(pipe_top)
            last_pipe = time_now
       
        if len(pipe_group) >0:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
            and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
            and pass_pipe == False:
                pass_pipe = True
        
            if pass_pipe == True:
                if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                    score += 1
                    pass_pipe = False

        #If bird hit the floor, Stop the Game
        if bird.rect.bottom > screen_height-75:
            game_active = False


        #make the floor move
        ground_pos_x -= game_speed # move the floor a little to Letf - NEGATIVA VALUE
        if abs(ground_pos_x) > 100:
            ground_pos_x = 0

    if game_active == False:
        reset_button.draw()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()