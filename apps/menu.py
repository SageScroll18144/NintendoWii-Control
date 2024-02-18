import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((600, 400))


def start_tetris():
    # Do the job here !
    pass
def start_flappy():
    # Do the job here !
    pass
def start_space():
    # Do the job here !
    pass
def start_bomber():
    # Do the job here !
    pass
def start_doodle():
    # Do the job here !
    pass
def start_agario():
    # Do the job here !
    pass
  

meu_tema = pygame_menu.themes.Theme(
    background_color= 	(18,52,86),  # cor de fundo
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE,  # estilo da barra de título
    title_background_color='white',
    title_font=pygame_menu.font.FONT_FRANCHISE,  # fonte do título
    title_font_size=60,  # tamanho da fonte do título
    title_font_color='black',  # cor da fonte do título
    widget_font=pygame_menu.font.FONT_FRANCHISE,  # fonte dos widgets
    widget_font_size=40,  # tamanho da fonte dos widgets
    widget_font_color='black',  # cor da fonte dos widgets
    widget_alignment=pygame_menu.locals.ALIGN_CENTER,  # alinhamento dos widgets
    widget_margin=(0, 20),  # margem dos widgets
    
)


Dudu_Image = pygame_menu.baseimage.BaseImage(
image_path='./images/DDtitle.png',
)
Agario_Image = pygame_menu.baseimage.BaseImage(
image_path='./images/agario.jpg',
)
Flappy_Image = pygame_menu.baseimage.BaseImage(
image_path='./images/flappybird.jpg',
)
Bomber_Image = pygame_menu.baseimage.BaseImage(
image_path='./images/bomberman.jpg',
)
Space_Image = pygame_menu.baseimage.BaseImage(
image_path='./images/SpaceInvaders.png',
)
Tetris_Image = pygame_menu.baseimage.BaseImage(
image_path='./images/tetris.jpg',
)


menu = pygame_menu.Menu('ARCADE GAMES', 600, 400,
             theme= meu_tema, columns=2, rows=5)

default_button_config = {'font_size': 80, 'padding': (10, 100), 'margin': (0, 10)}
## Column 1
menu.add.vertical_margin(10)
menu.add.button('', start_doodle(), background_color=Dudu_Image, **default_button_config)
menu.add.button('', start_bomber(), background_color=Bomber_Image, **default_button_config)
menu.add.button('', start_agario(),  background_color=Agario_Image, **default_button_config)
menu.add.vertical_fill()

## Column 2
menu.add.vertical_fill()
menu.add.button('', start_flappy(), background_color=Flappy_Image, **default_button_config)
menu.add.button('', start_flappy(), background_color=Tetris_Image, **default_button_config)
menu.add.button('', start_space(), background_color=Space_Image, **default_button_config)
menu.add.button('Fechar', pygame_menu.events.EXIT)
#Run the menu
menu.mainloop(surface)