import pygame as pg
from interface import affiche_map
from classe_mons_pers import Personnage

personnage = Personnage([15, 15])
carte = [[8, 8]]


running = True
while running:
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False
            Personnage.avancer(personnage, event.key)
        affiche_map(carte, personnage)
