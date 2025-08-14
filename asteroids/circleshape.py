import pygame

# Base class for all circular game objects (player, asteroids, shots, etc.)
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        """
        Initialize a circular game object.
        - (x, y): initial position
        - radius: circle radius for drawing & collision
        """
        # Add to sprite groups if 'containers' attribute exists
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        # Position & movement
        self.position = pygame.Vector2(x, y)  # Current position
        self.velocity = pygame.Vector2(0, 0)  # Movement vector
        self.radius = radius                  # Size of the circle

    def draw(self, screen):
        """
        Placeholder method for drawing.
        Must be overridden in subclasses.
        """
        pass

    def update(self, dt):
        """
        Placeholder method for updating object state each frame.
        Must be overridden in subclasses.
        """
        pass

    def collision(self, circleshape):
        """
        Check collision with another CircleShape object.
        Returns True if the distance between centers <= sum of radii.
        """
        distance = self.position.distance_to(circleshape.position)
        return distance <= self.radius + circleshape.radius
