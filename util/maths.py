import constant as config

square = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1]
]

# TODO:
# position vector -> vector matrix -> draw vector
# velocity vector -> position vector
# acceleration vector -> velocity vector
# vector field (draw arrow)


def compute_field(density):
    matrix = []
    width = config.window_width
    height = config.window_height
    x_limit = int(width/density)
    y_limit = int(height/density)
    for i in range(1, x_limit):
        for j in range(1, y_limit):
            matrix.append([i*density, j*density])
    return matrix


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
