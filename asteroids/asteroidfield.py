import pygame
import random
from asteroid import Asteroid
from constants import *

class AsteroidField(pygame.sprite.Sprite):
    # Possible spawn edges for asteroids.
    # Each entry contains:
    #   - A base direction vector (for initial movement away from the spawn edge)
    #   - A function to generate a spawn position along that edge
    edges = [
        [  # Spawn from LEFT edge, moving right
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [  # Spawn from RIGHT edge, moving left
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [  # Spawn from TOP edge, moving down
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [  # Spawn from BOTTOM edge, moving up
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        # Add this AsteroidField to its container groups
        pygame.sprite.Sprite.__init__(self, self.containers)
        # Tracks time since last asteroid spawn
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        """
        Create a single asteroid at given position with given radius & velocity.
        """
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        """
        Called every frame. Spawns new asteroids at set intervals.
        dt = time elapsed since last frame (seconds)
        """
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            # Reset timer after spawning
            self.spawn_timer = 0

            # Choose a random edge for asteroid spawn
            edge = random.choice(self.edges)

            # Set asteroid speed & angle variation
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))

            # Get random position along the chosen edge
            position = edge[1](random.uniform(0, 1))

            # Choose random asteroid size multiplier
            kind = random.randint(1, ASTEROID_KINDS)

            # Create the asteroid
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
