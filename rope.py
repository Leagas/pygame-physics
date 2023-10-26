import pygame
import constant as config
from lib.string import Entity


def init():
    pygame.init()
    screen = pygame.display.set_mode(
        (config.window_width, config.window_height))
    screen.fill((255, 255, 255))

    fixed_surface = pygame.Surface((config.window_width, config.window_height))
    fixed_surface.fill((255, 255, 255))

    string = Entity(screen, [300, 300], 25)

    pygame.draw.line(fixed_surface, (0, 0, 0),
                     [config.window_width/2, 0],
                     [config.window_width/2, config.window_height], 1)
    pygame.draw.line(fixed_surface, (0, 0, 0),
                     [0, config.window_height/2],
                     [config.window_width, config.window_height/2], 1)

    desired_fps = 60
    frame_time = 1 / desired_fps
    previous_time = pygame.time.get_ticks()
    accumulator = 0.0

    update(screen, fixed_surface, string)

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


def update(screen, fixed_surface, string):
    screen.blit(fixed_surface, (0, 0))
    string.draw()


def main():
    init()


if __name__ == "__main__":
    main()
