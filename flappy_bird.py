import pygame
import os
import random

TELA_LARGURA = 500
TELA_ALTURA = 600

IMAGEM_CANO_BASE = pygame.image.load(os.path.join('imgs', 'pipe_bottom.png'))
IMAGEM_CANO_TOPO = pygame.image.load(os.path.join('imgs', 'pipe_top.png'))
IMAGEM_CHAO = pygame.image.load(os.path.join('imgs', 'base.png'))
IMAGEM_BACKGROUND = pygame.image.load(os.path.join('imgs', 'bg.png'))
IMAGENS_PASSARO = [
    pygame.image.load(os.path.join('imgs', 'bird1.png')),
    pygame.image.load(os.path.join('imgs', 'bird2.png')),
    pygame.image.load(os.path.join('imgs', 'bird3.png')),
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)


class passaro:
    IMGS = IMAGENS_PASSARO
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 26
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = IMGS[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        self.tempo += 1
        #S = S0 + V0T + AT²/2:
        deslocamento = ????

class cano:
    pass

class floor:
    pass
