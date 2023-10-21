import pygame
from util.maths import compute_matrix, compute_velocity


class Entity:
    screen: pygame.Surface = None
    position: list = []
    matrix: list = []
    force: list = []
    vector: list = []
    velocity: list = []

    def __init__(self, screen, position, velocity, force, mass):
        self.screen = screen
        self.position = position
        self.force = force
        self.mass = mass
        self.matrix = compute_matrix(position)
        self.velocity = compute_velocity(velocity, force, mass)

    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.velocity = compute_velocity(self.velocity, self.force, self.mass)
        self.matrix = compute_matrix(self.position)

    def draw(self):
        pygame.draw.lines(self.screen, (255, 0, 0), True, self.matrix, 2)
        self.update()
