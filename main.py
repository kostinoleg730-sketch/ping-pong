import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

score_left = 0
score_right = 0

font = pygame.font.SysFont(None, 60)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Пинг-понг")

clock = pygame.time.Clock()

left_paddle_y = 250
right_paddle_y = 250

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100

BALL_SIZE = 15
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_dx = 7
ball_dy = 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Левая ракетка — W/S
    if keys[pygame.K_w]:
        left_paddle_y = left_paddle_y - 5
    if keys[pygame.K_s]:
        left_paddle_y = left_paddle_y + 5

    if left_paddle_y < 0:
        left_paddle_y = 0
    if left_paddle_y > SCREEN_HEIGHT - PADDLE_HEIGHT:
        left_paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT

    # Правая ракетка — стрелки
    if keys[pygame.K_UP]:
        right_paddle_y = right_paddle_y - 5
    if keys[pygame.K_DOWN]:
        right_paddle_y = right_paddle_y + 5

    if right_paddle_y < 0:
        right_paddle_y = 0
    if right_paddle_y > SCREEN_HEIGHT - PADDLE_HEIGHT:
        right_paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT

    # Движение мяча
    ball_x = ball_x + ball_dx
    ball_y = ball_y + ball_dy

    # Отскок от верхней и нижней стены
    if ball_y < 0 or ball_y > SCREEN_HEIGHT - BALL_SIZE:
        ball_dy = -ball_dy

    # Отскок от левой ракетки
    if ball_x < 20 + PADDLE_WIDTH and ball_x > 20:
        if ball_y + BALL_SIZE > left_paddle_y and ball_y < left_paddle_y + PADDLE_HEIGHT:
            if ball_dx < 0:
                ball_dx = -ball_dx

                    # Отскок от правой ракетки
    if ball_x + BALL_SIZE > 770 and ball_x < 770 + PADDLE_WIDTH:
        if ball_y + BALL_SIZE > right_paddle_y and ball_y < right_paddle_y + PADDLE_HEIGHT:
            if ball_dx > 0:
                ball_dx = -ball_dx

    # Мяч улетел вправо — очко левому игроку
    if ball_x > SCREEN_WIDTH:
        score_left = score_left + 1
        ball_x = SCREEN_WIDTH // 2
        ball_y = SCREEN_HEIGHT // 2
        ball_dx = -7
        ball_dy = 7

    # Мяч улетел влево — очко правому игроку
    if ball_x + BALL_SIZE < 0:
        score_right = score_right + 1
        ball_x = SCREEN_WIDTH // 2
        ball_y = SCREEN_HEIGHT // 2
        ball_dx = 7
        ball_dy = 7

    # Рисование
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), (20, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, (255, 255, 255), (770, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, (255, 255, 255), (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    text_left = font.render(str(score_left), True, (255, 255, 255))
    text_right = font.render(str(score_right), True, (255, 255, 255))

    screen.blit(text_left, (SCREEN_WIDTH // 2 - 80, 20))
    screen.blit(text_right, (SCREEN_WIDTH // 2 + 60, 20))

    pygame.display.flip()
    clock.tick(60)