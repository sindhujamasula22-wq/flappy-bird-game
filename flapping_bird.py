import pygame
import sys
import random

pygame.init()

# Screen
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flapping Bird")
clock = pygame.time.Clock()

# Colors
SKY = (135, 206, 235)
GREEN = (0, 200, 0)
GROUND = (222, 184, 135)

# Bird
bird_x = 100
bird_y = 300
bird_radius = 15
gravity = 0.6
velocity = 0
jump = -10

# Pipes
pipe_width = 60
pipe_gap = 160
pipe_x = WIDTH
pipe_height = random.randint(150, 350)
pipe_speed = 3
score = 0
passed_pipe = False

ground_y = 550
font = pygame.font.SysFont(None, 40)
game_over = False

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                velocity = jump
            if event.key == pygame.K_r and game_over:
                bird_y = 300
                velocity = 0
                pipe_x = WIDTH
                pipe_height = random.randint(150, 350)
                score = 0
                game_over = False

    if not game_over:
        velocity += gravity
        bird_y += velocity
        pipe_x -= pipe_speed

        if pipe_x + pipe_width < 0:
            pipe_x = WIDTH
            pipe_height = random.randint(150, 350)
            passed_pipe = False

        # Score
        if pipe_x < bird_x and not passed_pipe:
            score += 1
            passed_pipe = True

        # Collision
        if bird_x + bird_radius > pipe_x and bird_x - bird_radius < pipe_x + pipe_width:
            if bird_y - bird_radius < pipe_height or bird_y + bird_radius > pipe_height + pipe_gap:
                game_over = True

        if bird_y + bird_radius >= ground_y or bird_y - bird_radius <= 0:
            game_over = True

    # Draw
    screen.fill(SKY)

    pygame.draw.rect(screen, GREEN, (pipe_x, 0, pipe_width, pipe_height))
    pygame.draw.rect(screen, GREEN, (pipe_x, pipe_height + pipe_gap,
                                     pipe_width, HEIGHT))

    pygame.draw.rect(screen, GROUND, (0, ground_y, WIDTH, HEIGHT))
    pygame.draw.circle(screen, (255, 255, 0),
                       (bird_x, int(bird_y)), bird_radius)

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    if game_over:
        text = font.render("Game Over! Press R", True, (255, 0, 0))
        screen.blit(text, (70, 260))

    pygame.display.update()

pygame.quit()
sys.exit()
