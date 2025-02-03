import pygame
import constant as config
from lib.entity import Entity


class Container:
    def __init__(self, screen) -> None:
        self.screen = screen
        entity1 = Entity(screen, [500, 401], 10, 20, 60)
        entity2 = Entity(screen, [500, 1000], 100, 200, 600)
        self.entity = [entity1, entity2]

    def update(self, frame_time):
        self.screen.fill(config.window_background)
        for e in self.entity:
            e.draw()
            e.update(self.entity, frame_time)
