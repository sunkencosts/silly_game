# game_state.py
class GameState:
    def __init__(self, screen):
        self.entities = []
        self.screen = screen

    def get_walls(self):
        return [e for e in self.entities if e.solid]

    def add(self, entity):
        self.entities.append(entity)

    def cleanup(self):
        self.entities = [e for e in self.entities if not e.dead]
