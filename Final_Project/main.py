'''

Final Project: 2d, top-down, dungeon crawler game.
Explore, fight monsters, get loot

First Major Milestone: Moving charectar around map
Don't know?: How to generate worlds
How is project too ambitious?: Many things that I do not know currently, something could be much harder than I think
In what ways is your project not ambitous enough?: Gameplay could be very simple, it is possible that what I want to do is too hard
and what I end up with is not good enough.

Progress Report:
Week 1 + Break: Started Project, open game window with seperate files for settings
Week 2: Some technical difficulties with VS:Code.  Let myself get a bit lazy and used technical difficulties
as an excuse to be lazy.
Plan for week 3: Use long weeked to catch up, and get back to where I need to be.  Hopefully I will have a
player moving around a map by this time next week.


'''
import turtle
import pygame
import random
import math
import sys
from settings import Settings
from player import Player
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Dungeon Crawler")
    #create player
    player = Player(screen)

    # Start the main loop for the game.
    while True:
        gf.check_events(player)
        player.update()
        gf.update_screen(ai_settings, screen, player)
        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        player.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()

