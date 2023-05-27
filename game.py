# @Author: indoctrinatedrecluse
# @Date:   2023-05-26 00:00:00


# The idea here is to make a collision game where there is a ball and the player will
# have a paddle to hit the ball. The ball will bounce off the paddle and the walls.
# The player will have to move the paddle to hit the ball and prevent it from hitting
# the bottom of the screen. If the ball hits the bottom of the screen, the game is over.
# The player will have 3 lives to play the game. If the player loses all 3 lives, the
# game is over. The player will have to press the space bar to start the game. The
# player will have to press the space bar to restart the game after the game is over.
# The player will have to press the space bar to pause the game. The player will have
# to press the space bar to resume the game. The player will have to press the escape
# key to quit the game. The player will have to press the left and right arrow keys to
# move the paddle left and right. The player will have to press the up and down arrow
# keys to move the paddle up and down.

# The game will be made using the pygame module.

# Import the pygame and math modules.
import pygame, math
# Import the locals module from the pygame module.
# from pygame.locals import *
# Import the font module from the pygame module.
from pygame import font

# Helper functions
# Vector maths functions
# Magnitude of a vector
def magnitude(v):
    return math.sqrt(sum(v[i]*v[i] for i in range(len(v))))
# Add two vectors
def add(u, v):
    return [ u[i]+v[i] for i in range(len(u)) ]
# Normalize a vector
def normalize(v):
    vmag = magnitude(v)
    return [ v[i]/vmag  for i in range(len(v)) ]

# Initialize pygame.
pygame.init()
# Initialize pygame font.
pygame.font.init()

# Constants
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Paddle dimensions
PADDLE_WIDTH = 50
PADDLE_HEIGHT = 20
# Ball radius
BALL_RADIUS = 10
# Paddle movement speed
PADDLE_SPEED = 20
# Ball movement direction
BALL_VELOCITY_X = 1
BALL_VELOCITY_Y = 1
# Lives
LIVES = 3
# Ball coordinates (x, y): initially, the ball will be at the center of the screen.
BALL_X = SCREEN_WIDTH / 2
BALL_Y = SCREEN_HEIGHT / 2
# Paddle coordinates (x, y): initially, the paddle will be at the bottom middle of the screen.
PADDLE_X = SCREEN_WIDTH / 2
PADDLE_Y = SCREEN_HEIGHT - PADDLE_HEIGHT
# Frame limit for keypress updates
FRAME_LIMIT = 10

# Create a game window.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the game window.
pygame.display.set_caption("Jardinians")

# Create a list of sprites that will be used in the game.
sprites = pygame.sprite.Group()

# Create a game clock.
clock = pygame.time.Clock()

# Create a game loop.
running = True
move_ticker = 0
while running:
    
        # Check for events.
        for event in pygame.event.get():
    
            # Check if the user wants to quit the game.
            if event.type == pygame.QUIT:
                running = False
            
            # Check if the user wants to move the paddle, and continuously move the paddle as long as the user is pressing the arrow keys.
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                if move_ticker == 0:
                    move_ticker = FRAME_LIMIT
                # Move the paddle left.
                PADDLE_X -= PADDLE_SPEED
            if keys[pygame.K_RIGHT]:
                if move_ticker == 0:
                    move_ticker = FRAME_LIMIT
                # Move the paddle right.
                PADDLE_X += PADDLE_SPEED
            if keys[pygame.K_UP]:
                if move_ticker == 0:
                    move_ticker = FRAME_LIMIT
                # Move the paddle up.
                PADDLE_Y -= PADDLE_SPEED
            if keys[pygame.K_DOWN]:
                if move_ticker == 0:
                    move_ticker = FRAME_LIMIT
                # Move the paddle down.
                PADDLE_Y += PADDLE_SPEED
            
            # Check if the user wants to pause the game.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Pause the game.
                    pass

        # Game logic.

        # Get the screen rect.
        screen_rect = screen.get_rect()

        # Define the paddle as a red rectangle with the paddle dimensions and coordinates.
        paddle = pygame.Rect(PADDLE_X, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT)

        # Move the ball.
        BALL_X += BALL_VELOCITY_X
        BALL_Y += BALL_VELOCITY_Y

        # If the user is pressing the arrow keys, decrement the move ticker.
        if move_ticker > 0:
            move_ticker -= 1

        # Check if the paddle is within the screen.
        if not screen_rect.contains(paddle):
            # Move the paddle back into the screen.
            paddle.clamp_ip(screen_rect)

        # Check if the ball has hit the left, right or top wall.
        if BALL_X <= BALL_RADIUS or BALL_X >= SCREEN_WIDTH - BALL_RADIUS:
            BALL_VELOCITY_X *= -1
        if BALL_Y <= BALL_RADIUS:
            BALL_VELOCITY_Y *= -1

        # Check if the ball has hit the paddle, and if it has, invert the ball's direction.
        if paddle.collidepoint(BALL_X, BALL_Y):
            BALL_VELOCITY_Y *= -1

        # Check if the ball has hit the bottom wall.
        if BALL_Y >= SCREEN_HEIGHT - BALL_RADIUS:
            # The player loses a life.
            LIVES -= 1
            # Reset the ball coordinates.
            BALL_X = SCREEN_WIDTH / 2
            BALL_Y = SCREEN_HEIGHT / 2
            # Reset the paddle coordinates.
            PADDLE_X = SCREEN_WIDTH / 2
            PADDLE_Y = SCREEN_HEIGHT - PADDLE_HEIGHT
            # Reset the ball velocity.
            BALL_VELOCITY_X = 1
            BALL_VELOCITY_Y = 1

        # Check if the player has lost all lives.
        if LIVES == 0:
            """
            # Create a sprite for the game over message.
            game_over_message = pygame.sprite.Sprite()
            # Set the image of the game over message.
            game_over_message.image = pygame.image.load("game_over.png").convert_alpha()
            # Set the rect of the game over message.
            game_over_message.rect = game_over_message.image.get_rect()
            # Set the coordinates of the game over message.
            game_over_message.rect.x = SCREEN_WIDTH / 2 - game_over_message.rect.width / 2
            game_over_message.rect.y = SCREEN_HEIGHT / 2 - game_over_message.rect.height / 2
            # Add the game over message to the list of sprites.
            sprites.add(game_over_message) """
            # The game is over.
            running = False


        # Drawing code.

        # Set the backround as background.jpg from the assets folder.
        background = pygame.image.load("assets/background.jpg").convert()
        screen.blit(background, (0, 0))
        # Draw a 1 px thick black line at the bottom of the screen to denote the failure line.
        pygame.draw.line(screen, BLACK, (0, SCREEN_HEIGHT - 1), (SCREEN_WIDTH, SCREEN_HEIGHT - 1), 1)
        # Draw the paddle using the paddle rect object.
        pygame.draw.rect(screen, RED, paddle)
        # Draw the ball using the ball radius and coordinates.
        pygame.draw.circle(screen, BLUE, (BALL_X, BALL_Y), BALL_RADIUS)
        # Draw the lives text at the top right corner of the screen.
        font = pygame.font.SysFont("Arial", 20)
        lives_text = font.render("Lives: " + str(LIVES), True, WHITE)
        screen.blit(lives_text, (SCREEN_WIDTH - lives_text.get_width() - 10, 10))
    
        # Update the game window.
        pygame.display.update()
    
        # Set the game clock to 60 FPS.
        clock.tick(60)

# Quit the game.
pygame.quit()