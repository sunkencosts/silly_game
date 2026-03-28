# Example file showing a circle moving on screen
import pygame

from entities.explosion import Explosion
from entities.player import Player
from entities.wall import Wall
from game_state import GameState
import settings


pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Silly Game")

game_state = GameState(screen)

starting_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player = Player(starting_position)
game_state.add(player)

for i in range(10):
    game_state.add(Wall(100 * i, 100, 50, 25))

space_was_pressed = False
dt = 0

running = True
while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for entity in game_state.entities:
        entity.update(dt, game_state)
    game_state.cleanup()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not space_was_pressed:
        game_state.add(Explosion(player.pos))
    space_was_pressed = keys[pygame.K_SPACE]

    # Draw
    game_state.screen.fill("black")

    for entity in game_state.entities:
        entity.draw(game_state.screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000


pygame.quit()
