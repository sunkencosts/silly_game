import pygame


class Entity:
    def __init__(self):
        self.dead = False
        self.solid = False  # does this block movement?

    @property
    def rect(self) -> pygame.Rect:
        raise NotImplementedError("Entities that collide must implement rect")

    def update(self, dt, game_state):
        pass

    def draw(self, screen):
        pass
