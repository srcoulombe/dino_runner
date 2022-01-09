# dino_avatar.py

# standard library dependencies
from typing import List 

# external dependencies
import pygame

# local dependencies
from .game_element import GameElement

class DinoAvatar(GameElement):
    def __init__(   self, 
                    running_images: List[pygame.Surface],
                    ducking_images: List[pygame.Surface],
                    jumping_images: List[pygame.Surface],
                    screen_width: int,
                    debug_mode: bool = False):
        super().__init__(
            running_images[0], 
            screen_width
        )

        self.debug_mode = debug_mode 

        self.rect.x = 80
        self.rect.y = 310
        self.x_position = 80
        self.y_position = 310
        self.y_position_when_ducking = 340
        self.jump_velocity = 8.5

        self.running_images = running_images
        self.ducking_images = ducking_images
        self.jumping_images = jumping_images

        self.is_running = True
        self.is_ducking = False 
        self.is_jumping = False
        self.can_jump = False

        self.step_index = 0

        self.front_point = [self.rect.x + 45, self.rect.y + 5]
        self.front_point_when_crouching = (self.rect.x + 105, self.rect.y + 40)
        self.bottom_point = [self.rect.x + 10, self.rect.y + 70]
        self.tail_point = [self.rect.x, self.rect.y + 50]

    def update_step_index(self) -> int:
        self.step_index = self.step_index + 1
        return self.step_index

    def draw(self, screen: pygame.Surface):
        screen.blit(
            self.image, 
            (self.rect.x, self.rect.y)
        )
        if self.debug_mode:
            colors = (
                (0,0,255), # blue = front
                (255,0,0), # red = when crouching
                (0,255,0), # green = bottom
                (0,0,0) # black = tail
            )
            points = (self.front_point, self.front_point_when_crouching, self.bottom_point, self.tail_point)
            for point, color in zip(points, colors):
                pygame.draw.circle(screen, color, point, 10)

    def duck(self):
        self.image = self.ducking_images[(self.update_step_index() // 5) % len(self.ducking_images)]
        self.rect = self.image.get_rect()
        self.rect.x = self.x_position
        self.rect.y = self.y_position_when_ducking
        self.front_point_when_crouching = (self.rect.x + 105, 310 + 40)
        self.is_ducking = True

    def run(self):
        self.image = self.running_images[(self.update_step_index() // 5) % len(self.running_images)]
        self.rect = self.image.get_rect()
        self.rect.x = self.x_position
        self.rect.y = self.y_position
        self.front_point = [self.rect.x + 45, self.rect.y + 5]
        self.is_running = True
    
    def jump(self):
        self.image = self.jumping_images[(self.update_step_index() // 5) % len(self.jumping_images)]
        if self.is_jumping:
            self.can_jump = False
            self.rect.y -= self.jump_velocity * 4
            self.front_point[1] -= self.jump_velocity * 4
            self.bottom_point[1] -= self.jump_velocity * 4
            self.tail_point[1] -= self.jump_velocity * 4
            self.jump_velocity -= 0.8
        if self.jump_velocity < -8.5:
            self.can_jump = True 
            self.is_jumping = False
            self.jump_velocity = 8.5
            self.rect.y = 310
            self.front_point[1] = self.rect.y + 5
            self.bottom_point[1] = self.rect.y + 70
            self.tail_point[1] = self.rect.y + 50
        
    def update(self, userInput):
        if self.is_ducking:
            self.duck()
        if self.is_running:
            self.run()
        if self.is_jumping:
            self.jump()

        if userInput[pygame.K_UP] and not self.is_jumping:
            self.is_ducking = False
            self.is_running = False
            self.is_jumping = True
            self.jump()
        elif userInput[pygame.K_DOWN] and not self.is_jumping:
            self.is_ducking = True 
            self.is_running = False
            self.is_jumping = False 
            self.duck()

        elif not (self.is_jumping or userInput[pygame.K_DOWN]):
            self.is_ducking = False
            self.is_running = True
            self.is_jumping = False

    def collides_with(self, rect: pygame.Rect) -> bool:
        if self.is_ducking:
            is_colliding = rect.collidepoint(self.bottom_point) \
                or rect.collidepoint(self.front_point_when_crouching)
            if is_colliding:
                print("A")
                print(self.front_point_when_crouching)
                print(self.front_point)
                print(dir(rect))
            return is_colliding
        elif self.is_jumping:
            is_colliding = rect.collidepoint(self.bottom_point) \
                or rect.collidepoint(self.front_point) \
                or rect.collidepoint(self.tail_point)
            if is_colliding:
                print("B")
            return is_colliding
        else:
            is_colliding = rect.collidepoint(self.front_point)
            if is_colliding:
                print("C")
            return is_colliding

