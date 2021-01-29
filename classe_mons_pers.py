import pygame as pg

class Personnage:
     
    def __init__(self, position, hp=100, force=80):
        self.position = position
        self.hp = hp
        self.force = force

    def avancer(self, key):
        if key == pg.K_LEFT:
            direction = [-1, 0]
        if key == pg.K_RIGHT:
            direction = [1, 0]
        if key == pg.K_UP:
            direction = [0, -1]
        if key == pg.K_DOWN:
            direction = [0, 1] 
        
        self.position = [self.position[0] + direction[0], self.position[1] + direction[1]]
    
    
    
    
