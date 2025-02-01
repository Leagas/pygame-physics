import pygame
import constant as config
from lib.entity import Entity


class Container:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.entity = [Entity(screen, [500, 500], 10)]

    def update(self, frame_time):
        self.screen.fill(config.window_background)
        for e in self.entity:
            e.draw()
            e.update(frame_time)
