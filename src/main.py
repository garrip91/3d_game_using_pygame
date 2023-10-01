import pygame
import settings
from player import Player
import math
from map import world_map
from drawing import Drawing


pygame.init()
sc = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
sc_map = pygame.Surface((settings.WIDTH // settings.MAP_SCALE, settings.HEIGHT // settings.MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(settings.BLACK)

    drawing.background(player.angle)
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)
    drawing.mini_map(player)

    pygame.display.flip()
    clock.tick()
