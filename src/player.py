""" import settings
import pygame
import math

class Player:
    def __init__(self):
        self.x, self.y = settings.PLAYER_POS
        self.angle = settings.PLAYER_ANGLE

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
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
            self.angle += 0.02 """


import settings
import pygame
import math

class Player:
    def __init__(self):
        self.x, self.y = settings.PLAYER_POS
        self.angle = settings.PLAYER_ANGLE

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
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
