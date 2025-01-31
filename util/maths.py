# TODO:
# position vector -> vector matrix -> draw vector
# velocity vector -> position vector
# acceleration vector -> velocity vector
# vector field (draw arrow)

import math


def compute_acceleration_vector(mass, force, angle):
    Fx = force*math.cos(angle)
    Fy = force*math.sin(angle)
    return [Fx/mass, Fy/mass]


def compute_velocity_vector(velocity, acceleration):
    return [v + a for v, a in zip(velocity, acceleration)]


def compute_position_vector(position, velocity, frame_time):
    return [p + v*frame_time for p, v in zip(position, velocity)]


def compute_total_acceleration(mass, forces):
    accelerations = [
        compute_acceleration_vector(
            mass, force["mag"], math.radians(force["angle"]))
        for force in forces
    ]
    return list(map(sum, zip(*accelerations)))
