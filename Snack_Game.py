import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen size
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 200, 0)
red = (200, 0, 0)

# Snake block size
block_size = 10
clock = pygame.time.Clock()
speed = 15

font = pygame.font.SysFont(None, 35)

def show_score(score):
    value = font.render("Score: " + str(score), True, black)
    screen.blit(value, [10, 10])

def game_loop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    dx = 0
    dy = 0

    snake = []
    length = 1

    food_x = random.randrange(0, width - block_size, block_size)
    food_y = random.randrange(0, height - block_size, block_size)

    while not game_over:

        while game_close:
            screen.fill(white)
            msg = font.render("Game Over! Press Q-Quit or C-Play Again", True, red)
            screen.blit(msg, [50, height / 2])
            show_score(length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -block_size
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = block_size
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -block_size
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = block_size
                    dx = 0

        # Move snake
        x += dx
        y += dy

        # Wall collision
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        screen.fill(white)

        # Draw food
        pygame.draw.rect(screen, green, [food_x, food_y, block_size, block_size])

        # Snake body
        head = []
        head.append(x)
        head.append(y)
        snake.append(head)

        if len(snake) > length:
            del snake[0]

        # Self collision
        for segment in snake[:-1]:
            if segment == head:
                game_close = True

        for segment in snake:
            pygame.draw.rect(screen, black, [segment[0], segment[1], block_size, block_size])

        show_score(length - 1)

        pygame.display.update()

        # Food collision
        if x == food_x and y == food_y:
            food_x = random.randrange(0, width - block_size, block_size)
            food_y = random.randrange(0, height - block_size, block_size)
            length += 1

        clock.tick(speed)

    pygame.quit()
    sys.exit()

game_loop()