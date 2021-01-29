import pygame as pg
from interface import affiche_map, affiche_monstre_mort
from classe_mons_pers import Personnage, Monstre
from map import Map

personnage = Personnage([15, 15])
mur = [[[1, 1], [14, 8]], [[5, 15], [26, 22]]]
porte = [(14, 7), (22, 15)]
couloir = [[[15, 7], [22, 7], [22, 14]]]
carte = Map(mur, porte, couloir)
monstre = Monstre([10, 20])
monstres = [monstre]

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
            if event.key == pg.K_a:
                personnage.attaquer(monstres)
                for monstre in monstres:
                    affiche_monstre_mort(monstre)
            Personnage.avancer(personnage, event.key, carte)
            for monstre in monstres:
                if monstre.vivant:
                    Monstre.avancer(monstre, personnage, event.key, carte)
        affiche_map(carte, personnage, monstres)
