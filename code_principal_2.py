import pygame as pg
from interface import affiche_map, affiche_monstre_mort
from classe_mons_pers import Personnage, Monstre, Objet
from map import Map

personnage = Personnage([5, 5])
mur = [[[1, 1], [14, 8]], [[5, 15], [26, 22]]]
porte = [(14, 7), (22, 15)]
couloir = [[[15, 7], [22, 7], [22, 14]]]
carte = Map(mur, porte, couloir)
monstre = Monstre([10, 20], 15, 5)
monstres = [monstre]
potion1 = Objet("soin", [5, 4], 30)
potion2 = Objet("soin", [18, 17], 30)
marteau = Objet("arme", [10, 5], 20)
listobj = [potion1, potion2, marteau]



mur2 = [[[1,1],[12,7]],[[16,5],[27,17]],[[2,12],[13,27]]
porte2 = [(13,2),(22,5),(18,17),(13,23)]
couloir2 = [[[13,2],[22,2],[22,4]],[[18,18],[18,23],[14,23]]]
carte2 = Map(mur2,porte2,couloir2)
monstre2 = Monstre([18,9], 25, 10)
monstres2 = [monstre2]
potion21 = Objet("soin",[25,14], 30)
gold2 = Objet("gold", [7, 17], 1)
epee = Objet("arme", [8,5], 30)
listobj2 = [potion21, gold2, epee]

escalier = [6,21]
escalier2 = [2,2]



running = True
while running:
    if personnage.hp <= 0:
        running = False
    objets = listobj
    lesmonstres = monstres
    lacarte = carte
    esc = escalier
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
            if event.key == pg.K_e:
                if personnage.position == escalier:
                    objets = listobj2
                    lesmonstres = monstres2
                    lacarte = carte2
                    esc = escalier2
            if event.key == pg.K_t:
                if personnage.position == escalier2:
                    objets = listobj
                    lesmonstres = monstres
                    lacarte = carte
                    esc = escalier


        affiche_map(lacarte, personnage, lesmonstres, objets, [esc])
        pg.display.set_caption(f"Force : {personnage.force}, Gold : {personnage.gold}")
