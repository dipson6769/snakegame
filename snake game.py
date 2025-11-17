import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake settings
snake_size = 10
snake_speed = 15

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, GREEN, [x, y, snake_size, snake_size])

def game_loop():
    game_over = False

    x = WIDTH // 2
    y = HEIGHT // 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    food_x = random.randrange(0, WIDTH - snake_size, snake_size)
    food_y = random.randrange(0, HEIGHT - snake_size, snake_size)

    while True:
        while game_over:
            screen.fill(BLACK)
            msg = font.render("Game Over! Press R to Restart or Q to Quit", True, RED)
            screen.blit(msg, (50, HEIGHT // 2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_r:
                        return game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    x_change = 0
                    y_change = -snake_size
                elif event.key == pygame.K_DOWN and y_change == 0:
                    x_change = 0
                    y_change = snake_size

        x += x_change
        y += y_change

        # Check boundaries (game over)
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over = True

        screen.fill(BLACK)

        # Draw food
        pygame.draw.rect(screen, RED, [food_x, food_y, snake_size, snake_size])

        # Snake movement
        snake_list.append((x, y))
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Snake hits itself
        if (x, y) in snake_list[:-1]:
            game_over = True

        draw_snake(snake_list)

        # Check if snake eats food
        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - snake_size, snake_size)
            food_y = random.randrange(0, HEIGHT - snake_size, snake_size)
            snake_length += 1

        pygame.display.update()
        clock.tick(snake_speed)

game_loop()
