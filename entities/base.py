class Entity:
    def __init__(self):
        self.dead = False
        self.solid = False  # does this block movement?

    def update(self, dt, game_state):
        pass

    def draw(self, screen):
        pass
