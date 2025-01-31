import pygame
import constant as config
from util.setup import Container


def init():
    pygame.init()
    screen = pygame.display.set_mode(
        (config.window_width, config.window_height))

    clock = pygame.time.Clock()
    desired_fps = 60
    frame_time = 1 / desired_fps
    previous_time = pygame.time.get_ticks() / 1000.0
    accumulator = 0.0

    container = Container(screen)

    running = True
    while running:
        current_time = pygame.time.get_ticks() / 1000.0
        elapsed_time = current_time - previous_time
        previous_time = current_time
        accumulator += elapsed_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        while accumulator >= frame_time:
            container.update(frame_time)
            accumulator -= frame_time

        pygame.display.flip()
        clock.tick(desired_fps)

    pygame.quit()
