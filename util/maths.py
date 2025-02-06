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


def compute_impulse_vector(object1):
    # e = -0.9
    # total_mass = object1.mass + object2.mass
    # r_vx = (object1.velocity[0] - object2.velocity[0])
    # r_vy = (object1.velocity[1] - object2.velocity[1])
    # v1x = e*object2.mass*r_vx / total_mass
    # v1y = e*object2.mass*r_vy / total_mass
    # v2x = e*object1.mass*r_vx / total_mass
    # v2y = e*object1.mass*r_vy / total_mass
    # return [v1x, v1y], [v2x, v2y]
    e = -0.9
    vx = object1.velocity[0]
    vy = e*object1.velocity[1]
    return [vx, vy]
