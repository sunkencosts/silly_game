# game_state.py
from entities.explosion import Explosion
from entities.pickup import Pickup
import random
import settings
import pygame
from utils.collision import make_rect, check_collision


class GameState:
    def __init__(self, screen):
        self.entities = []
        self.screen = screen
        self.pickup_timer = self.pickup_interval = 1
        self.score = 0

    def get_walls(self):
        return [e for e in self.entities if e.solid]

    def get_explosions(self):
        return [e for e in self.entities if isinstance(e, Explosion)]

    def get_pickups(self):
        return [e for e in self.entities if isinstance(e, Pickup)]

    def add(self, entity):
        self.entities.append(entity)

    def update(self, dt):
        self.pickup_timer += dt
        if self.pickup_timer >= self.pickup_interval:
            self.pickup_timer = 0
            self.spawn_pickup()

    def spawn_pickup(self):
        wall_rects = [e for e in self.entities if e.solid]
        for _ in range(20):
            x = random.randint(20, settings.SCREEN_WIDTH - 20)
            y = random.randint(20, settings.SCREEN_HEIGHT - 20)
            candidate = make_rect(pygame.Vector2(x, y), settings.PICKUP_RADIUS)
            if not check_collision(candidate, wall_rects):
                self.add(Pickup(pygame.Vector2(x, y), settings.PICKUP_RADIUS))
                return

    def cleanup(self):
        self.entities = [e for e in self.entities if not e.dead]
