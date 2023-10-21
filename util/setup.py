import pygame
import constant as config
from lib.entity import Entity


class Container:
    screen: pygame.Surface = None
    entity: list = []
    field: list = []

    def __init__(self, screen, field) -> None:
        entity = Entity(screen, [300, 300], [1, -3], [1, 1], 10)
        self.entity = [entity]
        self.screen = screen
        self.field = field

    def update(self):
        setup(self.screen)
        for entity in self.entity:
            entity.draw()
            for field in self.field:
                field.apply(entity)


def setup(screen: pygame.Surface):
    screen.fill(config.window_background)
    pygame.draw.line(screen, (0, 0, 0),
                     [config.window_width/2, 0],
                     [config.window_width/2, config.window_height], 1)
    pygame.draw.line(screen, (0, 0, 0),
                     [0, config.window_height/2],
                     [config.window_width, config.window_height/2], 1)
