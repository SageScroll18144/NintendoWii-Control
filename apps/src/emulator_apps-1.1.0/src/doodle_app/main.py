#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
# _view for exe building
#from pygame import _view
from pygame.locals import *

from .locations import *
from .sprites import *

from .config import screen_width, screen_height, fps


# Main class for game window
class Game():

    def __init__(self):
        pygame.init()
        window = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Doodle jump')
    def event(self, event):
        if event.type == QUIT:
            return False
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                if isinstance(self.location, GameLocation):
                    self.location = StartLocation(self)
                elif isinstance(self.location, StartLocation):
                    return False
        return True
                

# main function
def run_doodle():
    running = True
    game = Game()

    start_location = StartLocation(game)

    game.location = start_location
    #game.location = GameLocation(game,'Т0стер')

    clock = pygame.time.Clock()
    while running:
        clock.tick(fps)
        game.location.draw()
        pygame.display.flip()
        event = []
        for event_ in pygame.event.get():
            event = event_
            exit1 = game.location.event(event)
            exit2 = game.event(event)     
            running = exit1 and exit2
if __name__ == "__main__":
    run_doodle()
