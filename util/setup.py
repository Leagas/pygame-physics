import math
import pygame
import constant as config
from lib.field import Field
from lib.entity import Entity


class Container:
    screen: pygame.Surface = None
    entity: list = []
    field: list = []

    def __init__(self, screen) -> None:
        field = Field(screen, 20)
        entity1 = Entity(screen, [300, 300], 20)
        entity2 = Entity(screen, [200, 200], 10)
        self.entity = [entity1, entity2]
        self.field = [field]
        self.screen = screen
        setup(self.screen)

    def update(self):
        for e in self.entity:
            e.draw()
        for f in self.field:
            f.draw(self.entity)


def setup(screen: pygame.Surface):
    screen.fill(config.window_background)
    pygame.draw.line(screen, (0, 0, 0),
                     [config.window_width/2, 0],
                     [config.window_width/2, config.window_height], 1)
    pygame.draw.line(screen, (0, 0, 0),
                     [0, config.window_height/2],
                     [config.window_width, config.window_height/2], 1)
