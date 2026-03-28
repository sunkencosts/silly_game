import pygame
import settings


def make_rect(pos: pygame.Vector2, radius: int):
    return pygame.Rect(
        pos.x - radius,
        pos.y - radius,
        radius * 2,
        radius * 2,
    )


def check_collision(rect_a: pygame.Rect, rects: list) -> bool:
    return any(rect_a.colliderect(r) for r in rects)


def get_collissions(rect_a: pygame.Rect, entities: list) -> list:
    """Returns all entities whose rect overlaps rect_a"""
    return [e for e in entities if rect_a.colliderect(e.rect)]
