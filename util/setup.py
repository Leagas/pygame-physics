import pygame
import constant as config
from lib.entity import Entity


class Container:
    screen: pygame.Surface = None
    entity: list = []

    def __init__(self, screen) -> None:
        entity = Entity(screen, [300, 300], 2)
        self.entity = [entity]
        self.screen = screen
        setup(self.screen)

    def update(self, frame_time):
        self.screen.fill(config.window_background)
        for e in self.entity:
            e.draw()
            e.update(frame_time)


def setup(screen: pygame.Surface):
    screen.fill(config.window_background)
