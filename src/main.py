import pygame
import settings
from player import Player
import sprite_objects
from ray_casting import ray_casting
from drawing import Drawing


pygame.init()
sc = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
sc_map = pygame.Surface((settings.WIDTH // settings.MAP_SCALE, settings.HEIGHT // settings.MAP_SCALE))

sprites = sprite_objects.Sprites()
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
    walls = ray_casting(player, drawing.textures)
    drawing.world(walls + [obj.object_locate(player, walls) for obj in sprites.list_of_objects])
    drawing.fps(clock)
    # drawing.mini_map(player)

    pygame.display.flip()
    clock.tick()
