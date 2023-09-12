import pygame
import settings


class Player:

    def __init__(self):
        self.x, self.y = settings.PLAYER_POS
        self.angle = settings.PLAYER_ANGLE
    
    @property
    def pos(self):
        return (self.x, self.y)
    
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= settings.PLAYER_SPEED
        if keys[pygame.K_s]:
            self.y += settings.PLAYER_SPEED
        if keys[pygame.K_a]:
            self.x -= settings.PLAYER_SPEED
        if keys[pygame.K_d]:
            self.x += settings.PLAYER_SPEED
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
