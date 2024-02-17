import pygame
from aliens import main as Alien
from stars import main as Stars
from blit_blends import main as LeftGame
from blend_fill import main as RightGame

def main():
    pygame.init()

    try:
        while True:
            screen = pygame.display.set_mode((500, 500))
            screen.fill((255, 0, 0))
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == "q":
                    break
                if event.key == pygame.K_DOWN:
                    Alien()
                if event.key == pygame.K_UP:
                   Stars()
                if event.key == pygame.K_LEFT:
                   LeftGame()
                if event.key == pygame.K_RIGHT:
                   RightGame()
    finally:
        pygame.quit()

if __name__ == "_main_":
    main()