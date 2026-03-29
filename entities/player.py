import pygame
import settings
from utils.collision import check_collision, get_collissions, make_rect
from entities.base import Entity


class Player(Entity):
    def __init__(self, pos: pygame.Vector2):
        super().__init__()
        self.pos = pygame.Vector2(pos)
        self.size_modifier = 0

    @property
    def radius(self):
        return settings.PLAYER_RADIUS + self.size_modifier

    @property
    def rect(self):
        return make_rect(self.pos, self.radius)

    def update(self, dt, game_state):
        keys = pygame.key.get_pressed()
        wall_rects = [e.rect for e in game_state.get_walls()]
        explosions = game_state.get_explosions()
        pickups = game_state.get_pickups()

        new_pos = pygame.Vector2(self.pos)
        if keys[pygame.K_a]:
            new_pos.x -= settings.PLAYER_SPEED * dt
        if keys[pygame.K_d]:
            new_pos.x += settings.PLAYER_SPEED * dt

        if not check_collision(make_rect(new_pos, self.radius), wall_rects):
            self.pos.x = new_pos.x

        new_pos = pygame.Vector2(self.pos)
        if keys[pygame.K_w]:
            new_pos.y -= settings.PLAYER_SPEED * dt
        if keys[pygame.K_s]:
            new_pos.y += settings.PLAYER_SPEED * dt
        if not check_collision(make_rect(new_pos, self.radius), wall_rects):
            self.pos.y = new_pos.y

        hit = get_collissions(self.rect, explosions)
        if hit:
            print(f"Player hit by {len(hit)} explosion(s)!")

        onPickups = get_collissions(self.rect, pickups)

        if onPickups:
            print(f"Player on pickup! Give POWER!")
            self.size_modifier += 1
            game_state.score += 1
            for pickup in onPickups:
                pickup.dead = True

        # then clamp to screen at the end
        player_rect = pygame.Rect(
            self.pos.x - self.radius,
            self.pos.y - self.radius,
            self.radius * 2,
            self.radius * 2,
        )
        player_rect.clamp_ip(game_state.screen.get_rect())
        self.pos.x = player_rect.centerx
        self.pos.y = player_rect.centery

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.pos, self.radius)
