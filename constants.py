import pygame
from enum import Enum

BILDSCHIRM_BREITE, BILDSCHIRM_HOEHE = 800, 600

WEISS = (255, 255, 255)
SCHWARZ = (0, 0, 0)
ROT = (255, 0, 0)

FPS = 60
BILDER_VERZEICHNIS = "bilder"

SCHRIFT_KLEIN = None
SCHRIFT_GROSS = None


def init_fonts():
    global SCHRIFT_KLEIN, SCHRIFT_GROSS
    SCHRIFT_KLEIN = pygame.font.SysFont("arial", 25)
    SCHRIFT_GROSS = pygame.font.SysFont("arial", 36)


class Tasten(Enum):
    LINKS = pygame.K_LEFT
    RECHTS = pygame.K_RIGHT
    OBEN = pygame.K_UP
    UNTEN = pygame.K_DOWN
    A = pygame.K_a
    D = pygame.K_d
    W = pygame.K_w
    S = pygame.K_s
    PAUSE = pygame.K_p
