import pygame
import pygame_menu
import cv2

from rw_emb_comp_funcs import RWEmbCompFuncs

from bomberman_app import run_bomberman
from doom_app import run_doom
from doodle_app import run_doodle
from agario_app import run_agario
from matris_app import run_matris
from flappy_app import run_flappy
from space_invaders_app import run_space_invaders

import threading

main_theme = pygame_menu.themes.Theme(
    background_color= 	(18,52,86),
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE,
    title_background_color='white',
    title_font=pygame_menu.font.FONT_FRANCHISE,
    title_font_size=60,
    title_font_color='black',
    widget_font=pygame_menu.font.FONT_FRANCHISE,
    widget_font_size=40,
    widget_font_color='black',
    widget_alignment=pygame_menu.locals.ALIGN_CENTER,
    widget_margin=(0, 20),
)

images_url = {
    'doodle': './images/DDtitle.png',
    'agario': './images/agario.jpg',
    'flappy': './images/flappybird.jpg',
    'bomber': './images/bomberman.jpg',
    'space': './images/SpaceInvaders.png',
    'tetris': './images/tetris.jpg',
    'doom': './images/doom.jpg'
}

base_images = {
    'doodle': pygame_menu.baseimage.BaseImage(
        image_path=images_url['doodle'],
    ),
    'agario': pygame_menu.baseimage.BaseImage(
        image_path=images_url['agario'],
    ),
    'flappy': pygame_menu.baseimage.BaseImage(
        image_path=images_url['flappy'],
    ),
    'bomber': pygame_menu.baseimage.BaseImage(
        image_path=images_url['bomber'],
    ),
    'space': pygame_menu.baseimage.BaseImage(
        image_path=images_url['space'],
    ),
    'tetris': pygame_menu.baseimage.BaseImage(
        image_path=images_url['tetris'],
    ),
    'doom': pygame_menu.baseimage.BaseImage(
        image_path=images_url['doom'],
    ),
}

default_button_config = {
    'font_size': 80, 'padding': (10, 100), 'margin': (0, 10)
}

total_tickets = 7

class Menu:
    def __init__(self):
        self.games_started_count = total_tickets
        self.surface = pygame.display.set_mode((600, 500))
        RW.green_leds(7)
        RW.seven_segment_r(self.games_started_count)
        threading.Thread(target=self.check_switches_and_buttons).start()


    def start_game(self, game: str):
        if (self.games_started_count <= 0):
            RW.green_leds(0)
            print('No more tickets')
            return
        
        self.games_started_count -= 1
        RW.seven_segment_r(self.games_started_count)
        RW.green_leds(self.games_started_count)

        if game == 'doodle':
            run_doodle()
        elif game == 'agario':
            run_agario()
        elif game == 'doom':
            run_doom()
        elif game == 'flappy':
            run_flappy()
        elif game == 'space':
            run_space_invaders()
        elif game == 'tetris':
            run_matris()
        elif game == 'bomber':
            run_bomberman()
        else:
            print('Game not found')

        RW.red_leds(0)
        RW.seven_segment_l(0)
        pygame.display.set_mode((600, 500))
    
    def check_switches_and_buttons(self):
        while True:
            switch_value = int(RW.read_switches(), 2)
            button_value = int(RW.read_button(), 2)

            print(f"switch_value: {switch_value} | button_value: {button_value}")

            if switch_value == 1 and button_value == 7:
                self.start_game('doodle')
            elif switch_value == 2 and button_value == 7:
                self.start_game('bomber')
            elif switch_value == 4 and button_value == 7:
                self.start_game('doom')
            elif switch_value == 5 and button_value == 7:
                self.start_game('flappy')
            elif switch_value == 6 and button_value == 7:
                self.start_game('tetris')
            elif switch_value == 7 and button_value == 7:
                self.start_game('space')

            pygame.time.wait(100)  # espera um pouco para não sobrecarregar a CPU

if __name__ == '__main__':
    pygame.init()
    RW = RWEmbCompFuncs()
    menu = Menu()
    pygame.quit()
    quit()