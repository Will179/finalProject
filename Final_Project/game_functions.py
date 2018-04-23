import sys

import pygame

def check_events(player):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
            elif event.key == pygame.K_LEFT:
                player.moving_left = True
            elif event.key == pygame.K_UP:
                player.moving_up = True
            elif event.key == pygame.K_DOWN:
                player.moving_down = True

                # Move the player to the right.
                player.rect.centerx += 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            elif event.key == pygame.K_LEFT:
                player.moving_left = False
            elif event.key == pygame.K_UP:
                player.moving_up = False
            elif event.key == pygame.K_DOWN:
                player.moving_down = False


def update_screen(ai_settings, screen, player):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    player.blitme()
    # Make the most recently drawn screen visible.
    pygame.display.flip()

