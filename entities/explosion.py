import pygame


class Explosion:
    DURATION = 0.2  # seconds

    def __init__(self, postition: pygame.Vector2):
        super().__init__()
        self.position = pygame.Vector2(postition)
        self.elapsed = 0
        self.color = "orange"

    def is_dead(self):
        return self.elapsed >= self.DURATION

    def update(self, dt):
        self.elapsed += dt

    def get_radius(self):
        progress = self.elapsed / self.DURATION
        return int(progress * 80)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.get_radius())
