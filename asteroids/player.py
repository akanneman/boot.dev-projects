from shot import Shot
from circleshape import CircleShape
from constants import *
import pygame

print("PLAYER_TURN_SPEED in player.py:", PLAYER_TURN_SPEED)

class Player(CircleShape):
    def __init__(self, x, y):
        # Initialize player at given position with defined radius
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0       # Current facing direction (degrees)
        self.health = 100       # Player health (not yet used in gameplay)
        self.timer = 0          # Shot cooldown timer

    def triangle(self):
        """
        Returns a list of 3 points for drawing the player ship as a triangle.
        - 'forward' vector points in the current rotation direction.
        - 'right' vector is perpendicular to forward, used to get triangle width.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        # Define triangle points based on position and rotation
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # Draw the ship as a white triangle outline
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        """
        Rotates the player ship.
        - dt ensures rotation speed is consistent regardless of framerate.
        - Positive dt rotates clockwise, negative dt rotates counterclockwise.
        """
        rotation_change = PLAYER_TURN_SPEED * dt
        self.rotation += rotation_change

    def update(self, dt):
        """
        Called each frame to handle input and update player state.
        - WASD keys move and rotate the ship
        - SPACE shoots projectiles
        - Cooldown timer prevents firing too fast
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate left
        if keys[pygame.K_d]:
            self.rotate(dt)   # Rotate right
        if keys[pygame.K_w]:
            self.move(dt)     # Move forward
        if keys[pygame.K_s]:
            self.move(-dt)    # Move backward
        if keys[pygame.K_SPACE]:
            self.shoot()      # Fire a shot

        # Update shot cooldown timer
        self.timer = max(0, self.timer - dt)
    
    def move(self, dt):
        """
        Moves the player forward or backward based on rotation.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        """
        Fires a projectile if cooldown timer is ready.
        """
        if self.timer > 0:
            return  # Still cooling down, no shot fired

        # Create new shot at player's current position
        shot = Shot(self.position.x, self.position.y)

        # Set shot velocity in direction of player's rotation
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot.velocity = velocity

        # Reset cooldown timer
        self.timer = PLAYER_SHOOT_COOLDOWN
