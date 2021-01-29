class Map:

    def __init__(self, mur, porte, couloir):
        self.murs = set([])
        for k in range(len(mur)):
            for i in range(mur[k][0][0], mur[k][1][0]):
                self.murs.add((i, mur[k][0][1]))
                self.murs.add((i, mur[k][1][1]))
            for j in range(mur[k][0][1], mur[k][1][1]):
                self.murs.add((mur[k][0][0], j))
                self.murs.add((mur[k][1][0], j))
            self.murs.add((mur[k][1][0], mur[k][1][1]))
        self.portes = set(porte)
        for y in porte:
            if y in self.murs:
                self.murs.remove(y)
        self.couloirs = set([])
        for k in range(len(couloir)):
            if len(couloir[k]) > 1:
                for i in range(len(couloir[k]) - 1):
                    if i < len(couloir[k]) - 2:
                        if couloir[k][i][0] != couloir[k][i + 1][0]:
                            for j in range(couloir[k][i][0], couloir[k][i + 1][0]):
                                self.couloirs.add((j, couloir[k][i][1]))
                        else:
                            for m in range(couloir[k][i][1], couloir[k][i + 1][1]):
                                self.couloirs.add((couloir[k][i][0], m))
                    else:
                        if couloir[k][i][0] != couloir[k][i + 1][0]:
                            for j in range(couloir[k][i][0], couloir[k][i + 1][0]+1):
                                self.couloirs.add((j, couloir[k][i][1]))
                        else:
                            for m in range(couloir[k][i][1], couloir[k][i + 1][1]+1):
                                self.couloirs.add((couloir[k][i][0], m))


mur = [[[1, 1], [13, 8]], [[5, 15], [26, 22]]]
porte = [(13, 7), (22, 15)]
couloir = [[[14, 7], [22, 7], [22, 14]]]

map1 = Map(mur, porte, couloir)
