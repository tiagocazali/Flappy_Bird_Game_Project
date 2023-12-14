from typing import Any
import pygame
import random

#from pygame.sprite import Group

# pygame setup
pygame.init()

screen_width = 600 
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


#Load Imagem
bg = pygame.image.load("img/bgg.png")
ground = pygame.image.load("img/ground.png")

#Game Variables
ground_pos_x = 0
ground_speed = 4


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
       
        if self.rect.bottom <= screen_height-80:
            self.rect.y += int(self.gravity) 

        #Jump = Press Space
        

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


bird_group = pygame.sprite.Group()

bird = Bird(100, int(screen_height/2))

bird_group.add(bird)
  

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

    # Add de Background Image
    screen.blit(bg, (0,-150))

    #add the Bird
    bird_group.draw(screen)
    bird_group.update()

    # Add and make the floor move
    screen.blit(ground, (ground_pos_x,(screen_height-70)))
    ground_pos_x -= ground_speed # move the floor a little to Letf - NEGATIVA VALUE
    if abs(ground_pos_x) > 100:
        ground_pos_x = 0


    # flip() the display to put your work on screen
    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()