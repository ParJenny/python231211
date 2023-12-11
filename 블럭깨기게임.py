# 블럭깨기게임.py

import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
FPS = 60

# 색깔
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 파드, 공, 블록 설정
PADDLE_WIDTH, PADDLE_HEIGHT = 200, 10
BALL_RADIUS = 10
BLOCK_WIDTH, BLOCK_HEIGHT = 80, 30
BLOCK_ROWS = 5
BLOCK_COLS = 10

# 게임 화면
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블록 깨기 게임")

# 시계
clock = pygame.time.Clock()

# 함수
def draw_paddle(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, PADDLE_WIDTH, PADDLE_HEIGHT])

def draw_ball(x, y):
    pygame.draw.circle(screen, WHITE, (x, y), BALL_RADIUS)

def draw_block(x, y):
    pygame.draw.rect(screen, RED, [x, y, BLOCK_WIDTH, BLOCK_HEIGHT])

# 게임 변수
paddle_x = (WIDTH - PADDLE_WIDTH) // 2
paddle_y = HEIGHT - PADDLE_HEIGHT - 10
paddle_speed = 8

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5 * random.choice([1, -1])
ball_speed_y = -5

blocks = []
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        block_x = col * (BLOCK_WIDTH + 5) + 50
        block_y = row * (BLOCK_HEIGHT + 5) + 50
        blocks.append((block_x, block_y))

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH:
        paddle_x += paddle_speed

    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 벽 충돌 체크
    if ball_x <= 0 or ball_x >= WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y

    # 패들 충돌 체크
    if (
        paddle_x <= ball_x <= paddle_x + PADDLE_WIDTH
        and paddle_y <= ball_y <= paddle_y + PADDLE_HEIGHT
    ):
        ball_speed_y = -ball_speed_y

    # 블록 충돌 체크
    for block in blocks:
        block_x, block_y = block
        if (
            block_x <= ball_x <= block_x + BLOCK_WIDTH
            and block_y <= ball_y <= block_y + BLOCK_HEIGHT
        ):
            ball_speed_y = -ball_speed_y
            blocks.remove(block)

    # 화면 그리기
    screen.fill(BLACK)
    draw_paddle(paddle_x, paddle_y)
    draw_ball(int(ball_x), int(ball_y))
    for block in blocks:
        draw_block(block[0], block[1])

    pygame.display.flip()
    clock.tick(FPS)
