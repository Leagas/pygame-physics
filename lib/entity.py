import pygame
from util.maths import compute_total_acceleration, compute_velocity_vector, compute_position_vector


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
        self.forces = [
            {
                "mag": 100,
                "angle": 0
            }
        ]
        self.acceleration = [0, 0],
        self.velocity = [0, 0]
        self.position = position

    def apply_force(self, force):
        self.forces.append(force)

    def update(self, frame_time):
        d_acceleration = compute_total_acceleration(self.mass, self.forces)
        d_velocity = compute_velocity_vector(self.velocity, d_acceleration)
        d_position = compute_position_vector(
            self.position, d_velocity, frame_time)
        self.position = d_position

    def draw(self):
        x, y = self.position
        pygame.draw.circle(
            self.screen,
            (0, 0, 0),
            [x, y],
            self.radius
        )
