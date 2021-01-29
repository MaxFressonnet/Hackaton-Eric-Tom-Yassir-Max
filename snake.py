import pygame as pg
from random import randint

pg.init()
screen = pg.display.set_mode((900, 900))
clock = pg.time.Clock()

running = True


def affiche_damier():
    width = 30
    height = 30
    for x in range(30):
        for y in range(30):
            if (x + y) % 2 == 0:
                rect = pg.Rect(x*30, y*30, width, height)
                color = (255, 255, 255)
                pg.draw.rect(screen, color, rect)
            pg.display.update()


snake = [
    (10, 15),
    (11, 15),
    (12, 15),
]
direction = (1, 0)
fruit = (10, 10)
score = 0


def affiche_serpent():
    width = 20
    height = 20
    global running
    global score
    global direction
    global fruit
    c, d = fruit
    color = (255, 0, 0)
    rect = pg.Rect((c)*20, (d)*20, width, height)
    pg.draw.rect(screen, color, rect)
    pg.display.update()
    u, v = snake[0]
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT and direction != (1, 0):
            direction = (-1, 0)
        if event.key == pg.K_RIGHT and direction != (-1, 0):
            direction = (1, 0)
        if event.key == pg.K_UP and direction != (0, 1):
            direction = (0, -1)
        if event.key == pg.K_DOWN and direction != (0, -1):
            direction = (0, 1)
    for i in range(len(snake)):
        (x, y) = snake[i]
        rect = pg.Rect(x*20, y*20, width, height)
        color = (255, 255, 255)
        pg.draw.rect(screen, color, rect)
        pg.display.update()
        if i != len(snake) - 1:
            snake[i] = snake[i + 1]
        else:
            a, b = direction
            for (uu, vv) in snake:
                if x+a == uu and y+b == vv:
                    running = False
            snake[i] = (x+a, y+b)
    if snake[-1] != fruit:
        color = (0, 0, 0)
        rect = pg.Rect((u)*20, (v)*20, width, height)
        pg.draw.rect(screen, color, rect)
        pg.display.update()
    else:
        snake.insert(0, (u, v))
        fruit = (randint(1, 19), randint(1, 19))
        c, d = fruit
        score += 1
        color = (255, 0, 0)
        rect = pg.Rect((c)*20, (d)*20, width, height)
        pg.draw.rect(screen, color, rect)
        pg.display.set_caption(f"Score: {score}")
        pg.display.update()


pg.display.set_caption(f"Score: {score}")
while running:
    clock.tick(3)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
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
    affiche_serpent()


# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()
