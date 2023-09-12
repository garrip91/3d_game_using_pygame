import pygame
import settings
from player import Player


pygame.init()
sc = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
clock = pygame.time.Clock()
player = Player()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(settings.BLACK)

    pygame.draw.circle(sc, settings.GREEN, settings.PLAYER_POS, 12)

    pygame.display.flip()
    clock.tick()
