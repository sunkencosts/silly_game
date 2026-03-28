import pygame
import settings
from utils.collision import check_collision
from entities.base import Entity


class Player(Entity):
    def __init__(self, pos: pygame.Vector2):
        super().__init__()
        self.pos = pygame.Vector2(pos)

    def update(self, dt, game_state):
        keys = pygame.key.get_pressed()
        wall_rects = [e.rect for e in game_state.get_walls()]
        new_pos = pygame.Vector2(self.pos)
        if keys[pygame.K_a]:
            new_pos.x -= settings.PLAYER_SPEED * dt
        if keys[pygame.K_d]:
            new_pos.x += settings.PLAYER_SPEED * dt

        if not check_collision(new_pos, wall_rects):
            self.pos.x = new_pos.x

        new_pos = pygame.Vector2(self.pos)
        if keys[pygame.K_w]:
            new_pos.y -= settings.PLAYER_SPEED * dt
        if keys[pygame.K_s]:
            new_pos.y += settings.PLAYER_SPEED * dt
        if not check_collision(new_pos, wall_rects):
            self.pos.y = new_pos.y

        # then clamp to screen at the end
        player_rect = pygame.Rect(
            self.pos.x - settings.PLAYER_RADIUS,
            self.pos.y - settings.PLAYER_RADIUS,
            settings.PLAYER_RADIUS * 2,
            settings.PLAYER_RADIUS * 2,
        )
        player_rect.clamp_ip(game_state.screen.get_rect())
        self.pos.x = player_rect.centerx
        self.pos.y = player_rect.centery

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.pos, settings.PLAYER_RADIUS)
