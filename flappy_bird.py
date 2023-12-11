import pygame
import random
from bird import Bird

screen_width = 500
screen_height = 800

pipe_img = pygame.image.load("img/pipe.png")
floor_img = pygame.image.load("img/base.png")
bg_img = pygame.image.load("img/bg")


pygame.font.init()
score_font = pygame.font.SysFont("Arial", 50)