# standard library dependencies
import os
import random 
from typing import Tuple 

# external dependencies
import pygame

# local dependencies
from assets.game_element import Cloud
from assets.dino_avatar import DinoAvatar
from assets.obstacles import SmallCactus, LargeCactus, Bird

# constants
# NOTE: Remind IM of convention of having constants in uppercase
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

IMAGES_DIRPATH = os.path.join(
    os.getcwd(),
    "assets",
    "images"
)

RUNNING_IMAGES = [
    pygame.image.load(os.path.join(IMAGES_DIRPATH, "Dino", "DinoRun1.png")),
    pygame.image.load(os.path.join(IMAGES_DIRPATH, "Dino", "DinoRun2.png"))
]

JUMPING_IMAGES = [
    pygame.image.load(os.path.join(IMAGES_DIRPATH, "Dino", "DinoJump.png"))
]

DUCKING_IMAGES = [
    pygame.image.load(os.path.join(IMAGES_DIRPATH, "Dino", "DinoDuck1.png")),
    pygame.image.load(os.path.join(IMAGES_DIRPATH, "Dino", "DinoDuck2.png"))
]

SMALL_CACTUS_IMAGES = [
    pygame.image.load(os.path.join(IMAGES_DIRPATH, "Cactus", "SmallCactus1.png")),
    pygame.image.load(os.path.join(IMAGES_DIRPATH, "Cactus", "SmallCactus2.png")),
    pygame.image.load(os.path.join(IMAGES_DIRPATH, "Cactus", "SmallCactus3.png"))
]

LARGE_CACTUS_IMAGES = [
    pygame.image.load(os.path.join(IMAGES_DIRPATH, "Cactus", "LargeCactus1.png")),
    pygame.image.load(os.path.join(IMAGES_DIRPATH, "Cactus", "LargeCactus2.png")),
    pygame.image.load(os.path.join(IMAGES_DIRPATH, "Cactus", "LargeCactus3.png"))
]

BIRD_IMAGES = [
    pygame.image.load(os.path.join(IMAGES_DIRPATH, "Bird", "Bird1.png")),
    pygame.image.load(os.path.join(IMAGES_DIRPATH, "Bird", "Bird2.png"))
]

CLOUD_IMAGE = pygame.image.load(os.path.join(IMAGES_DIRPATH, "Other", "Cloud.png"))

BG_IMAGE = pygame.image.load(os.path.join(IMAGES_DIRPATH, "Other", "Track.png"))


# utility functions

def update_score_and_game_speed(points: int, 
                                game_speed: int) -> Tuple[int,int]:
    """Updates `points` and `game_speed`

    Parameters
    ----------
    points : int
        Current points.
    game_speed : int
        Current game speed.

    Returns
    -------
    Tuple[int,int]
        The updated values for points and game speed.
    """
    points += 1
    if points % 100 == 0:
        game_speed += 1
    # cap game_speed at 40
    return points, min(game_speed, 40)
    
