import pygame as pg
pg.init()
taille = 30
screen = pg.display.set_mode((taille * taille, taille * taille))


def affiche_map(carte, personnage):
    for (x, y) in carte:
        rect = pg.Rect(x*taille, y*taille, taille, taille)
        color = (255, 255, 255)
        pg.draw.rect(screen, color, rect)
    pg.display.update()
    a, b = personnage.position
    rect = pg.Rect(a*taille, b*taille, taille, taille)
    color = (0, 255, 0)
    pg.draw.rect(screen, color, rect)
    pg.display.update
    c, d = personnage.previous
    rect = pg.Rect(c*taille, d*taille, taille, taille)
    color = (0, 0, 0)
    pg.draw.rect(screen, color, rect)
    pg.display.update
