import pygame
import settings
from player import Player
import math
from map import world_map
from ray_casting import ray_casting


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

    pygame.draw.rect(sc, settings.BLUE, (0, 0, settings.WIDTH, settings.HALF_HEIGHT))
    pygame.draw.rect(sc, settings.DARKGRAY, (0, settings.HALF_HEIGHT, settings.WIDTH, settings.HALF_HEIGHT))

    ray_casting(sc, player.pos, player.angle)

    # pygame.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)
    # pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
    #                                          player.y + WIDTH * math. sin(player.angle)), 2)
    # for x,y in world_map:
    #     pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE), 2)

    pygame.display.flip()
    clock.tick(settings.FPS)
    # print(clock.get_fps())
