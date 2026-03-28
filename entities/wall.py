import pygame
from entities.base import Entity


class Wall(Entity):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.solid = True
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rect)
