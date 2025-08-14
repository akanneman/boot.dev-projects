# --- Screen Dimensions ---
SCREEN_WIDTH = 1280   # Width of the game window in pixels
SCREEN_HEIGHT = 720   # Height of the game window in pixels

# --- Asteroid Settings ---
ASTEROID_MIN_RADIUS = 20         # Smallest asteroid size
ASTEROID_KINDS = 3               # Number of asteroid size levels (large, medium, small)
ASTEROID_SPAWN_RATE = 0.8        # Seconds between asteroid spawns
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS  # Largest asteroid size

# --- Player Settings ---
PLAYER_RADIUS = 20       # Size of the player's ship (collision circle)
PLAYER_TURN_SPEED = 300  # Rotation speed in degrees per second
PLAYER_SPEED = 200       # Forward movement speed in pixels per second

# --- Shot Settings ---
SHOT_RADIUS = 5                # Size of each projectile
PLAYER_SHOOT_SPEED = 500       # Speed of projectiles in pixels per second
PLAYER_SHOOT_COOLDOWN = 0.3    # Seconds between allowed shots
