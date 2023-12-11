import pygame

class Bird:

    bird_images = [
        pygame.image.load("img/bird1.png"),
        pygame.image.load("img/bird2.png"),
        pygame.image.load("img/bird3.png"),
    ]
    
    max_rotation = 25
    rotation_speed = 20
    animation_time = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 90
        self.speed = 0
        self.height = self.y
        self.time = 0
        self.img_count = 0
        self.image = self.bird_images[0]







