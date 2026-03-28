import pygame
import settings


def check_collision(pos: pygame.Vector2, wall_rects) -> bool:
    player_rect = pygame.Rect(
        pos.x - settings.PLAYER_RADIUS,
        pos.y - settings.PLAYER_RADIUS,
        settings.PLAYER_RADIUS * 2,
        settings.PLAYER_RADIUS * 2,
    )
    for wr in wall_rects:
        if player_rect.colliderect(wr):
            return True
    return False
