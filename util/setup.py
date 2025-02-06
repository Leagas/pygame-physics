import pygame
import constant as config
from lib.entity import Entity


class Container:
    def __init__(self, screen) -> None:
        self.screen = screen
        entity1 = Entity(screen, [500, 800], 10, 20, 0, 255)
        self.entity = [entity1]

    def update(self, frame_time):
        self.screen.fill(config.window_background)
        for e in self.entity:
            e.draw()
            e.update(frame_time)
