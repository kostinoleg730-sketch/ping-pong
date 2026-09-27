import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WIN_SCORE = 10

game_over = False
winner = ""

player_1 = 0
player_2 = 0

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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                player_1 = 0
                player_2 = 0
                game_over = False
                winner = ""
                ball_x = SCREEN_WIDTH // 2
                ball_y = SCREEN_HEIGHT // 2
                ball_dx = 7
                ball_dy = 7

    if not game_over:
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

        # Мяч улетел вправо — очко игроку 1
        if ball_x > SCREEN_WIDTH:
            player_1 = player_1 + 1
            ball_x = SCREEN_WIDTH // 2
            ball_y = SCREEN_HEIGHT // 2
            ball_dx = -7
            ball_dy = 7

        # Мяч улетел влево — очко игроку 2
        if ball_x + BALL_SIZE < 0:
            player_2 = player_2 + 1
            ball_x = SCREEN_WIDTH // 2
            ball_y = SCREEN_HEIGHT // 2
            ball_dx = 7
            ball_dy = 7

        # Проверка победы
        if player_1 >= WIN_SCORE:
            game_over = True
            winner = "PLAYER 1 WINS!"
        if player_2 >= WIN_SCORE:
            game_over = True
            winner = "PLAYER 2 WINS!"

    # Рисование
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), (20, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, (255, 255, 255), (770, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, (255, 255, 255), (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Счёт
    text_left = font.render(str(player_1), True, (255, 255, 255))
    text_right = font.render(str(player_2), True, (255, 255, 255))

    screen.blit(text_left, (SCREEN_WIDTH // 2 - 80, 20))
    screen.blit(text_right, (SCREEN_WIDTH // 2 + 60, 20))

    # Надпись победы
    if game_over:
        big_font = pygame.font.SysFont(None, 80)
        win_text = big_font.render(winner, True, (255, 255, 0))
        screen.blit(win_text, (SCREEN_WIDTH // 2 - win_text.get_width() // 2, SCREEN_HEIGHT // 2 - 40))

        hint_font = pygame.font.SysFont(None, 40)
        hint_text = hint_font.render("Press R to restart", True, (200, 200, 200))
        screen.blit(hint_text, (SCREEN_WIDTH // 2 - hint_text.get_width() // 2, SCREEN_HEIGHT // 2 + 40))

    pygame.display.flip()
    clock.tick(60)