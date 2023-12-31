import math
import pygame
import settings
from ray_casting import ray_casting
from map import mini_map


class Drawing:
    
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont("Arial", 36, bold=True)
        self.textures = {1: pygame.image.load("img/wall3.png").convert(),
                         2: pygame.image.load("img/wall4.png").convert(),
                         3: pygame.image.load("img/wall5.png").convert(),
                         4: pygame.image.load("img/wall6.png").convert(),
                         "S": pygame.image.load("img/sky1.png").convert()
                         }

    def background(self, angle):
        sky_offset = -10 * math.degrees(angle) % settings.WIDTH
        self.sc.blit(self.textures["S"], (sky_offset, 0))
        self.sc.blit(self.textures["S"], (sky_offset - settings.WIDTH, 0))
        self.sc.blit(self.textures["S"], (sky_offset + settings.WIDTH, 0))
        pygame.draw.rect(self.sc, settings.DARKGRAY, (0, settings.HALF_HEIGHT, settings.WIDTH, settings.HALF_HEIGHT))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.sc.blit(object, object_pos)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, settings.DARKORANGE)
        self.sc.blit(render, settings.FPS_POS)

    def mini_map(self, player):
        self.sc_map.fill(settings.BLACK)
        map_x, map_y = player.x // settings.MAP_SCALE, player.y // settings.MAP_SCALE
        pygame.draw.line(self.sc_map, settings.YELLOW, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                 map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.sc_map, settings.RED, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, settings.DARKBROWN, (x, y, settings.MAP_TILE, settings.MAP_TILE))
        self.sc.blit(self.sc_map, settings.MAP_POS)
