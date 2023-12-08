import math
import pygame
import settings
from map import world_map, WORLD_WIDTH, WORLD_HEIGHT


def mapping(a, b):
    return (a // settings.TILE) * settings.TILE, (b // settings.TILE) * settings.TILE


def ray_casting(player, textures):
    walls = []
    ox, oy = player.pos
    texture_v, texture_h = 1, 1
    xm, ym = mapping(ox, oy)
    cur_angle = player.angle - settings.HALF_FOV
    for ray in range(settings.NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001

        # verticals
        x, dx = (xm + settings.TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WORLD_WIDTH, settings.TILE):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            x += dx * settings.TILE

        # horizontals
        y, dy = (ym + settings.TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, WORLD_HEIGHT, settings.TILE):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            y += dy * settings.TILE

        # projection
        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        offset = int(offset) % settings.TILE
        depth *= math.cos(player.angle - cur_angle)
        depth = max(depth, 0.00001)
        proj_height = min(int(settings.PROJ_COEFF / depth), settings.PENTA_HEIGHT)

        wall_column = textures[texture].subsurface(offset * settings.TEXTURE_SCALE, 0, settings.TEXTURE_SCALE, settings.TEXTURE_HEIGHT)
        wall_column = pygame.transform.scale(wall_column, (settings.SCALE, proj_height))
        wall_pos = (ray * settings.SCALE, settings.HALF_HEIGHT - proj_height // 2)

        walls.append((depth, wall_column, wall_pos))
        cur_angle += settings.DELTA_ANGLE
    return walls
