import pygame
import constant as config
from lib.field import Field
from lib.entity import Entity


class Container:
    screen: pygame.Surface = None
    entity: list = []
    field: list = []

    def __init__(self, screen, fixed_surface) -> None:
        field = Field(screen, fixed_surface, 10)
        entity1 = Entity(screen, [300,300], 20)
        # entity2 = Entity(screen, [250,250], 5)
        self.entity = [entity1]
        self.field = [field]
        self.screen = screen

    def update(self, fixed_surface):
        self.screen.blit(fixed_surface, (0, 0))
        for e in self.entity:
            e.draw()
        for f in self.field:
            f.draw(self.entity)


    def setup(self, fixed_surface: pygame.Surface):
        pygame.draw.line(fixed_surface, (0, 0, 0),
                        [config.window_width/2, 0],
                        [config.window_width/2, config.window_height], 1)
        pygame.draw.line(fixed_surface, (0, 0, 0),
                        [0, config.window_height/2],
                        [config.window_width, config.window_height/2], 1)
