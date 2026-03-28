import pygame
from utils.collision import make_rect
from entities.base import Entity


class Explosion(Entity):
    DURATION = 0.2  # seconds

    def __init__(self, postition: pygame.Vector2):
        super().__init__()
        self.position = pygame.Vector2(postition)
        self.elapsed = 0
        self.color = "orange"

    @property
    def rect(self):
        return make_rect(self.position, self.get_radius())

    def update(self, dt, game_state):
        self.elapsed += dt
        if self.elapsed >= self.DURATION:
            self.dead = True

    def get_radius(self):
        progress = self.elapsed / self.DURATION
        return int(progress * 80)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.get_radius())
