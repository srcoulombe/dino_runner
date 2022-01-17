# standard library dependencies
import os 
import random

# external dependencies
import pygame

class GameElement:
    """Parent class for obstacles (cactus classes, bird class)
    and extra game elements (cloud)
    """
    def __init__(   self, 
                    image: pygame.Surface, 
                    screen_width: int):
        self.image = image
        self.screen_width = screen_width
        self.rect = self.image.get_rect()
        self.rect.x = screen_width

    def update(self, game_speed: int):
        self.rect.x -= game_speed

    def draw(self, screen: pygame.Surface):
        screen.blit(
            self.image, 
            self.rect
        )

    def update_and_draw(self,
                        game_speed: int,
                        screen: pygame.Surface):
        self.update(game_speed)
        self.draw(screen)

class Cloud(GameElement):
    def __init__(   self, 
                    screen_width: int,
                    image: pygame.Surface = None):
        if image is None:
            image = pygame.image.load(
                os.path.join(
                    os.getcwd(),
                    "images",
                    "Other", 
                    "Cloud.png"
                )
            )
        # NOTE: remind them what this `super()` does and
        # what `super().__init__` triggers
        super().__init__(
            image, 
            screen_width
        )
        self.x = screen_width + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.width = self.image.get_width()

    def update(self, game_speed: int):
        """Updates the position of the cloud, 
        and respawns it if it is 100% off-screen.

        Parameters
        ----------
        game_speed : int
            Current game speed.
        """
        self.x -= game_speed
        if self.x < -self.width:
            self.respawn()

    def respawn(self):
        """Resets the cloud's x- and y-positions.
        """
        self.x = self.screen_width + random.randint(2500, 3000)
        self.y = random.randint(50, 100)

    def draw(self, screen: pygame.Surface):
        """Draws the cloud on the screen

        Parameters
        ----------
        screen : pygame.Surface
            Game screen.
        """
        screen.blit(
            self.image, 
            (self.x, self.y)
        )