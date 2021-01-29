import pygame as pg

class Personnage:
     
    def __init__(self, position, hp=100, force=80):
        self.position = position
        self.hp = hp
        self.force = force
        self.previous = position

    def avancer(self, key):
        self.previous = self.position
        if key == pg.K_LEFT:
            direction = [-1, 0]
        if key == pg.K_RIGHT:
            direction = [1, 0]
        if key == pg.K_UP:
            direction = [0, -1]
        if key == pg.K_DOWN:
            direction = [0, 1] 
        
        pos = [self.position[0] + direction[0], self.position[1] + direction[1]]
        if pos not in 
    

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
    
    def attaquer(self, personnage)







    
