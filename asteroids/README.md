# Asteroids Game (Boot.dev Project)

A simple clone of the classic arcade game **Asteroids**, built with [Pygame](https://www.pygame.org/).  
This project was completed as part of the Boot.dev game development course.

## Gameplay
- Control your spaceship, avoid asteroids, and shoot them to score points.
- Larger asteroids split into smaller ones when destroyed.
- Survive as long as possible without colliding with asteroids.

## Controls
- **Left / Right Arrow Keys** – Rotate the ship
- **Up Arrow** – Thrust forward
- **Spacebar** – Fire bullets
- **Esc** – Quit the game

## Requirements
- Python 3.12+
- Pygame 2.5+
- (Optional) A virtual environment for dependency management

## How to Run
```bash
# Install dependencies
pip install -r requirements.txt

# Clone this repository
git clone https://github.com/YOUR_USERNAME/boot.dev-projects.git
cd boot.dev-projects/asteroids

# Run the game
python main.py

Project Structure
asteroids/
├── asteroid.py
├── asteroidfield.py
├── circleshape.py
├── constants.py
├── main.py
├── player.py
├── shot.py
└── ...
