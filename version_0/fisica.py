import math

#Calcula força
def force(G, m1, m2, d):
    return (G * m1 * m2) / (d ** 2)

#Calcula distancia entre dois pontos
def distancia(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

#Calcula aceleracão
def calcula_aceleracao(force, m):
    return force / m