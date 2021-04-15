import math
G = 1

class Planeta:
    #G = 1
    def __init__(self, pos_x, pos_y, v_x, v_y, a_x, a_y, massa, color=(255, 255, 255), raio=3):
        self.x = pos_x
        self.y = pos_y
        self.vx = v_x
        self.vy = v_y
        self.ax = a_x
        self.ay = a_y
        self.m = massa
        self.color = color
        self.r = raio
        self.distancias = set()

    def update_pos(self, v_x, v_y):
        self.x += v_x
        self.y += v_y
    
    def update_velocity(self, a_x, a_y):
        self.vx += a_x
        self.vy += a_y
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vx += self.ax
        self.vy += self.ay

    def force2(self, p):
        vetor_distancia = (p.x - self.x, p.y - self.y)
        ro_distancia = distancia(self.x, self.y, p.x, p.y)
        #self.distancias.add(ro_distancia)
        #force_max = force(G, self.m, p.m, 15)
        versor_i = vetor_distancia[0] / ro_distancia
        versor_j = vetor_distancia[1] / ro_distancia
        max_dis = 5
        if ro_distancia < max_dis:
            f = force(G, self.m, p.m, max_dis)
        else:
            f = force(G, self.m, p.m, ro_distancia)
        self.ax = calcula_aceleracao(f, p.m) * versor_i
        self.ay = calcula_aceleracao(f, p.m) * versor_j


#Calcula força
def force(G, m1, m2, d):
    return (G * m1 * m2) / (d * d)

#Calcula distancia entre dois pontos
def distancia(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

#Calcula aceleracão
def calcula_aceleracao(force, m):
    return force / m