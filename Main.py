import pygame
import math
import time
from datetime import datetime

# Constants for Earth's orbital speed calculation
G = 6.674 * (10 ** -11)  # Gravitational constant in m^3 kg^-1 s^-2
M = 1.989 * (10 ** 30)   # Mass of the Sun in kg
r = 1.496 * (10 ** 11)   # Average orbital radius of Earth in meters

# Calculate Earth's orbital speed in m/s and convert to km/s
earth_orbital_speed = math.sqrt(G * M / r) / 1000

# Circumference of Earth's orbit in meters
circumference = 2 * math.pi * r

# Time for one orbit in seconds (365.25 days)
orbit_time_seconds = 365.25 * 24 * 60 * 60

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Real-Time Earth's Orbital Speed")

# Colors
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Ball properties
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
CENTER_RADIUS = 50
ORBIT_RADIUS = 150  # Scaled for visualization
ORBIT_BALL_RADIUS = 20

# Orbit properties
start_date = datetime(2024, 12, 25)  # Starting date: 1st August
current_date = datetime.now()
elapsed_days = (current_date - start_date).total_seconds()

# Font for displaying text
font = pygame.font.Font(None, 36)

# Clock for controlling the frame rate
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Draw the central ball (yellow outline, transparent center)
    pygame.draw.circle(screen, YELLOW, (CENTER_X, CENTER_Y), CENTER_RADIUS, 3)

    # Calculate the current angle based on elapsed days since 1st August
    angle = (elapsed_days / orbit_time_seconds) * 2 * math.pi

    # Calculate orbiting ball position
    orbit_x = CENTER_X + ORBIT_RADIUS * math.cos(angle)
    orbit_y = CENTER_Y + ORBIT_RADIUS * math.sin(angle)

    # Draw the orbiting ball
    pygame.draw.circle(screen, GREEN, (int(orbit_x), int(orbit_y)), ORBIT_BALL_RADIUS, 3)

    # Display Earth's orbital speed
    speed_text = font.render(f"Earth's Orbital Speed: {earth_orbital_speed:.2f} km/s", True, WHITE)
    screen.blit(speed_text, (20, 20))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
