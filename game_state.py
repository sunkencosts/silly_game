# game_state.py
from entities.explosion import Explosion


class GameState:
    def __init__(self, screen):
        self.entities = []
        self.screen = screen

    def get_walls(self):
        return [e for e in self.entities if e.solid]

    def get_explosions(self):
        return [e for e in self.entities if isinstance(e, Explosion)]

    def add(self, entity):
        self.entities.append(entity)

    def cleanup(self):
        self.entities = [e for e in self.entities if not e.dead]
