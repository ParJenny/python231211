# List
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Set
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Dictionary
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
print("Dictionary:", my_dict)


import os
import random
import time

# 게임 설정
WIDTH = 20
HEIGHT = 10
PADDLE_LENGTH = 3
BALL_CHAR = 'O'
PADDLE_CHAR = '|'
BLOCK_CHAR = '#'
EMPTY_CHAR = ' '

# 게임 상태
ball = {'x': WIDTH // 2, 'y': HEIGHT // 2, 'dx': 1, 'dy': 1}
paddle = {'x': WIDTH // 2, 'y': HEIGHT - 1}

blocks = [{'x': x, 'y': y} for x in range(WIDTH) for y in range(HEIGHT // 2)]

def draw_game():
    os.system('cls' if os.name == 'nt' else 'clear')

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x == ball['x'] and y == ball['y']:
                print(BALL_CHAR, end='')
            elif x == paddle['x'] and y == paddle['y']:
                print(PADDLE_CHAR, end='')
            elif any(block['x'] == x and block['y'] == y for block in blocks):
                print(BLOCK_CHAR, end='')
            else:
                print(EMPTY_CHAR, end='')
        print()

# 게임 루프
while True:
    draw_game()

    # 입력 처리
    key = input("Move paddle left (a) or right (d): ").lower()

    # 패들 이동
    if key == 'a' and paddle['x'] > 0:
        paddle['x'] -= 1
    elif key == 'd' and paddle['x'] < WIDTH - PADDLE_LENGTH:
        paddle['x'] += 1

    # 공 이동
    ball['x'] += ball['dx']
    ball['y'] += ball['dy']

    # 벽 충돌 체크
    if ball['x'] == 0 or ball['x'] == WIDTH - 1:
        ball['dx'] *= -1
    if ball['y'] == 0 or ball['y'] == HEIGHT - 1:
        ball['dy'] *= -1

    # 패들 충돌 체크
    if (
        ball['y'] == paddle['y'] - 1
        and paddle['x'] <= ball['x'] < paddle['x'] + PADDLE_LENGTH
    ):
        ball['dy'] *= -1

    # 블록 충돌 체크
    for block in blocks:
        if ball['x'] == block['x'] and ball['y'] == block['y']:
            blocks.remove(block)
            ball['dy'] *= -1

    # 게임 종료 조건
    if ball['y'] == HEIGHT - 1:
        print("Game Over!")
        break

    if not blocks:
        print("You Win!")
        break

    time.sleep(0.1)  # 프레임 간격

