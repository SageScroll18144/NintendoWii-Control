import pygame
import pygame_menu
import cv2

def run_menu():
    pygame.init()
    surface = pygame.display.set_mode((600, 400))
    create_menu(surface)

def start_tetris():
    print('tetris')

def start_flappy():
    print('flappy')

def start_space():
    print('space')

def start_bomber():
    print('bomber')

def start_doodle():
    print('doodle')

def start_agario():
    print('agario')

def start_doom():
    print('doom')

def run_intro():
    video = cv2.VideoCapture("video/boot.mp4")
    success, video_image = video.read()
    fps = video.get(cv2.CAP_PROP_FPS)

    window = pygame.display.set_mode(video_image.shape[1::-1])
    clock = pygame.time.Clock()

    run = success
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        success, video_image = video.read()
        if success:
            video_surf = pygame.image.frombuffer(
                video_image.tobytes(), video_image.shape[1::-1], "BGR")
        else:
            run = False
        window.blit(video_surf, (0, 0))
        pygame.display.flip()

def create_menu(surface: pygame.Surface): 
    menu = pygame_menu.Menu(
        '                    ARCADE GAMES',
        600, 400, theme=main_theme, columns=2, rows=5
    )

    ## Column 1
    menu.add.vertical_margin(10)
    menu.add.button(
        '1', start_doodle, background_color=base_images['doodle'],
        **default_button_config
    )
    menu.add.button(
        '2', start_bomber, background_color=base_images['bomber'],
        **default_button_config
    )
    menu.add.button(
        '3', start_agario, background_color=base_images['agario'],
        **default_button_config
    )
    menu.add.button(
        '4', start_doom, background_color=base_images['doom'],
        **default_button_config
    )

    ## Column 2
    menu.add.vertical_fill()
    menu.add.button(
        '5', start_flappy, background_color=base_images['flappy'],
        **default_button_config
    )
    menu.add.button(
        '6', start_flappy, background_color=base_images['tetris'],
        **default_button_config
    )
    menu.add.button(
        '7', start_space, background_color=base_images['space'],
        **default_button_config
    )
    menu.add.button('Fechar', pygame_menu.events.EXIT)
    #Run the menu
    menu.mainloop(surface)

# Menu variables
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

if __name__ == "_main_":
    run_menu()