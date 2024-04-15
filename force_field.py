import pygame
import math
import constant as config
from util.util import line_length, vector_angle, draw_vector, distance_ratio
from lib.entity import Entity


class Field:
    screen: pygame.Surface = None
    density: int
    matrix: list
    fixed_surface: pygame.Surface = None

    def __init__(self, screen, fixed_surface, density):
        self.screen = screen
        self.density = density
        self.fixed_surface = fixed_surface
        self.matrix = self.compute_field(self.density, fixed_surface)

    def compute_field(self, density, fixed_surface):
        matrix = []
        width = config.window_width
        height = config.window_height
        x_limit = int(width/density)
        y_limit = int(height/density)
        for i in range(1, x_limit):
            for j in range(1, y_limit):
                matrix.append([i*density, j*density, [0, 0]])
                pygame.draw.circle(fixed_surface, (0, 0, 0), [
                                   matrix[-1][0], matrix[-1][1]], 1, 1)
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
                p[2] = [0, 0]

    def draw(self, entity):
        for p in self.matrix:
            x, y, v = p
            self.calculate_vector(entity, p)
            angle, magnitude = p[2]
            if magnitude > 0:
                # draw_vector(self.screen, [x, y], angle, magnitude)
                x2 = magnitude*(math.cos(angle))
                y2 = magnitude*(math.sin(angle))
                p[0] = x-x2
                p[1] = y-y2
        self.update()

    def update(self):
        self.fixed_surface.fill((255, 255, 255))
        for p in self.matrix:
            x, y, v = p
            pygame.draw.circle(self.fixed_surface, (0, 0, 0), [
                x, y], 1, 1)


class Container:
    screen: pygame.Surface = None
    entity: list = []
    field: list = []

    def __init__(self, screen, fixed_surface) -> None:
        field0 = Field(screen, fixed_surface, 10)
        # field1 = Field(screen, fixed_surface, 10)
        entity = Entity(screen, [250, 250], 5)
        self.entity = [entity]
        self.field = [field0]
        self.screen = screen

    def update(self, fixed_surface):
        self.screen.blit(fixed_surface, (0, 0))
        for e in self.entity:
            e.draw()
        for f in self.field:
            f.draw(self.entity)


def init():
    pygame.init()
    screen = pygame.display.set_mode(
        (config.window_width, config.window_height))
    screen.fill((255, 255, 255))

    fixed_surface = pygame.Surface((config.window_width, config.window_height))
    fixed_surface.fill((255, 255, 255))

    desired_fps = 60
    frame_time = 1 / desired_fps
    previous_time = pygame.time.get_ticks()
    accumulator = 0.0

    container = Container(screen, fixed_surface)

    running = True
    while running:
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - previous_time) / 1000.0
        previous_time = current_time
        accumulator += elapsed_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        while accumulator >= frame_time:
            accumulator -= frame_time
            container.update(fixed_surface)

        pygame.display.flip()

    pygame.quit()


def update(screen, fixed_surface, string):
    screen.blit(fixed_surface, (0, 0))
    string.draw()


def main():
    init()


if __name__ == "__main__":
    main()
