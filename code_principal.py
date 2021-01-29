import pygame as pg
from interface import affiche_map, affiche_monstre_mort
from classe_mons_pers import Personnage, Monstre, Objet
from map import Map

personnage = Personnage([5, 5])
mur = [[[1, 1], [14, 8]], [[5, 15], [26, 22]], [[1, 25], [14, 32]]]
porte = [(14, 7), (22, 15), (2, 8), (2, 25)]
couloir = [[[15, 7], [22, 7], [22, 14]], [[2, 9], [2, 24]]]
carte = Map(mur, porte, couloir)
monstre1 = Monstre([10, 20], 15, 5)
monstre2 = Monstre([13, 31], 20, 5)
monstres = [monstre1, monstre2]
potion1 = Objet("soin", [5, 4], 30)
potion2 = Objet("soin", [18, 17], 30)
marteau = Objet("arme", [10, 5], 20)
listobj = [potion1, potion2, marteau]

running = True
while running:
    if personnage.hp <= 0:
        running = False
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
            for x in listobj:
                if x.position == personnage.position:
                    if event.key == pg.K_r:
                        if x.nom == "soin":
                            if personnage.hp < personnage.hpmax - x.power:
                                personnage.hp += x.power
                            else:
                                personnage.hp = personnage.hpmax
                        if x.nom == "arme":
                            if personnage.force < x.power:
                                personnage.force = x.power
                        if x.nom == "gold":
                            personnage.gold += x.power
                        listobj.remove(x)
        affiche_map(carte, personnage, monstres, listobj)
        pg.display.set_caption(f"Force : {personnage.force}")
        pg.display.set_caption(f"Gold : {personnage.gold}")
