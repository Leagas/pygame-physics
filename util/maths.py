import math


def compute_force_vector(mass, force, angle):
    Fx = force*math.cos(angle) / mass
    Fy = force*math.sin(angle) / mass
    return [Fx, Fy]


def compute_velocity_vector(velocity, acceleration, frame_time):
    return [v + a * frame_time for v, a in zip(velocity, acceleration)]


def compute_position_vector(position, velocity, frame_time):
    return [p + v * frame_time for p, v in zip(position, velocity)]


def compute_total_acceleration(mass, forces):
    if not forces:
        return [0, 0]

    delta_acceleration = [
        compute_force_vector(
            mass, force[0], math.radians(force[1]))
        for force in forces
    ]
    return list(map(sum, zip(*delta_acceleration)))
