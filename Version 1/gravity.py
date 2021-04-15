import pygame
import numpy
import math
import random
from fisica import *

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
gray = (55, 55, 55)
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
m1 = 10
m2 = 200
G = 1
planetas = []
#p1 = Planeta(pos_x, pos_y, velocidade_x, velocidade_y, 0, 0, m1)
p2 = Planeta(pos_x0, pos_y0, 0, 0, 0, 0, m2, red, 5)
for i in range(5):
    pos_x = random.randint(150, largura / 2)
    #pos_y = random.randint(50, altura - 50)
    '''if random.random() < 0.5:
        signal = -1
    else:
        signal = 1
    velocidade_x = random.random() * 0.01 * signal'''
    if random.random() < 0.5:
        signal = -1
    else:
        signal = 1
    velocidade_y = 0.15 * signal
    m = float(random.randint(1, 10))
    r = float(random.randint(1, 5))
    planetas.append(Planeta(pos_x, altura / 2, 0, velocidade_y, 0, 0, 5, white, r))
'''
Gravitação Universal:
f = G * m1 * m2 / d ** 2

Segunda lei de Newton:
f = m1 * a1

a1 = G * m2 / d ** 2
a2 = G * m1 / d ** 2
'''
relogio = pygame.time.Clock()
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Valentines Game')
window.fill(gray)

def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    window.blit(texto1, [x, y])

continua = True
while continua: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continua = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continua = False
    for p1 in planetas:
        p1.force2(p2)
        p1.update_pos(p1.vx, p1.vy)
        p1.update_velocity(p1.ax, p1.ay)
        #p1.update()
        velocidade = (p1.vx ** 2 + p1.vy ** 2) ** 0.5
        
        window.fill(gray)
        #texto(f"Velocidade: {velocidade:.7f}", white, 20, 10, altura - 80)
        #texto(f"Distancia: {velocidade:.7f}", white, 20, 10, altura - 60)
        #texto(f"Periélio: {min(p1.distancias):.5f}", white, 20, 10, altura - 40)
        #texto(f"Afélio: {max(p1.distancias):.5f}", white, 20, 10, altura - 20)
        pygame.draw.circle(window, red, (p2.x, p2.y), p2.r)
        for p1 in planetas:
            pygame.draw.circle(window, p1.color, (p1.x, p1.y), p1.r)
        relogio.tick(600)
        pygame.display.update()

pygame.quit()