import math
import pygame

# field strength
# velocity += velocity + (distance/radius)

# get length of line
# if length is less than entity radius
# -> calculate angle of vector
# -> calculate magnitude
# -> draw field vector at point


def line_length(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def vector_angle(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dx = x2-x1
    dy = y2-y1
    return math.atan2(dy, dx)


def draw_vector(screen, point1, angle, magnitude):
    color_ratio = map_color_ratio(magnitude)
    red = color_ratio
    green = 255 - red
    x1, y1 = point1
    # length = 5 + 10 * magnitude
    x2 = x1 + 5 * math.cos(angle)
    y2 = y1 + 5 * math.sin(angle)
    point2 = [x2, y2]
    pygame.draw.line(screen, (red, green, 0), point1, point2, 2)


def distance_ratio(length, entity):
    min_distance = entity.radius
    max_distance = entity.field
    if length <= min_distance:
        return 1.0
    elif length >= max_distance:
        return 0.0
    else:
        # Inverse square law for gravitational-like effect
        return ((max_distance - length) / (max_distance - min_distance)) ** 2


def map_color_ratio(magnitude):
    # Ensure magnitude is between 0 and 1
    magnitude = max(0, min(magnitude, 1))
    return int(magnitude * 255)
