from .objects import *
try:
    import serial
except:
    pass

def run_agario():
    global cam

    MAIN_SURFACE, cam, cells, blob, painter = init_game()

    # Other Definitions
    NAME = "agar.io"
    VERSION = "0.3"

    # Pygame initialization
    pygame.display.set_caption("{} - v{}".format(NAME, VERSION))
    clock = pygame.time.Clock()

    try:
        ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    except:
        ser = None 

    # Game main loop
    try:
        while(True):
            clock.tick(70)
            for e in pygame.event.get():
                if(e.type == pygame.KEYDOWN):
                    if(e.key == pygame.K_ESCAPE):
                        pygame.quit()
                        break
                    if(e.key == pygame.K_SPACE):
                        blob.split()
                    if(e.key == pygame.K_w):
                        blob.feed()
                if(e.type == pygame.QUIT):
                    pygame.quit()
                    break
            
            keys_accel = 'F'
            try:
                if ser.in_waiting:
                    ser.flushInput()
                    serial_data = ser.read().decode('utf-8')
                    keys_accel = serial_data
            except:
                blob.move()
            if (keys_accel == 'D'):
                blob.moveUp()
            if (keys_accel == 'U'):
                blob.moveDown()
            if (keys_accel == 'L'):
                blob.moveLeft()
            if (keys_accel == 'R'):
                blob.moveRight()
            if (keys_accel == 'S'):
                blob.split()

            print(f"device state: {keys_accel}")

            blob.collisionDetection(cells.list)
            cam.update(blob)
            MAIN_SURFACE.fill((242,251,255))
            # Uncomment next line to get dark-theme
            #surface.fill((0,0,0))
            painter.paint()
            # Start calculating next frame
            pygame.display.flip()
    except Exception as e:
        print("An error occurred: ", e)