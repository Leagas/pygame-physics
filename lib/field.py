import pygame
from util.maths import compute_field


class Field:
    screen: pygame.Surface = None
    density: int
    matrix: list

    def __init__(self, screen, density):
        self.screen = screen
        self.density = density
        self.matrix = compute_field(density)

    def draw(self):
        x_o = 0
        y_o = 0
        for p in self.matrix:
            center = [x_o+p[0], y_o+p[1]]
            pygame.draw.circle(self.screen, (0, 0, 0), center, 1, 1)
