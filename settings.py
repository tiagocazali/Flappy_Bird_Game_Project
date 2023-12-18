import pygame

class Settings:
    
    def __init__(self) -> None:
        
        self.screen_width = 500
        self.screen_height = 600

        #Game Variables
        self.ground_pos_x = 0
        self.game_speed = 4
        
        self.pipe_espace = 75
        self.pipe_frequency = 1500 #milliseconds
        self.last_pipe = pygame.time.get_ticks()
        self.score = 0
        self.pass_pipe = False
