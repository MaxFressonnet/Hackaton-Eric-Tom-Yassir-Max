

class Map:

    def __init__(self,mur,porte,couloir):
        self.murs = []
        for k in range(len(mur)):
            for i in range(mur[k][0][0],mur[k][1][0]):
                self.murs.append([mur[k][0][1],i])
                self.murs.append([mur[k][1][1],i])
            for j in range(mur[k][0][1],mur[k][1][1]):
                self.murs.append([j,mur[k][0][0]])
                self.murs.append([j,mur[k][1][0]])
        self.portes = porte
        for i in range(len(self.murs)):
            for y in porte:
                if self.murs[i]==y:
                    del(self.murs[i])
        self.couloirs = []
        for k in range(len(couloir)):
            if len(couloir[k])>1:
                for i in range(len(couloir[k]) - 1):
                    if i < len(couloir[k]) - 2:
                        if couloir[k][i][0] != couloir[k][i + 1][0]:
                            for j in range(couloir[k][i][0],couloir[k][i + 1][0]):
                                self.couloirs.append([j,couloir[k][i][1]])
                        else:
                            for m in range(couloir[k][i][1],couloir[k][i + 1][1]):
                                self.couloirs.append([couloir[k][i][0],m])
                    else:
                        if couloir[k][i][0] != couloir[k][i + 1][0]:
                            for j in range(couloir[k][i][0],couloir[k][i + 1][0]+1):
                                self.couloirs.append([j,couloir[k][i][1]])
                        else:
                            for m in range(couloir[k][i][1],couloir[k][i + 1][1]+1):
                                self.couloirs.append([couloir[k][i][0],m])



mur = [[[1,1],[14,8]],[[5,15],[26,22]]]
porte = [[13,7],[22,15]]
couloir = [[[13,7],[22,7],[22,15]]]

map1 = Map(mur,porte,couloir)