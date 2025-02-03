import pygame
from util.maths import compute_total_acceleration, compute_velocity_vector, compute_position_vector, compute_total_impulse
from util.util import line_length


class Entity:
    screen: pygame.Surface = None
    radius: int
    mass: int
    position: list
    acceleration: list
    velocity: list

    def __init__(self, screen, position, mass, radius, field):
        self.screen = screen
        self.mass = mass
        self.radius = radius
        self.forces = []
        self.impulse = []
        self.acceleration = [0, 0],
        self.velocity = [0, 0]
        self.position = position
        self.field = field

    def apply_force(self, entities):
        forces = []
        for e in entities:
            if e != self:
                distance = line_length(self.position, e.position)
                if distance < e.field:
                    forces.append([20, 90])
        self.forces = forces

    def apply_impulse(self, entities):
        for e in entities:
            if e != self:
                distance = line_length(self.position, e.position)
                if distance < self.radius + e.radius:
                    self.impulse.append([200, -90])

    def compute_force(self, frame_time):
        self.acceleration = compute_total_acceleration(
            self.mass, self.forces)
        self.velocity = compute_velocity_vector(
            self.velocity, self.acceleration, frame_time)
        self.position = compute_position_vector(
            self.position, self.velocity, frame_time)

    def compute_impulse(self, frame_time):
        delta_v = compute_total_impulse(self.mass, self.impulse)
        self.velocity = compute_velocity_vector(
            self.velocity, delta_v, frame_time)
        self.impulse.clear()

    def update(self, entities, frame_time):
        self.apply_force(entities)
        self.apply_impulse(entities)
        if self.impulse:
            self.compute_impulse(frame_time)
        self.compute_force(frame_time)

    def draw(self):
        x, y = self.position
        pygame.draw.circle(
            self.screen,
            (0, 0, 0),
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
