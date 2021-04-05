import pygame
import numpy
import math
from fisica import *

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
largura = 640
altura = 300
pos_x0 = largura / 2
pos_y0 = altura / 2
pos_x = pos_x0 - 150
pos_y = pos_y0
velocidade_x = 0
velocidade_y = -0.05
aceleracao_x = 0
aceleracao_y = 0
m1 = 1
m2 = 2
G = 1
'''
f = G * m1 * m2 / d ** 2

f = m1 * a1

a1 = G * m2 / d ** 2
a2 = G * m1 / d ** 2
'''
relogio = pygame.time.Clock()
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Valentines Game')

continua = True
while continua: 


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continua = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continua = False

    vetor_distancia = (pos_x0 - pos_x, pos_y0 - pos_y)
    ro_distancia = distancia(pos_x, pos_y, pos_x0, pos_y0)
    versor_i = (pos_x0 - pos_x) / ro_distancia
    versor_j = (pos_y0 - pos_y) / ro_distancia

    aceleracao_x = (force(G, m1, m2, ro_distancia) / m2) * versor_i
    aceleracao_y = (force(G, m1, m2, ro_distancia) / m2) * versor_j
    velocidade_x += aceleracao_x
    velocidade_y += aceleracao_y
    velocidade = (velocidade_x ** 2 + velocidade_y ** 2) ** 0.5
    pos_x += velocidade_x
    pos_y += velocidade_y

    window.fill(white)
    texto("Velocidade: " + str(velocidade), black, 20, 10, altura - 30)
    pygame.draw.circle(window, black, (pos_x, pos_y), 5)
    pygame.draw.circle(window, red, (pos_x0, pos_y0), 5)
    relogio.tick(600)
    pygame.display.update()

pygame.quit()