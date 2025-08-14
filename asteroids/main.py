import pygame
from shot import Shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # Initialize Pygame
    pygame.init()
    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Delta time tracker
    dt = 0

    # --- Sprite groups for game object management ---
    updatable = pygame.sprite.Group()  # Objects that need to be updated every frame
    drawable = pygame.sprite.Group()   # Objects that need to be drawn every frame
    asteroids = pygame.sprite.Group()  # All asteroid objects
    shots = pygame.sprite.Group()      # All player-fired shots

    # Assign containers so new instances auto-add themselves to groups
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    # Create player at center of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Spawn initial asteroid field
    asteroid_field = AsteroidField()

    # Remove any asteroids that spawn too close to the player (safe zone)
    for a in list(asteroids):
        if a.position.distance_to(player.position) < 200:
            a.kill()

    # Draw an initial black frame so the window is visible immediately
    screen.fill("black")
    pygame.display.flip()

    # --- Main Game Loop ---
    while True:
        # Handle input/events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game

        # Update all updatable objects with delta time
        for obj in updatable:
            obj.update(dt)

        # Collision check: Player vs Asteroids
        for a in asteroids:
            if player.collision(a):
                print("Game over!")
                return
        
        # Collision check: Shots vs Asteroids
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()           # Remove the shot
                    result = asteroid.split()  # Split asteroid into smaller ones
                    if result:            # If asteroid splits, add new pieces
                        asteroids.add(result[0])
                        asteroids.add(result[1])

        # Draw everything
        screen.fill("black")  # Clear screen
        for obj in drawable:
            obj.draw(screen)  # Draw each drawable object
        pygame.display.flip() # Update the display

        # Cap the framerate to 60 FPS and get time since last frame (seconds)
        dt = clock.tick(60) / 1000

# Run the game if executed directly
if __name__ == "__main__":
    main()


