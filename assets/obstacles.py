# obstacles.py
from typing import List 

# external dependencies
import pygame

# local dependencies
from .game_element import GameElement

class SmallCactus(GameElement):
    def __init__(   self, 
                    screen_width: int, 
                    image: pygame.Surface):
        super().__init__(
            image,
            screen_width
        )
        self.rect.y = 325

class LargeCactus(GameElement):
    def __init__(   self, 
                    screen_width: int, 
                    image: pygame.Surface):
        super().__init__(
            image,
            screen_width
        )
        self.rect.y = 300

class Bird(GameElement):
    def __init__(   self, 
                    screen_width: int, 
                    images: List[pygame.Surface],
                    debug: bool = False):
        super().__init__(
            images[0],
            screen_width
        )
        self.images = images
        self.rect.y = 250
        self.image_index = 0
        self.debug = debug

    def draw(self, screen: pygame.Surface):
        self.image_index = (self.image_index + 1)
        self.image = self.images[(self.image_index // 5) % len(self.images)]
        screen.blit(
            self.image, 
            self.rect
        )
        if self.debug:    
            collision_box = pygame.Rect(
                self.rect.x, 
                self.rect.y, 
                self.rect.width, 
                self.rect.height
            )
            pygame.draw.rect(
                screen,
                (0,0,0),
                collision_box,
                1
            )
