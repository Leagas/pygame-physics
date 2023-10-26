import pygame
import math

class Entity:
    screen: pygame.Surface = None
    radius: int
    length: int
    field: int
    position: list
    angle: int

    def __init__(self, screen, position, length):
        self.screen = screen
        self.position = position
        self.length = length
        self.radius = 5
        self.angle = math.radians(90)

    def calculate(self, i):
        x,y = self.position
        magnitude = i*self.length
        x2 = magnitude*(math.cos(self.angle))
        y2 = magnitude*(math.sin(self.angle))
        return [x+x2, y+y2]

    def draw(self):
        for i in range(3):
            x,y = self.calculate(i)
            pygame.draw.circle(
                self.screen,
                (0, 0, 0),
                [x, y],
                self.radius
            )
