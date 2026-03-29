import pygame
from utils.collision import make_rect
from entities.base import Entity


class Pickup(Entity):

    def __init__(self, postition: pygame.Vector2, size: int):
        super().__init__()
        self.position = pygame.Vector2(postition)
        self.color = "green"
        self.size = size
        self.dead = False

    @property
    def rect(self):
        return make_rect(self.position, self.size)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.size)
