import pygame
import os
import random

TELA_LARGURA = 500
TELA_ALTURA = 600

IMAGEM_CANO = pygame.image.load(os.path.join('img', 'pipe.png'))
IMAGEM_CHAO = pygame.image.load(os.path.join('img', 'base.png'))
IMAGEM_BACKGROUND = pygame.image.load(os.path.join('img', 'bg.png'))
IMAGENS_PASSARO = [
    pygame.image.load(os.path.join('img', 'bird1.png')),
    pygame.image.load(os.path.join('img', 'bird2.png')),
    pygame.image.load(os.path.join('img', 'bird3.png')),
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)


class passaro:
    pass

class cano:
    pass

class floor:
    pass
