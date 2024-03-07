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

class Menu:
    def __init__(self):
        self.surface = pygame.display.set_mode((600, 500))
        self.create_menu()

    def start_game(self, game: str):
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
        
        pygame.display.set_mode((600, 500))

    def create_menu(self): 
        menu = pygame_menu.Menu(
            '                    ARCADE GAMES',
            600, 500, theme=main_theme, columns=2, rows=5
        )

        ## Column 1
        menu.add.vertical_margin(5)
        menu.add.button(
            '1',lambda: self.start_game('doodle'), background_color=base_images['doodle'],
            **default_button_config
        )
        menu.add.button(
            '2',lambda: self.start_game('bomber'), background_color=base_images['bomber'],
            **default_button_config
        )
        menu.add.button(
            '3',lambda: self.start_game('agario'), background_color=base_images['agario'],
            **default_button_config
        )
        menu.add.button(
            '4',lambda: self.start_game('doom'), background_color=base_images['doom'],
            **default_button_config
        )

        ## Column 2
        menu.add.vertical_margin(5)
        menu.add.button(
            '5',lambda: self.start_game('flappy'), background_color=base_images['flappy'],
            **default_button_config
        )
        menu.add.button(
            '6',lambda: self.start_game('tetris'), background_color=base_images['tetris'],
            **default_button_config
        )
        menu.add.button(
            '7',lambda: self.start_game('space'), background_color=base_images['space'],
            **default_button_config
        )
        menu.add.button('Fechar', pygame_menu.events.EXIT)
        #Run the menu
        menu.mainloop(self.surface) 

if __name__ == '__main__':
    pygame.init()
    RW = RWEmbCompFuncs()

    menu = Menu()
    pygame.quit()
    quit()