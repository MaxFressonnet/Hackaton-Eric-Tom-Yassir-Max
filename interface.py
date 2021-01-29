import pygame as pg
from classe_mons_pers import Monstre
pg.init()
taille = 20
screen = pg.display.set_mode((600, 600))


def affiche_map(carte, personnage, monstres):
    for (x, y) in carte.murs:
        rect = pg.Rect(x*taille, y*taille, taille, taille)
        color = (255, 255, 255)
        pg.draw.rect(screen, color, rect)
    for (x, y) in carte.portes:
        if (x, y) != tuple(personnage.position):
            rect = pg.Rect(x*taille, y*taille, taille, taille)
            color = (0, 0, 255)
            pg.draw.rect(screen, color, rect)
    for(x, y) in carte.couloirs:
        if (x, y) != tuple(personnage.position):
            rect = pg.Rect(x*taille, y*taille, taille, taille)
            color = (0, 255, 255)
            pg.draw.rect(screen, color, rect)
    pg.display.update()
    a, b = personnage.position
    font_obj = pg.font.Font('freesansbold.ttf', taille // 2)
    text_surface_obj = font_obj.render(
        f'{personnage.hp}', True, (255, 0, 0))
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (taille * a + taille / 2,
                            taille * b + taille / 2)
    rect = pg.Rect(a*taille, b*taille, taille, taille)
    color = (0, 255, 0)
    pg.draw.rect(screen, color, rect)
    screen.blit(text_surface_obj, text_rect_obj)
    pg.display.update
    c, d = personnage.previous
    if (c, d) != (a, b):
        rect = pg.Rect(c*taille, d*taille, taille, taille)
        color = (0, 0, 0)
        pg.draw.rect(screen, color, rect)
        pg.display.update
    for monstre in monstres:
        if monstre.vivant:
            font_obj = pg.font.Font('freesansbold.ttf', taille - 1)
            text_surface_obj = font_obj.render(
                f'{monstre.hp}', True, (255, 255, 0))
            text_rect_obj = text_surface_obj.get_rect()
            x, y = monstre.position
            u, v = monstre.previous
            text_rect_obj.center = (taille * x + taille / 2,
                                    taille * y + taille / 2)
            rect = pg.Rect(x*taille, y*taille, taille, taille)
            color = (255, 0, 0)
            pg.draw.rect(screen, color, rect)
            screen.blit(text_surface_obj, text_rect_obj)
            if (u, v) != (x, y):
                rect = pg.Rect(u*taille, v*taille, taille, taille)
                color = (0, 0, 0)
                pg.draw.rect(screen, color, rect)
                pg.display.update


def affiche_monstre_mort(monstre):
    if monstre.hp <= 0:
        x, y = monstre.position
        rect = pg.Rect(x*taille, y*taille, taille, taille)
        color = (0, 0, 0)
        pg.draw.rect(screen, color, rect)
        pg.display.update
