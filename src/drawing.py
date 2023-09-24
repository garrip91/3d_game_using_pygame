import pygame
import settings
from ray_casting import ray_casting
from map import mini_map
import math


class Drawing:
    
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)

    def background(self):
        pygame.draw.rect(self.sc, settings.SKYBLUE, (0, 0, settings.WIDTH, settings.HALF_HEIGHT))
        pygame.draw.rect(self.sc, settings.DARKGRAY, (0, settings.HALF_HEIGHT, settings.WIDTH, settings.HALF_HEIGHT))

    def world(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, settings.RED)
        self.sc.blit(render, settings.FPS_POS)

    def mini_map(self, player):
        """show mini-map at display"""
        self.sc_map.fill(settings.BLACK)
        map_x, map_y = player.x // settings.MAP_SCALE, player.y // settings.MAP_SCALE
        pygame.draw.line(self.sc_map, settings.YELLOW, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                 map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.sc_map, settings.RED, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, settings.GREEN, (x, y, settings.MAP_TILE, settings.MAP_TILE))
        self.sc.blit(self.sc_map, settings.MAP_POS)
