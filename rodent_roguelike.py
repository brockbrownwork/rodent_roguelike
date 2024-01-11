import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for the game window
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (150, 150, 150)  # A light grey color

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jumping Man Game')

# Player class with added horizontal movement functionality
class Player:
    def __init__(self):
        self.x = 100
        self.y = 300
        self.width = 40
        self.height = 60
        self.color = (0, 128, 255)  # Blue color
        self.velocity = 5
        self.jump_count = 10
        self.is_jumping = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def jump(self):
        if self.is_jumping:
            if self.jump_count >= -10:
                neg = 1 if self.jump_count > 0 else -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10

    def move(self, keys):
        if keys[pygame.K_a] and self.x > self.velocity:  # Changed to 'A' key
            self.x -= self.velocity
        if keys[pygame.K_d] and self.x < SCREEN_WIDTH - self.width - self.velocity:  # Changed to 'D' key
            self.x += self.velocity

# Create a player instance
player = Player()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for key presses
    keys = pygame.key.get_pressed()
    
    # Move the player based on WASD key presses
    player.move(keys)

    # Enable jumping when 'W' key is pressed
    if keys[pygame.K_w]:  # Changed to 'W' key
        player.is_jumping = True

    # Update the player
    player.jump()

    # Drawing
    screen.fill(BG_COLOR)
    player.draw(screen)
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
