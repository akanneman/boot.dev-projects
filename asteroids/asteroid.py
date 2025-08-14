import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # Store the asteroid's position as a Vector2 for easy math
        self.position = pygame.math.Vector2(x, y)
        # Velocity vector (default to stationary; set later as needed)
        self.velocity = pygame.math.Vector2(0, 0)
        # Radius of the asteroid (used for size and collision)
        self.radius = radius

    def draw(self, screen):
        """Draw the asteroid as a white circle outline."""
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        """Move the asteroid according to its velocity and delta time."""
        self.position += self.velocity * dt

    def split(self):
        """
        Destroy this asteroid and, if it's big enough, split it into two
        smaller asteroids traveling in slightly different directions.
        """
        self.kill()  # Remove this asteroid from its sprite groups

        # If the asteroid is already at or below the minimum size, don't split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Pick a small random angle to rotate the velocity for the new asteroids
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors rotated in opposite directions
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)

        # New smaller radius (shrink by the minimum asteroid size)
        s_radius = self.radius - ASTEROID_MIN_RADIUS

            # Create smaller asteroids
        new_ast1 = Asteroid(self.position.x, self.position.y, s_radius)
        new_ast1.velocity = vector1 * 1.2

        new_ast2 = Asteroid(self.position.x, self.position.y, s_radius)
        new_ast2.velocity = vector2 * 1.2

        return (new_ast1, new_ast2)
