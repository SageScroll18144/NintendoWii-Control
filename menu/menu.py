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
image_path='./DDtitle.png',
)
Agario_Image = pygame_menu.baseimage.BaseImage(
image_path='./agario.jpg',
)
Flappy_Image = pygame_menu.baseimage.BaseImage(
image_path='./flappybird.jpg',
)
Bomber_Image = pygame_menu.baseimage.BaseImage(
image_path='./bomberman.jpg',
)
Space_Image = pygame_menu.baseimage.BaseImage(
image_path='./SpaceInvaders.png',
)
Tetris_Image = pygame_menu.baseimage.BaseImage(
image_path='./tetris.jpg',
)


menu = pygame_menu.Menu('                    ARCADE GAMES', 600, 400,
                       theme= meu_tema)

menu.add.vertical_margin(50)
menu.add.button('                ', start_doodle(), background_color=Dudu_Image, font_size=80   )
menu.add.button('                ', start_bomber(), background_color=Bomber_Image, font_size=80)
menu.add.vertical_margin(20)
menu.add.button('                ', start_agario(),  background_color=Agario_Image, font_size=80 )
menu.add.vertical_margin(20)
menu.add.button('                ', start_flappy(), background_color=Flappy_Image, font_size=80)
menu.add.vertical_margin(20)
menu.add.button('                ', start_flappy(), background_color=Tetris_Image, font_size=80)
menu.add.vertical_margin(20)
menu.add.button('                ', start_space(), background_color=Space_Image, font_size=80)
menu.add.vertical_margin(20)
menu.add.button('Fechar', pygame_menu.events.EXIT)


#Run the menu
menu.mainloop(surface)