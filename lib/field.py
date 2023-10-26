import pygame
import constant as config
from util.util import line_length, vector_angle, draw_vector, distance_ratio


class Field:
    screen: pygame.Surface = None
    density: int
    matrix: list

    def __init__(self, screen, fixed_surface, density):
        self.screen = screen
        self.density = density
        self.matrix = self.compute_field(self.density, fixed_surface)

    def compute_field(self, density, fixed_urface):
        matrix = []
        width = config.window_width
        height = config.window_height
        x_limit = int(width/density)
        y_limit = int(height/density)
        for i in range(1, x_limit):
            for j in range(1, y_limit):
                matrix.append([i*density, j*density, [0, 0]])
                pygame.draw.circle(fixed_urface, (0, 0, 0), [i*density, j*density], 1, 1)
        return matrix

    def calculate_vector(self, entity, p):
        for e in entity:
            x, y, _ = p
            length = line_length([x, y], e.position)
            if length <= e.field and length >= e.radius:
                angle = vector_angle([x, y], e.position)
                magnitude = distance_ratio(length, e)
                p[2] = [angle, magnitude]
            else:
                p[2] = [0,0]

    def draw(self, entity):
        for p in self.matrix:
            x, y, v = p
            self.calculate_vector(entity, p)
            angle, magnitude = p[2]
            if magnitude > 0:
                draw_vector(self.screen, [x, y], angle, magnitude)
