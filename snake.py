import pygame
import sys

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

font = pygame.font.SysFont(None, 60)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змейка")

pygame.display.flip()