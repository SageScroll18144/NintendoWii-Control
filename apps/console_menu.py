import pygame
import cv2
import sys
sys.path.append('Bomb-app/')

# from aliens import main as Alien
# from stars import main as Stars
# from blit_blends import main as LeftGame
# from blend_fill import main as RightGame

from bomb_app import main as DOOM

def main():
    
    # setup 
    pygame.init()

    # video = cv2.VideoCapture("video/boot.mp4")
    # success, video_image = video.read()
    # fps = video.get(cv2.CAP_PROP_FPS)

    # window = pygame.display.set_mode(video_image.shape[1::-1])
    # clock = pygame.time.Clock()

    # run = success
    # while run:
    #     clock.tick(fps)
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             run = False
        
    #     success, video_image = video.read()
    #     if success:
    #         video_surf = pygame.image.frombuffer(
    #             video_image.tobytes(), video_image.shape[1::-1], "BGR")
    #     else:
    #         run = False
    #     window.blit(video_surf, (0, 0))
    #     pygame.display.flip()

    # loop

    try:
        while True:
            screen = pygame.display.set_mode((500, 500))
            screen.fill((255, 0, 0))
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            #if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == "q":
                break
            if event.key == pygame.K_DOWN:
                DOOM()
                
    finally:
        pygame.quit()

if __name__ == "_main_":
    main()