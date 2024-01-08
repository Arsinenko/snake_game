import pygame
import random

pygame.init()


def msg(text:str, color, x:int, y:int):
    screen.fill(pygame.Color("black"))
    font = pygame.font.SysFont("comicsansms", 30)
    screen.blit(font.render(text, True, color), (x, y))
    pygame.display.update()
    pygame.time.delay(3000)


RES = 600
SIZE = 20
screen = pygame.display.set_mode((RES, RES))
pygame.display.set_caption("Snake")

X_pos = random.randrange(0, RES, SIZE)
Y_pos = random.randrange(0, RES, SIZE)
apple = random.randrange(0, RES, SIZE),  random.randrange(0, RES, SIZE)
snake = [(X_pos, Y_pos)]
snake_length = 1
dx, dy = 0, 0
fps = 10
clock = pygame.time.Clock()
score = 0

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    if X_pos < 0 or X_pos > RES - SIZE or Y_pos < 0 or Y_pos > RES:
        msg(f"Game over! score:{score}", pygame.Color("green"), 200, 200)
        game_over = True
    if len(snake) != len(set(snake)):
        msg(f"Game over! score:{score}", pygame.Color("green"), 200, 200)
        game_over = True
    screen.fill(pygame.Color("black"))

    [pygame.draw.rect(screen, pygame.Color("green"), (i, j, SIZE, SIZE)) for i, j in snake]
    pygame.draw.rect(screen, pygame.Color("red"), (apple[0], apple[1], SIZE, SIZE))
    font = pygame.font.SysFont("comicsansms", 25)
    screen.blit(font.render(f"Score: {score}", True, pygame.Color("white")), (0, 0))

    X_pos += dx * SIZE
    Y_pos += dy * SIZE
    snake.append((X_pos, Y_pos))

    if (X_pos, Y_pos) == apple:
        apple = random.randrange(0, RES, SIZE), random.randrange(0, RES, SIZE)
        snake_length += 1
        score += 1
    snake = snake[-snake_length:]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dx, dy = -1, 0
    if keys[pygame.K_RIGHT]:
        dx, dy = 1, 0
    if keys[pygame.K_DOWN]:
        dx, dy = 0, 1
    if keys[pygame.K_UP]:
        dx, dy = 0, -1

    pygame.display.update()
    clock.tick(fps)