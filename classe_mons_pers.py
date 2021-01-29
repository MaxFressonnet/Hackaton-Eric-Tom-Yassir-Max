import pygame as pg
from map import Map


class Personnage:

    def __init__(self, position, hp=100, force=10):
        self.position = position
        self.hp = hp
        self.force = force
        self.previous = position
        self.gold = 0
        self.hpmax = hp

    def avancer(self, key, carte):
        direction = [0, 0]
        self.previous = list.copy(self.position)
        if key == pg.K_LEFT:
            direction = [-1, 0]
        if key == pg.K_RIGHT:
            direction = [1, 0]
        if key == pg.K_UP:
            direction = [0, -1]
        if key == pg.K_DOWN:
            direction = [0, 1]

        pos = (self.position[0] + direction[0],
               self.position[1] + direction[1])
        if tuple(self.position) in carte.couloirs:
            if pos not in carte.murs and (pos in carte.couloirs or pos in carte.portes):
                self.position = list(pos)
        else:
            if pos not in carte.murs:
                self.position = list(pos)

    def attaquer(self, monstres):
        for monstre in monstres:
            if monstre.vivant:
                m_pos = monstre.position
                x_m, y_m = m_pos[0], m_pos[1]
                x_p, y_p = self.position[0], self.position[1]
                d_x = x_p - x_m
                d_y = y_p - y_m
                d = abs(d_x) + abs(d_y)
                if d <= 1:
                    monstre.hp -= self.force
                if monstre.hp <= 0:
                    monstre.vivant = False


class Monstre:

    def __init__(self, position, hp, force, couleur=(255, 0, 0)):
        self.position = position
        self.hp = hp
        self.force = force
        self.vue = False
        self.previous = position
        self.vivant = True
        self.couleur = couleur

    def avancer(self, personnage, key, carte):
        self.previous = list.copy(self.position)
        pos_pers = personnage.position
        x_p, y_p = pos_pers[0], pos_pers[1]
        x_m, y_m = self.position[0], self.position[1]
        d_x = x_p - x_m
        d_y = y_p - y_m
        d = max(abs(d_x), abs(d_y))
        if self.vue and d >= 2:
            if d == abs(d_x):
                pos = [x_m + d_x/d, y_m]
                if tuple(pos) not in carte.murs and not tuple(pos) in carte.portes:
                    self.position = pos
            else:
                pos = [x_m, y_m + d_y/d]
                if tuple(pos) not in carte.murs and not tuple(pos) in carte.portes:
                    self.position = pos
        elif d <= 5:
            self.vue = True
        if d <= 1:
            personnage.hp -= self.force


class Objet:

    def __init__(self,nom,pos, power):
        self.nom = nom
        self.position = pos
        self.power = power