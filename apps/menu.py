import pygame
import pygame_menu
from rw_emb_comp_funcs import RWEmbCompFuncs
from bomberman_app import run_bomberman
from doom_app import run_doom
from doodle_app import run_doodle
from agario_app import run_agario
from matris_app import run_matris
from flappy_app import run_flappy
from space_invaders_app import run_space_invaders

main_theme = pygame_menu.themes.Theme(
    background_color=(18, 52, 86),
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

base_images = {}
for game, url in images_url.items():
    base_images[game] = pygame_menu.baseimage.BaseImage(image_path=url)

default_button_config = {
    'font_size': 80, 'padding': (10, 100), 'margin': (0, 10)
}

total_tickets = 7


class Menu:
    def __init__(self):
        self.games_started_count = total_tickets
        self.surface = pygame.display.set_mode((600, 500))
        self.create_menu()

    def start_game(self, game: str):
        if self.games_started_count <= 0:
            RW.green_leds(0)
            print('No more tickets')
            return

        self.games_started_count -= 1
        RW.seven_segment_r(self.games_started_count)
        RW.green_leds(self.games_started_count)

        games = {
            'doodle': run_doodle,
            'agario': run_agario,
            'doom': run_doom,
            'flappy': run_flappy,
            'space': run_space_invaders,
            'tetris': run_matris,
            'bomber': run_bomberman
        }

        if game in games:
            games[game]()

        RW.red_leds(0)
        RW.seven_segment_l(0)
        pygame.display.set_mode((600, 500))

    def create_menu(self):
        menu = pygame_menu.Menu(
            '                    ARCADE GAMES',
            600, 500, theme=main_theme, columns=2, rows=5
        )

        ## Column 1
        menu.add.vertical_margin(5)
        menu.add.button(
            '1',
            lambda: self.start_game('doodle') if int(RW.read_switches(), 2) == 1 and int(RW.read_button(), 2) == 7 else None,
            background_color=base_images['doodle'],
            **default_button_config
        )
        menu.add.button(
            '2',
            lambda: self.start_game('bomber') if int(RW.read_switches(), 2) == 2 and int(RW.read_button(), 2) == 7 else None,
            background_color=base_images['bomber'],
            **default_button_config
        )
        menu.add.button(
            '3',
            lambda: self.start_game('agario') if int(RW.read_switches(), 2) == 3 and int(RW.read_button(), 2) == 7 else None,
            background_color=base_images['agario'],
            **default_button_config
        )
        menu.add.button(
            '4',
            lambda: self.start_game('doom') if int(RW.read_switches(), 2) == 4 and int(RW.read_button(), 2) == 7 else None,
            background_color=base_images['doom'],
            **default_button_config
        )

        ## Column 2
        menu.add.vertical_margin(5)
        menu.add.button(
            '5',
            lambda: self.start_game('flappy') if int(RW.read_switches(), 2) == 5 and int(RW.read_button(), 2) == 7 else None,
            background_color=base_images['flappy'],
            **default_button_config
        )
        menu.add.button(
            '6',
            lambda: self.start_game('tetris') if int(RW.read_switches(), 2) == 6 and int(RW.read_button(), 2) == 7 else None,
            background_color=base_images['tetris'],
            **default_button_config
        )
        menu.add.button(
            '7',
            lambda: self.start_game('space') if int(RW.read_switches(), 2) == 7 and int(RW.read_button(), 2) == 7 else None,
            background_color=base_images['space'],
            **default_button_config
        )
        menu.add.button(
            'Fechar',
            lambda: pygame_menu.events.EXIT if int(RW.read_switches(), 2) == 1 and int(RW.read_button(), 2) == 14 else None
        )
        RW.green_leds(7)
        RW.seven_segment_r(self.games_started_count)
        # Run the menu
        menu.mainloop(self.surface)


if __name__ == '__main__':
    pygame.init()
    RW = RWEmbCompFuncs()
    menu = Menu()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break  # Sai do loop se o usuário fechar a janela

        # Atualize a tela do menu
        menu.surface.fill((18, 52, 86))  # Preenche a tela com a cor de fundo do tema
        menu.create_menu()  # Renderiza o menu na tela
        pygame.display.flip()  # Atualiza a tela

    pygame.quit()
    quit()
