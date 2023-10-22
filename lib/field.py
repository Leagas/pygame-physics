import pygame
from util.maths import compute_field
from util.util import line_length, vector_angle, draw_vector


class Field:
    screen: pygame.Surface = None
    density: int
    matrix: list

    def __init__(self, screen, density):
        self.screen = screen
        self.density = density
        self.matrix = compute_field(density)

    def calculate_vector(self, entity, point):
        for e in entity:
            length = line_length(point, [300,300])
            if length <= 200 and length >= 20:
                angle = vector_angle(point, [300,300])
                draw_vector(self.screen, point, angle, length)

    def draw(self, entity):
        x_o = 0
        y_o = 0
        for p in self.matrix:
            point = [x_o+p[0], y_o+p[1]]
            pygame.draw.circle(self.screen, (0,0,0), point, 1, 1)
            self.calculate_vector(entity, point)
