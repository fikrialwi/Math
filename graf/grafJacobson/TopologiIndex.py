import Graf as graf

class TopologicalIndex:
    def __init__(self, graf):
        pass
        self.graf = graf
    def getVertex(self):
        return self.graf.vertex()
    def getEdeg(self):
        return self.graf.edge()
    def getEdgeofVertex(self, vertex):
        return self.graf.edgeofVertex(vertex)
    def getDegEdgeofVertex(self,vertex):
        return len(self.getEdgeofVertex(vertex ))

class NarumiKatayama(TopologicalIndex):
    def __init__(self, graf):
        super().__init__(graf)
    def getVertex(self):
        return super().getVertex()
    def getDegEdgeofVertex(self, vertex):
        return super().getDegEdgeofVertex(vertex)
    def narumikatayama(self):
        res = 1
        for i in self.getVertex():
            res *= self.getDegEdgeofVertex(i)
        return res


NK = NarumiKatayama(graf.GrafJacobson('Z_11','*'))
print(NK.getEdgeofVertex(0))