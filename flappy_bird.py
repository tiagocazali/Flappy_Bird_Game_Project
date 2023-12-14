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

#Game Variables
ground_pos_x = 0
ground_speed = 4

  

running = True
while running:
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Add de Background Image
    screen.blit(bg, (0,-150))

    # Add and make the floor move
    screen.blit(ground, (ground_pos_x,(screen_height-70)))
    ground_pos_x -= ground_speed # move the floor a little to Letf - NEGATIVA VALUE
    if abs(ground_pos_x) > 100:
        ground_pos_x = 0


    # flip() the display to put your work on screen
    pygame.display.update()

    clock.tick(30)  # limits FPS to 60

pygame.quit()