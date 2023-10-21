import pygame
import constant as config
from util.setup import Container
from util.maths import Gravity


def init():
    pygame.init()
    screen = pygame.display.set_mode(
        (config.window_width, config.window_height))

    desired_fps = 60
    frame_time = 1 / desired_fps
    previous_time = pygame.time.get_ticks()
    accumulator = 0.0

    gravity = Gravity([0, 9.81])
    container = Container(screen, [gravity])

    container.update()
    container.update()
    container.update()
    container.update()
    container.update()
    container.update()
    container.update()
    container.update()
    container.update()

    running = True
    while running:
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - previous_time) / 1000.0
        previous_time = current_time
        accumulator += elapsed_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        while accumulator >= frame_time:
            accumulator -= frame_time

        pygame.display.flip()

    pygame.quit()
