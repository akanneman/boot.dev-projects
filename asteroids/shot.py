from constants import *
import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        # Initialize a shot at given position (x, y) with fixed radius from constants
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        # Draw the shot as a white circle outline on the given screen
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Move the shot based on its velocity and delta time
        # (dt keeps movement consistent regardless of framerate)
        self.position += self.velocity * dt