def update_and_draw_score(  points: int, 
                            game_speed: int,
                            screen: pygame.Surface,
                            font : pygame.font.Font) -> Tuple[int,int]:
    """Wrapper around `update_score_and_game_speed` that
    also displays the updated score (`points`) on the screen.

    Parameters
    ----------
    points : int
        Current points.
    game_speed : int
        Current game speed.
    screen : pygame.Surface
        Game screen.
    font : pygame.font.Font
        Font used for the display.

    Returns
    -------
    Tuple[int,int]
        The updated values for points and game speed.
    """
    updated_score, updated_game_speed = update_score_and_game_speed(
        points, 
        game_speed
    )
    text = font.render("Points: " + str(updated_score), True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (1000, 40)
    screen.blit(
        text, 
        textRect
    )
    return updated_score, updated_game_speed

def update_background(  bg_image: pygame.Surface,
                        screen: pygame.Surface,
                        game_speed: int,
                        x_pos_bg: int = 0,
                        y_pos_bg: int = 380) -> int:
    """Convenience function that handles updating
    the background according to the game speed.

    Parameters
    ----------
    bg_image : pygame.Surface
        Image for the background.
    screen : pygame.Surface
        Game screen.
    game_speed : int
        Current value for game speed.
    x_pos_bg : int, optional
        x-position for the background image, by default 0.
    y_pos_bg : int, optional
        y-position for the background image, by default 380.

    Returns
    -------
    int
        The updated x-position for the background image.
    """
    image_width = bg_image.get_width()
    screen.blit(
        bg_image, (x_pos_bg, y_pos_bg)
    )
    screen.blit(
        bg_image, 
        (image_width + x_pos_bg, y_pos_bg)
    )
    # reset background - put it back to its initial position
    if x_pos_bg <= -image_width:
        screen.blit(
            bg_image, 
            (image_width + x_pos_bg, y_pos_bg)
        )
        x_pos_bg = 0
    x_pos_bg -= game_speed
    return x_pos_bg

def main(   game_speed: int = 15, 
            x_pos_bg: int = 0, 
            y_pos_bg: int = 380):
    """Main game loop.

    Parameters
    ----------
    game_speed : int, optional
        Starting value for game speed, by default 15.
    x_pos_bg : int, optional
        Starting value for the x-position of the background image, by default 0.
    y_pos_bg : int, optional
        Starting value for the y-position of the background image, by default 380.
    """
    # useful for setting the time between frames
    clock = pygame.time.Clock()

    # instantiate known assets
    font = pygame.font.Font('freesansbold.ttf', 20)
    
    dino_avatar = DinoAvatar(
        RUNNING_IMAGES,
        DUCKING_IMAGES,
        JUMPING_IMAGES,
        SCREEN_WIDTH
    )

    cloud = Cloud(
        SCREEN_WIDTH,
        image = CLOUD_IMAGE
    )

    score, game_speed = update_and_draw_score(  
        -1, 
        game_speed,
        SCREEN,
        font
    )
    obstacles = []
    run = True 

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # fill with white
        SCREEN.fill((255,255,255))
        cloud.draw(SCREEN)
        cloud.update(game_speed)

        dino_avatar.draw(SCREEN)
        dino_avatar.update(pygame.key.get_pressed())

        if len(obstacles) == 0:
            # NOTE: could also refactor this to use `random.choices`
            random_choice = random.randint(0,2)
            # decide which obstacle to add
            if random_choice == 0:
                obstacles.append(
                    SmallCactus(
                        SCREEN_WIDTH,
                        SMALL_CACTUS_IMAGES[
                            random.randint(0, len(SMALL_CACTUS_IMAGES)-1)
                        ]
                    )
                )
            elif random_choice == 1:
                obstacles.append(
                    LargeCactus(
                        SCREEN_WIDTH,
                        LARGE_CACTUS_IMAGES[
                            random.randint(0, len(LARGE_CACTUS_IMAGES)-1)
                        ]
                    )
                )
            else:
                obstacles.append(
                    Bird(
                        SCREEN_WIDTH,
                        BIRD_IMAGES
                    )
                )
            
        
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(game_speed)

            # if the obstacle image is completely off-screen, 
            # pop it
            if obstacle.rect.x < -obstacle.rect.width:
                obstacles.pop()
                break

            if dino_avatar.collides_with(obstacle.rect):
                pygame.time.delay(2000)
                menu(
                    SCREEN,
                    score = score
                )
        
        x_pos_bg = update_background(
            BG_IMAGE,
            SCREEN,
            game_speed,
            x_pos_bg = x_pos_bg,
            y_pos_bg = y_pos_bg
        )

        score, game_speed = update_and_draw_score(  
            score, 
            game_speed,
            SCREEN,
            font
        )

        clock.tick(30)
        pygame.display.update()

def menu(   screen: pygame.Surface,
            score: int = -1):
    run = True
    font = pygame.font.Font('freesansbold.ttf', 30)

    while run:
        screen.fill((255,255,255))
        if score == -1:
            text = font.render(
                "Press SPACE to start!",
                True,
                (0,0,0)
            )
            text_rect = text.get_rect()
            text_rect.center = (
                SCREEN_WIDTH // 2, 
                SCREEN_HEIGHT // 2
            )
            screen.blit(text, text_rect)
        else:
            text = font.render(
                "Press SPACE to start over!",
                True, 
                (0,0,0)
            )
            text_rect = text.get_rect()
            text_rect.center = (
                SCREEN_WIDTH // 2, 
                SCREEN_HEIGHT // 2
            )
            screen.blit(
                text, text_rect
            )
            text = font.render(
                f"Your score: {score}",
                True,
                (0,0,0)
            )
            text_rect = text.get_rect()
            text_rect.center = (
                SCREEN_WIDTH // 2, 
                SCREEN_HEIGHT // 2 + 50
            )
            screen.blit(text, text_rect)
        screen.blit(
            RUNNING_IMAGES[0],
            (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140)
        )
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                raise SystemExit

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                main()

if __name__ == '__main__':
    pygame.init()
    menu(SCREEN)