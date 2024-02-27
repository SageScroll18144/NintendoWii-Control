import random
from typing import List, Tuple

import pygame

from .constants import BACKGROUNDS, PIPES, PLAYERS
import os
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

class Images:
    numbers: List[pygame.Surface]
    game_over: pygame.Surface
    welcome_message: pygame.Surface
    base: pygame.Surface
    background: pygame.Surface
    player: Tuple[pygame.Surface]
    pipe: Tuple[pygame.Surface]

    def __init__(self) -> None:
        self.numbers = list(
            (
                pygame.image.load(
                    os.path.join(base_path, f"assets/sprites/{num}.png")
                ).convert_alpha()
                for num in range(10)
            )
        )

        # game over sprite
        self.game_over = pygame.image.load(
            os.path.join(base_path, "assets/sprites/gameover.png")
        ).convert_alpha()
        # welcome_message sprite for welcome screen
        self.welcome_message = pygame.image.load(
            os.path.join(base_path, "assets/sprites/message.png")
        ).convert_alpha()
        # base (ground) sprite
        self.base = pygame.image.load(
            os.path.join(base_path, "assets/sprites/base.png")
        ).convert_alpha()
        self.randomize()

    def randomize(self):
        # select random background sprites
        rand_bg = random.randint(0, len(BACKGROUNDS) - 1)
        # select random player sprites
        rand_player = random.randint(0, len(PLAYERS) - 1)
        # select random pipe sprites
        rand_pipe = random.randint(0, len(PIPES) - 1)

        self.background = pygame.image.load(
            os.path.join(base_path, BACKGROUNDS[rand_bg])
        ).convert()
        self.player = (
            pygame.image.load(
                os.path.join(base_path, PLAYERS[rand_player][0]
            )).convert_alpha(),
            pygame.image.load(
                os.path.join(base_path, PLAYERS[rand_player][1]
            )).convert_alpha(),
            pygame.image.load(
                os.path.join(base_path, PLAYERS[rand_player][2]
            )).convert_alpha(),
        )
        self.pipe = (
            pygame.transform.flip(
                pygame.image.load(
                    os.path.join(base_path, PIPES[rand_pipe]
                )).convert_alpha(),
                False,
                True,
            ),
            pygame.image.load(
                os.path.join(base_path, PIPES[rand_pipe])
            ).convert_alpha(),
        )
