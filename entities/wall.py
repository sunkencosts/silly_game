import pygame
from entities.base import Entity


class Wall(Entity):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.solid = True
        self._rect = pygame.Rect(x, y, w, h)

    @property
    def rect(self):
        return self._rect

    def draw(self, screen):
        pygame.draw.rect(screen, "white", self._rect)
