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

def draw_vector(screen, point1, angle, length):
    distance = length-20
    red = int(255-distance)
    green = int(255-red)
    x1, y1 = point1
    x2 = 5*(math.cos(angle))
    y2 = 5*(math.sin(angle))
    point2 = [x1+x2, y1+y2]
    pygame.draw.line(screen, (red,green,0), point1, point2, 2)

# rotate vector
# def draw_vector(start, angle):
#     rad = math.radians(angle)*-1
#     x = 50*(math.cos(rad))
#     y = 50*(math.sin(rad))
#     end = [start[0] + x, start[1] + y]
#     return end

# get angle of vector
# angle_radians = math.atan2(delta_y, delta_x)
