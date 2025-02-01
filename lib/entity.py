import pygame
from util.maths import compute_total_acceleration, compute_velocity_vector, compute_position_vector, compute_total_impulse


class Entity:
    screen: pygame.Surface = None
    radius: int
    mass: int
    position: list
    acceleration: list
    velocity: list

    def __init__(self, screen, position, mass):
        self.screen = screen
        self.mass = mass
        self.radius = mass*10
        self.forces = []
        self.impulse = []
        self.acceleration = [0, 0],
        self.velocity = [0, 0]
        self.position = position

    def apply_force(self, force):
        self.forces.append(force)

    def apply_impulse(self, force, angle):
        self.impulse.append(force, angle)

    def update(self, frame_time):
        if self.impulse:
            delta_v = compute_total_impulse(self.mass, self.impulse)
            self.velocity = compute_velocity_vector(self.velocity, delta_v)
            self.impulse.clear()

        self.acceleration = compute_total_acceleration(self.mass, self.forces)
        self.velocity = compute_velocity_vector(
            self.velocity, self.acceleration)
        self.position = compute_position_vector(
            self.position, self.velocity, frame_time)

    def draw(self):
        x, y = self.position
        pygame.draw.circle(
            self.screen,
            (0, 0, 0),
            [x, y],
            self.radius
        )
