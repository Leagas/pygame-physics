import pygame


class Entity:
    screen: pygame.Surface = None
    radius: int
    field: int
    position: list

    def __init__(self, screen, position, radius):
        self.screen = screen
        self.position = position
        self.radius = radius
        self.field = radius*10

    def draw(self):
        x,y = self.position
        pygame.draw.circle(
            self.screen,
            (0, 0, 0),
            [x, y],
            self.radius
        )
        # pygame.draw.circle(
        #     self.screen,
        #     (0, 0, 0),
        #     [x, y],
        #     self.field,
        #     1
        # )
