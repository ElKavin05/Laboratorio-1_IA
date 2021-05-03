importar retro
importar pygame
desde la importación de pygame.locals *
importar cv2
importar numpy como np
importar imutils


video_size = 700, 500

def key_action ():
    # ["B", "A", "MODO", "INICIO", "ARRIBA", "ABAJO", "IZQUIERDA", "DERECHA", "C", "Y", "X", "Z"]
    botones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    claves = pygame.key.get_pressed ()
    si claves [K_LEFT]:
        botones [6] = 1
    si claves [K_UP]:
        botones [0] = 1
    si claves [K_RIGHT]:
        botones [7] = 1
    si claves [K_DOWN]:
        botones [5] = 1
    botones de retorno

pygame.init ()
env = retro.make ('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1', record = ".")
screen = pygame.display.set_mode (video_size)
env.reset ()

done = False
reloj = pygame.time.Clock ()
mientras no esté hecho:
    clock.tick (60) # Alentar un poco, quitar si prefieren entrar en modo ultra instinto
    img = env.render (mode = 'rgb_array') # Esta porqueria viene rotada, hay que darle forma.
    img = np.flipud (np.rot90 (img)) # La rotamos
    image_np = imutils.resize (img, ancho = 500) # Le ponenes un tamano descente
    surf = pygame.surfarray.make_surface (image_np)
    screen.blit (navegar, (0, 0))
    pygame.display.update ()
    acción = key_action ()
    ob, rew, done, info = env.step (acción)
    pygame.event.pump () ## Escucha los eventos
    imprimir ("Acción", acción, "Recompensa", rew)