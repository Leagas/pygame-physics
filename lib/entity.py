import pygame
import sys
from util.maths import compute_total_acceleration, compute_velocity_vector, compute_position_vector
from util.util import line_length

'''
TODO:
 1. Calculate change in velocity after collision
    - calculate applied impulse using impulse momentum theorem
    - calculate angle of force vector
'''


class Entity:
    screen: pygame.Surface = None
    radius: int
    mass: int
    position: list
    acceleration: list
    velocity: list

    def __init__(self, screen, position, mass, radius, field, color):
        self.screen = screen
        self.mass = mass
        self.radius = radius
        self.forces = [
            [98, 90]
        ]
        self.impulse = []
        self.acceleration = [0, 0],
        self.velocity = [0, 0]
        self.position = position
        self.field = field
        self.color = color

    def compute_force(self, frame_time):
        self.acceleration = compute_total_acceleration(
            self.mass, self.forces)
        self.velocity = compute_velocity_vector(
            self.velocity, self.acceleration, frame_time)

    def detect_collision(self):
        distance = line_length([500, 1000], self.position)
        if (distance < self.radius):
            self.acceleration = [0, -1 * self.acceleration[1] * 0.9]
            self.velocity = [0, -1 * self.velocity[1] * 0.9]
            self.position[1] = 1000 - self.radius

    def update(self, frame_time):
        self.compute_force(frame_time)
        self.detect_collision()
        self.position = compute_position_vector(
            self.position, self.velocity, frame_time)

    def draw(self):
        x, y = self.position
        pygame.draw.circle(
            self.screen,
            (self.color, 0, 0),
            [x, y],
            self.radius
        ),
        pygame.draw.circle(
            self.screen,
            (0, 0, 255),
            [x, y],
            self.field,
            1
        )
