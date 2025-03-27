import sys
import pygame
import random

pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("pygame")

clock = pygame.time.Clock()

VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render("Donovan", True, BRANCO)
texto_rect = texto.get_rect(center=(largura / 2, altura / 2))

velocidade_x = random.randint(-1, 1)
velocidade_y = random.randint(-1, 1)

while velocidade_x == 0:
    velocidade_x = random.randint(-1, 1)

while velocidade_y == 0:
    velocidade_y = random.randint(-1, 1)

pygame.mixer.init()

som_colisao = pygame.mixer.Sound("music2.mp3")

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

pygame.mixer.music.set_volume(0.6)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(PRETO)
    texto_rect.x += velocidade_x
    texto_rect.y += velocidade_y
    tela.blit(texto, texto_rect)

    if texto_rect.left <= 0:
        velocidade_x = random.randint(0, 1)
        velocidade_y = random.randint(-1, 1)
        cor_texto = (
            random.randint(10, 255),
            random.randint(10, 255),
            random.randint(10, 255),
        )
        texto = fonte.render("Donovan", True, cor_texto)
        som_colisao.play()

    if texto_rect.right >= largura:
        velocidade_x = random.randint(-1, 0)
        velocidade_y = random.randint(-1, 1)
        cor_texto = (
            random.randint(10, 255),
            random.randint(10, 255),
            random.randint(10, 255),
        )
        texto = fonte.render("Donovan", True, cor_texto)
        som_colisao.play()

    if texto_rect.top <= 0:
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(0, 1)
        cor_texto = (
            random.randint(10, 255),
            random.randint(10, 255),
            random.randint(10, 255),
        )
        texto = fonte.render("Donovan", True, cor_texto)
        som_colisao.play()

    if texto_rect.bottom >= altura:
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(-1, 0)
        cor_texto = (
            random.randint(10, 255),
            random.randint(10, 255),
            random.randint(10, 255),
        )
        texto = fonte.render("Donovan", True, cor_texto)
        som_colisao.play()

    clock.tick(100)
    pygame.display.flip()

pygame.quit()
sys.exit()