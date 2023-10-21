square = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1]
]

# TODO:
# position vector
# velocity vector (updates position)
# acceleration vector (updates velocity)
# apply field effect


class Gravity:
    force: list = [0, 9.81]

    def __init__(self, force):
        self.force = force

    def apply(self, entity):
        velocity = compute_velocity([0, 1], self.force, entity.mass)
        # entity.velocity[0] += velocity[0]
        # entity.velocity[1] += velocity[1]
        print('g vel', velocity)


def compute_matrix(position):
    entity_vector = []
    v_x = position[0]
    v_y = position[1]
    for vector in square:
        entity_vector.append([v_x, v_y])
        v_x += vector[0]*100
        v_y -= vector[1]*100
    return entity_vector


def compute_velocity(vector, force, mass):
    a_x = force[0]/mass
    a_y = force[1]/mass
    return [vector[0] + vector[0]*a_x, vector[1] + vector[1]*a_y]
