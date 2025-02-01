import pygame
import constant as config
from util.setup import Container


def init():
    pygame.init()
    screen = pygame.display.set_mode(
        (config.window_width, config.window_height))

    frame_time = 1/60
    container = Container(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        container.update(frame_time)
        pygame.display.flip()

    pygame.quit()
