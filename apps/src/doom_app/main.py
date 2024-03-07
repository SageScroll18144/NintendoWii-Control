from .player import Player
from .sprite_objects import *
from .ray_casting import ray_casting_walls
from .drawing import Drawing
from .interaction import Interaction
import gc

def run_doom():
    pygame.init()
    sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
    clock = pygame.time.Clock()

    sc_map = pygame.Surface(MAP_RES)
    sprites = Sprites()
    player = Player(sprites)
    drawing = Drawing(sc, sc_map, player, clock)
    interaction = Interaction(player, sprites, drawing)

    game_exit = drawing.menu()
    if game_exit:
        pygame.mixer.music.stop()
        return
    pygame.mouse.set_visible(False)

    interaction.play_music()
    while 1:
        exit_game1 = player.movement()
       
        drawing.background()
        walls, wall_shot = ray_casting_walls(player, drawing.textures)
        drawing.world(walls + [obj.object_locate(player) for obj in sprites.list_of_objects])
        drawing.fps(clock)
        drawing.mini_map()
        drawing.player_weapon([wall_shot, sprites.sprite_shot])
        drawing.life(interaction.life)
        drawing.kills(interaction.contadorMortes)
        interaction.interaction_objects()
        interaction.npc_action()
        interaction.clear_world()
        exit_game2 = interaction.check_death()
        exit_game3 = interaction.check_win()

        if exit_game1 or exit_game2 or exit_game3:
            pygame.mixer.music.stop()
            break

        pygame.display.flip()
        clock.tick()
        #gc.collect()