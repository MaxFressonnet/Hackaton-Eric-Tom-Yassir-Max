import pygame as pg
from map import Map

class Personnage:
     
    def __init__(self, position, hp=100, force=80):
        self.position = position
        self.hp = hp
        self.force = force
        self.previous = position

    def avancer(self, key, carte):
        direction = [0, 0]
        self.previous = self.position
        if key == pg.K_LEFT:
            direction = [-1, 0]
        if key == pg.K_RIGHT:
            direction = [1, 0]
        if key == pg.K_UP:
            direction = [0, -1]
        if key == pg.K_DOWN:
            direction = [0, 1] 
        
        pos = (self.position[0] + direction[0], self.position[1] + direction[1])
        if tuple(self.position) in carte.couloirs:
            if pos not in carte.murs and (pos in carte.couloirs or pos in carte.portes):
                self.position = pos
        else :
            if pos not in carte.murs:
                self.position = pos
             



class Monstre:

    def __init__(self, position, hp=100, force=120):
        self.position = position
        self.hp = hp
        self.force = force
        self.vue = False


    def avancer(self, pos_pers, key):
        x_p, y_p = pos_pers[0], pos_pers[1]
        x_m, y_m = self.position[0], self.position[1]
        d_x = x_p - x_m
        d_y = y_p - y_m
        d = max(abs(d_x), abs(d_y))
        if self.vue:
            if d == abs(d_x):
                self.position = [x_m + d_x/d, y_m]
            else:
                self.position = [x_m, y_m + d_y/d]
        else:
            if d <= 5:
                self.vue = True
    


    def attaquer(self, personnage):
        pass







    
