import pygame
import math
import struct
from .map import collision_walls
from .settings import *
try:
    import serial
except:
    pass

format_string = 'ffc?'

class Player:
    def __init__(self, sprites):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.sensitivity = 0.004
        self.sprites = sprites
        # collision parameters
        self.side = 50
        self.rect = pygame.Rect(*player_pos, self.side, self.side)
        # weapon settings
        self.shot = False
        #serial connection
        try:
            self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        except:
            self.ser = None

    @property
    def pos(self):
        return (self.x, self.y)

    @property
    def collision_list(self):
        return collision_walls + [pygame.Rect(*obj.pos, obj.side, obj.side) for obj
                                  in self.sprites.list_of_objects if obj.blocked]

    def movement(self):
        exit_command = self.keys_control()
        if exit_command:
            return True
        self.mouse_control()
        self.rect.center = self.x, self.y
        self.angle %= DOUBLE_PI

    def detect_collision(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(self.collision_list)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = self.collision_list[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top

            if abs(delta_x - delta_y) < 20:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_x < delta_y:
                dx = 0
        self.x += dx
        self.y += dy

    def keys_control(self):
        keys_accel = 'F'
        try:
            if self.ser.in_waiting:
                self.ser.flushInput()
                serial_data = self.ser.read().decode('utf-8')
                keys_accel = serial_data
        except:
            pass

        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return True
        if keys[pygame.K_w] or keys_accel == 'D':
            dx, dy = player_speed * cos_a, player_speed * sin_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_s] or keys_accel == 'U':
            dx, dy = -player_speed * cos_a, -player_speed * sin_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_a]:
            dx, dy = player_speed * sin_a, -player_speed * cos_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_d]:
            dx, dy = -player_speed * sin_a, player_speed * cos_a
            self.detect_collision(dx, dy)

        if keys[pygame.K_LEFT] or keys_accel == 'L':
            self.angle -= player_rotation_speed
        if keys[pygame.K_RIGHT] or keys_accel == 'R':
            self.angle += player_rotation_speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not self.shot:
                    self.shot = True

        
        if keys_accel == 'S'  and not self.shot:
            self.shot =  True

    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
            self.angle += difference * self.sensitivity
