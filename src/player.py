import settings
import pygame
import math


class Player:
    
    def __init__(self):
        self.x, self.y = settings.PLAYER_POS
        self.angle = settings.PLAYER_ANGLE
        self.sensitivity = 0.004

    @property
    def pos(self):
        return (self.x, self.y)
    
    def movement(self):
        self.keys_control()
        self.mouse_control()
        self.angle %= settings.DOUBLE_PI

    def keys_control(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()
        
        if keys[pygame.K_w]:
            self.x += settings.PLAYER_SPEED * cos_a
            self.y += settings.PLAYER_SPEED * sin_a
        if keys[pygame.K_s]:
            self.x += -settings.PLAYER_SPEED * cos_a
            self.y += -settings.PLAYER_SPEED * sin_a
        if keys[pygame.K_a]:
            self.x += settings.PLAYER_SPEED * sin_a
            self.y += -settings.PLAYER_SPEED * cos_a
        if keys[pygame.K_d]:
            self.x += -settings.PLAYER_SPEED * sin_a
            self.y += settings.PLAYER_SPEED * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
    
    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - settings.HALF_WIDTH
            pygame.mouse.set_pos((settings.HALF_WIDTH, settings.HALF_HEIGHT))
            self.angle += difference * self.sensitivity
