import sys

import pygame

import os
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
class Sounds:
    die: pygame.mixer.Sound
    hit: pygame.mixer.Sound
    point: pygame.mixer.Sound
    swoosh: pygame.mixer.Sound
    wing: pygame.mixer.Sound

    def __init__(self) -> None:
        if "win" in sys.platform:
            ext = "wav"
        else:
            ext = "wav"

        self.die = pygame.mixer.Sound(
            os.path.join(base_path, f"assets/audio/die.{ext}")
        )
        self.hit = pygame.mixer.Sound(
            os.path.join(base_path, f"assets/audio/hit.{ext}")
        )
        self.point = pygame.mixer.Sound(
            os.path.join(base_path, f"assets/audio/point.{ext}")
        )
        self.swoosh = pygame.mixer.Sound(
            os.path.join(base_path, f"assets/audio/swoosh.{ext}")
        )
        self.wing = pygame.mixer.Sound(
            os.path.join(base_path, f"assets/audio/wing.{ext}")
        )
