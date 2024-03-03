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
            pygame.quit()
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                if isinstance(self.location, GameLocation):
                    self.location = StartLocation(self)
                elif isinstance(self.location, StartLocation):
                    pygame.quit()
                

# main function
def run_doodle():
    game = Game()

    start_location = StartLocation(game)

    game.location = start_location
    #game.location = GameLocation(game,'Т0стер')

    clock = pygame.time.Clock()
    while 1:
        clock.tick(fps)
        game.location.draw()
        pygame.display.flip()
        event = []
        for event_ in pygame.event.get():
            event = event_
            game.location.event(event)
            game.event(event)     
            
    
if __name__ == "__main__":
    run_doodle()
