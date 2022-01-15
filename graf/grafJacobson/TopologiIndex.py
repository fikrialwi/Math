import math as m
class TopologicalIndex:
    def __init__(self, graf):
        pass
        self.graf = graf
    def getVertex(self):
        return self.graf.vertex()
    def getEdge(self):
        return self.graf.edge()
    def getEdgeofVertex(self, vertex):
        return self.graf.edgeofVertex(vertex)
    def getDegEdgeofVertex(self,vertex):
        return len(self.getEdgeofVertex(vertex ))
    def S(self, vertex):
        return sum(list(map(self.getDegEdgeofVertex,self.getEdgeofVertex(vertex))))

class NarumiKatayama(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def topologi(self):
        res = 1
        for i in self.getVertex():
            res *= self.getDegEdgeofVertex(i)
        return res

class ReciprocalRandic(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getEdgeofVertex(self, vertex):
        return super().getEdgeofVertex(vertex)
    def getEdge(self):
        return super().getEdge()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def topologi(self):
        res = 0
        for i in self.getVertex():
            for j in self.getVertex():
                if (i,j) in self.getEdge():
                    res += m.sqrt(self.getDegEdgeofVertex(i)*self.getDegEdgeofVertex(j))
        return res

class ReducedReciprocalRandic(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getEdgeofVertex(self, vertex):
        return super().getEdgeofVertex(vertex)
    def getEdge(self):
        return super().getEdge()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def topologi(self):
        res = 0
        for i in self.getVertex():
            for j in self.getVertex():
                if (i,j) in self.getEdge():
                    res += m.sqrt(abs(self.getDegEdgeofVertex(i)-1)*abs(self.getDegEdgeofVertex(j)-1))
        return res

class Randic(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getEdgeofVertex(self, vertex):
        return super().getEdgeofVertex(vertex)
    def getEdge(self):
        return super().getEdge()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def topologi(self, type = 1):
        res = 0
        for i in self.getVertex():
            for j in self.getVertex():
                if (i,j) in self.getEdge():
                    if type == 2:
                        res += 1/(m.sqrt(self.getDegEdgeofVertex(i)*self.getDegEdgeofVertex(j)))
                    else:
                        res += 1/(self.getDegEdgeofVertex(i)*self.getDegEdgeofVertex(j))
        return res

class FirstZagreb(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getEdgeofVertex(self, vertex):
        return super().getEdgeofVertex(vertex)
    def getEdge(self):
        return super().getEdge()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def topologi(self, type=1):
        res = 0
        if type == 1:
            for i in self.getVertex():
                res += self.getDegEdgeofVertex(i)**2
        else:
            for i in self.getVertex():
                for j in self.getVertex():
                    if (i,j) in self.getEdge():
                        res += (self.getDegEdgeofVertex(i)+self.getDegEdgeofVertex(j))
        return res

class SecondZagreb(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getEdgeofVertex(self, vertex):
        return super().getEdgeofVertex(vertex)
    def getEdge(self):
        return super().getEdge()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def topologi(self):
        res = 0
        for i in self.getVertex():
            for j in self.getVertex():
                if (i,j) in self.getEdge():
                    res += (self.getDegEdgeofVertex(i)*self.getDegEdgeofVertex(j))
        return res

class ForgottenTopological(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getEdgeofVertex(self, vertex):
        return super().getEdgeofVertex(vertex)
    def getEdge(self):
        return super().getEdge()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def topologi(self, type=1):
        res = 0
        if type == 1:
            for i in self.getVertex():
                res += self.getDegEdgeofVertex(i)**3
        else:
            for i in self.getVertex():
                for j in self.getVertex():
                    if (i,j) in self.getEdge():
                        res += (self.getDegEdgeofVertex(i)**2+self.getDegEdgeofVertex(j)**2)
        return res

class SecondMultipleZagreb(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getEdgeofVertex(self, vertex):
        return super().getEdgeofVertex(vertex)
    def getEdge(self):
        return super().getEdge()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def topologi(self):
        res = 1
        for i in self.getVertex():
            for j in self.getVertex():
                if (i,j) in self.getEdge():
                    res *= (self.getDegEdgeofVertex(i)*self.getDegEdgeofVertex(j))
        return res

class FirstMultipleZagreb(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getEdgeofVertex(self, vertex):
        return super().getEdgeofVertex(vertex)
    def getEdge(self):
        return super().getEdge()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def topologi(self, type=1):
        res = 1
        if type == 1:
            for i in self.getVertex():
                res *= self.getDegEdgeofVertex(i)**2
        else:
            for i in self.getVertex():
                for j in self.getVertex():
                    if (i,j) in self.getEdge():
                        res *= (self.getDegEdgeofVertex(i)+self.getDegEdgeofVertex(j))
        return res

class FirstZagrebCoindex(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getEdgeofVertex(self, vertex):
        return super().getEdgeofVertex(vertex)
    def getEdge(self):
        return super().getEdge()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def topologi(self, type=1):
        res = 1
        if type == 1:
            for i in self.getVertex():
                res *= self.getDegEdgeofVertex(i)**2
        else:
            for i in self.getVertex():
                for j in self.getVertex():
                    if i!=j and (i,j) not in self.getEdge() and (j,i) not in self.getEdge():
                        res += (self.getDegEdgeofVertex(i)+self.getDegEdgeofVertex(j))
        return res

class SecondZagrebCoindex(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getEdgeofVertex(self, vertex):
        return super().getEdgeofVertex(vertex)
    def getEdge(self):
        return super().getEdge()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def topologi(self):
        res = 1
        for i in self.getVertex():
            for j in self.getVertex():
                if i!=j and (i,j) not in self.getEdge() and (j,i) not in self.getEdge():
                        res += (self.getDegEdgeofVertex(i)*self.getDegEdgeofVertex(j))
        return res

class ReducedSecondZagreb(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getEdgeofVertex(self, vertex):
        return super().getEdgeofVertex(vertex)
    def getEdge(self):
        return super().getEdge()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def topologi(self):
        res = 0
        for i in self.getVertex():
            for j in self.getVertex():
                if (i,j) in self.getEdge():
                    res += ((self.getDegEdgeofVertex(i)-1)*(self.getDegEdgeofVertex(j)-1))
        return res

class AtomBondConectivity(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getEdgeofVertex(self, vertex):
        return super().getEdgeofVertex(vertex)
    def getEdge(self):
        return super().getEdge()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def topologi(self):
        res = 0
        for i in self.getVertex():
            for j in self.getVertex():
                if (i,j) in self.getEdge():
                    res += m.sqrt((self.getDegEdgeofVertex(i)+self.getDegEdgeofVertex(j) - 2)/(self.getDegEdgeofVertex(i)*self.getDegEdgeofVertex(j)))
        return res

class FouthVersionABC(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getEdgeofVertex(self, vertex):
        return super().getEdgeofVertex(vertex)
    def getEdge(self):
        return super().getEdge()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def topologi(self):
        res = 0
        for i in self.getVertex():
            for j in self.getVertex():
                if (i,j) in self.getEdge():
                    res += m.sqrt((self.S(i)+self.S(j) - 2)/(self.S(i)*self.S(j)))
        return res

class Harmonic(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getEdgeofVertex(self, vertex):
        return super().getEdgeofVertex(vertex)
    def getEdge(self):
        return super().getEdge()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def topologi(self):
        res = 0
        for i in self.getVertex():
            for j in self.getVertex():
                if (i,j) in self.getEdge():
                    res += (2/(self.getDegEdgeofVertex(i)+self.getDegEdgeofVertex(j)))
        return res

class AugmentedZagreb(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getEdgeofVertex(self, vertex):
        return super().getEdgeofVertex(vertex)
    def getEdge(self):
        return super().getEdge()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def topologi(self):
        res = 0
        for i in self.getVertex():
            for j in self.getVertex():
                if (i,j) in self.getEdge():
                    res += ((self.getDegEdgeofVertex(i)+self.getDegEdgeofVertex(j) - 2)/(self.getDegEdgeofVertex(i)*self.getDegEdgeofVertex(j)))**(-3)
        return res

class GeometricAritmethic(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getEdgeofVertex(self, vertex):
        return super().getEdgeofVertex(vertex)
    def getEdge(self):
        return super().getEdge()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def topologi(self):
        res = 0
        for i in self.getVertex():
            for j in self.getVertex():
                if (i,j) in self.getEdge():
                    res += 2*(m.sqrt(self.getDegEdgeofVertex(i)*self.getDegEdgeofVertex(j))/(self.getDegEdgeofVertex(i)+self.getDegEdgeofVertex(j)))
        return res

class FifthVersionGA(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getEdgeofVertex(self, vertex):
        return super().getEdgeofVertex(vertex)
    def getEdge(self):
        return super().getEdge()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def topologi(self):
        res = 0
        for i in self.getVertex():
            for j in self.getVertex():
                if (i,j) in self.getEdge():
                    res += 2*(m.sqrt(self.S(i)*self.S(j))/(self.S(i)+self.S(j)))
        return res

class SumConnectivity(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getEdgeofVertex(self, vertex):
        return super().getEdgeofVertex(vertex)
    def getEdge(self):
        return super().getEdge()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def topologi(self):
        res = 0
        for i in self.getVertex():
            for j in self.getVertex():
                if (i,j) in self.getEdge():
                    res += (self.getDegEdgeofVertex(i)+self.getDegEdgeofVertex(j))**(-1/2)
        return res

