class Settings:
    """A class to store all settings for Flappy Bird."""
    
    def __init__(self) -> None:
        
        # Screen Size
        self.screen_width = 500
        self.screen_height = 600

        # Floor Position
        self.ground_pos_x = 0
        
        # Pipe Variables
        self.game_speed = 4         # Speed that pipes move
        self.pipe_espace = 75       # Space beteween the Pipes
        self.pipe_frequency = 1300  # Milliseconds - Time beteween the Pipes

        self.fps = 60

        
