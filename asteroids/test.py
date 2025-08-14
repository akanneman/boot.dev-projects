# sanity_window.py
import os, pygame, time
os.environ["SDL_VIDEO_WINDOW_POS"] = "100,100"
os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()
pygame.display.set_caption("Sanity Window")
screen = pygame.display.set_mode((640, 400))
for i in range(120):  # ~2 seconds at 60 FPS
    screen.fill((255, 0, 255) if i % 2 == 0 else (0, 0, 0))  # magenta blink
    pygame.display.flip()
    pygame.time.delay(16)
pygame.quit()
