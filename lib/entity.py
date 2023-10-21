import pygame
from util.maths import compute_matrix, compute_velocity


class Entity:
    screen: pygame.Surface = None
    radius: int

    def __init__(self, screen, radius):
        self.screen = screen
        self.radius = radius

    def draw(self):
        pygame.draw.circle(
            self.screen,
            (0, 0, 0),
            [300, 300],
            self.radius
        )
        pygame.draw.circle(
            self.screen,
            (0, 0, 255),
            [300, 300],
            self.radius*10,
            1
        )
