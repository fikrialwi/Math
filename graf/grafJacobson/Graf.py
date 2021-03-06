import Bilangan as bil
import abc 
class GrafofRing:
    def __init__(self, ring, operation):
        self.ring = ring
        self.operation = operation
    # __Modulo = bil.Modulo(self.getNumber(),self.operation)
    def getNumber(self):
        return int(self.ring.split('_')[-1])
    def getOperation(self):
        return self.operation
    def getRing(self):
        return bil.Modulo(self.getNumber(),self.getOperation())

class GrafJacobson(GrafofRing):
    def __init__(self, ring, operation):
        super().__init__(ring, operation)
    def getRing(self):
        return super().getRing()
    def getOperation(self):
        return super().getOperation()
    def getNumber(self):
        return super().getNumber()
    def getJacobson(self):  
        return bil.Jacobson(self.getNumber(),self.getOperation())
    def get_jacobson(self):
        return self.getJacobson().jacobson()[0]
    def vertex(self):
        element = self.getJacobson().element()
        jacobson = self.get_jacobson()
        vertex = []
        if type(jacobson) == list:
            [vertex.append(i) for i in element if i not in jacobson]
        else:
            [vertex.append(i) for i in element if i != 0]
        return vertex
    def edge(self):
        edge = []
        for i in self.vertex():
            for j in self.vertex():
                if i != j:
                    if self.adjacent(i,j):
                        edge.append({i,j})
        edge = self.getRing().uniq(edge)
        return list(map(tuple,edge))
    def orde(self):
        return len(self.vertex())
    def size(self):
        return len(self.edge())
    def neighboor(self,vertex):
        if vertex not in self.vertex(): 
            return "Bilangan tidak termasuk dalam himpunan titik graf"
        edge = []
        for i in self.vertex():
            if self.adjacent(i,vertex) :
                edge.append(i)
        return edge
    def degree(self, vertex):
        return len(self.neighboor(vertex))
    def adjacent(self,vertex1,vertex2):
        return (1-vertex1*vertex2)%self.getNumber() not in self.getRing().unit()
    def matrixAdjencey(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if self.adjacent(i,j):
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix

class GrafUnit(GrafofRing):
    def __init__(self, ring, operation):
        super().__init__(ring, operation)
    def getNumber(self):
        return super().getNumber()
    def getRing(self):
        return super().getRing()
    def getUnit(self):
        return self.getRing().unit()
    def vertex(self):
        return self.getRing().element()
    def edge(self):
        vertex = self.vertex()
        edge = []
        for i in vertex:
            for j in vertex:
                if (i+j)%self.getNumber() in self.getUnit():
                    edge.append({i,j})
        edge = self.getRing().uniq(edge)
        return list(map(tuple,edge))
    def orde(self):
        return len(self.vertex())
    def size(self):
        return len(self.edge())
    def neighboor(self,vertex):
        if vertex not in self.vertex() : 
            return "Bilangan tidak termasuk dalam himpunan titik graf"
        edge = []
        for i in self.vertex():
            if self.adjacent(i,vertex) :
                edge.append(i)
        return edge
    def degree(self, vertex):
        return len(self.neighboor(vertex))
    def adjacent(self,vertex1,vertex2):
        return (vertex1+vertex2)%self.getNumber() in self.getUnit() and vertex1 != vertex2
    def matrixAdjencey(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if self.adjacent(i,j):
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix

class GrafZeroDivisor(GrafofRing):
    def __init__(self, ring, operation):
        super().__init__(ring, operation)
    def getNumber(self):
        return super().getNumber()
    def getRing(self):
        return super().getRing()
    def vertex(self):
        return self.getRing().zeroDivisor()
    def edge(self):
        vertex = self.vertex()
        edge = []
        for i in vertex:
            for j in vertex:
                if i*j%self.getNumber() == 0:
                    edge.append({i,j})
        edge = self.getRing().uniq(edge)
        return list(map(tuple,edge))
    def orde(self):
        return len(self.vertex())
    def size(self):
        return len(self.edge())
    def neighboor(self,vertex):
        if vertex not in self.vertex() : 
            return "Bilangan tidak termasuk dalam himpunan titik graf"
        edge = []
        for i in self.vertex():
            if self.adjacent(i,vertex) :
                edge.append(i)
        return edge
    def degree(self, vertex):
        return len(self.neighboor(vertex))
    def adjacent(self,vertex1,vertex2):
        return (vertex1*vertex2)%self.getNumber() == 0 and vertex1 != vertex2
    def matrixAdjencey(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if self.adjacent(i,j):
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix

class GrafTotal(GrafofRing):
    def __init__(self, ring, operation):
        super().__init__(ring, operation)
    def getNumber(self):
        return super().getNumber()
    def getRing(self):
        return super().getRing()
    def getZeroDivisor(self):
        return self.getRing().zeroDivisor()
    def vertex(self):
        return self.getRing().element()
    def edge(self):
        vertex = self.vertex()
        edge = []
        for i in vertex:
            for j in vertex:
                if self.adjacent(i,j):
                    edge.append({i,j})
        edge = self.getRing().uniq(edge)
        return list(map(tuple,edge))
    def orde(self):
        return len(self.vertex())
    def size(self):
        return len(self.edge())
    def neighboor(self,vertex):
        if vertex not in self.vertex() : 
            return "Bilangan tidak termasuk dalam himpunan titik graf"
        edge = []
        for i in self.vertex():
            if self.adjacent(i,vertex) :
                edge.append(i)
        return edge
    def degree(self, vertex):
        return len(self.neighboor(vertex))
    def adjacent(self,vertex1,vertex2):
        return (vertex1+vertex2)%self.getNumber() in self.getZeroDivisor() and vertex1 != vertex2
    def matrixAdjencey(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if self.adjacent(i,j):
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix

class GrafTotalZeroDivisor(GrafofRing):
    def __init__(self, ring, operation):
        super().__init__(ring, operation)
    def getNumber(self):
        return super().getNumber()
    def getRing(self):
        return super().getRing()
    def getZeroDivisor(self):
        return self.getRing().zeroDivisor()
    def vertex(self):
        return self.getZeroDivisor()
    def edge(self):
        vertex = self.vertex()
        edge = []
        for i in vertex:
            for j in vertex:
                if self.adjacent(i,j) :
                    edge.append({i,j})
        edge = self.getRing().uniq(edge)
        return list(map(tuple,edge))
    def orde(self):
        return len(self.vertex())
    def size(self):
        return len(self.edge())
    def neighboor(self,vertex):
        if vertex not in self.vertex() : 
            return "Bilangan tidak termasuk dalam himpunan titik graf"
        edge = []
        for i in self.vertex():
            if self.adjacent(i,vertex):
                edge.append(i)
        return edge
    def degree(self, vertex):
        return len(self.neighboor(vertex))
    def adjacent(self,vertex1,vertex2):
        return vertex1 != vertex2 and (vertex1*vertex2)%self.getNumber() in self.getZeroDivisor() and (vertex1+vertex2)%self.getNumber() == 0
    def matrixAdjencey(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if self.adjacent(i,j):
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix

class GrafIdentity(GrafofRing):
    def __init__(self, ring, operation):
        super().__init__(ring, operation)
    def getNumber(self):
        return super().getNumber()
    def getRing(self):
        return super().getRing()
    def getUnit(self):
        return self.getRing().unit()
    def vertex(self):
        return self.getUnit()
    def edge(self):
        vertex = self.vertex()
        edge = []
        for i in vertex:
            for j in vertex:
                if self.adjacent(i,j):
                    edge.append({i,j})
        edge = self.getRing().uniq(edge)
        return list(map(tuple,edge))
    def orde(self):
        return len(self.vertex())
    def size(self):
        return len(self.edge())
    def neighboor(self,vertex):
        if vertex not in self.vertex() : 
            return "Bilangan tidak termasuk dalam himpunan titik graf"
        edge = []
        for i in self.vertex():
            if self.adjacent(i,vertex):
                edge.append(i)
        return edge
    def degree(self, vertex):
        return len(self.neighboor(vertex))
    def adjacent(self,vertex1,vertex2):
        return (vertex1*vertex2)%self.getNumber() == 1 and vertex1 != vertex2
    def matrixAdjencey(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if self.adjacent(i,j):
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix

class GrafAnnihilator(GrafofRing):
    def __init__(self, ring, operation):
        super().__init__(ring, operation)
    def getNumber(self):
        return super().getNumber()
    def getRing(self):
        return super().getRing()
    def getZeroDivisor(self):
        return self.getRing().zeroDivisor()
    def vertex(self):
        return self.getZeroDivisor()
    def edge(self):
        vertex = self.vertex()
        edge = []
        for i in vertex:
            for j in vertex:
                if self.adjacent(i,j):
                    edge.append({i,j})
        edge = self.getRing().uniq(edge)
        return list(map(tuple,edge))
    def orde(self):
        return len(self.vertex())
    def size(self):
        return len(self.edge())
    def neighboor(self,vertex):
        if vertex not in self.vertex() : 
            return "Bilangan tidak termasuk dalam himpunan titik graf"
        edge = []
        for i in self.vertex():
            if self.adjacent(i,vertex):
                edge.append(i)
        return edge
    def degree(self, vertex):
        return len(self.neighboor(vertex))
    def adjacent(self,vertex1,vertex2):
        ring = self.getRing()
        return vertex1 != vertex2 and ring.union(ring.annihilator(vertex1), ring.annihilator(vertex2)) != ring.annihilator(vertex1*vertex2%self.getNumber())
    def matrixAdjencey(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if self.adjacent(i,j):
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix

class GrafMaximal(GrafofRing):
    def __init__(self, ring, operation):
        super().__init__(ring, operation)
    def getNumber(self):
        return super().getNumber()
    def getRing(self):
        return super().getRing()
    def getIdealMax(self):
        return self.getRing().idealMax()
    def vertex(self):
        return self.getRing().element()
    def edge(self):
        vertex = self.vertex()
        edge = []
        for i in vertex:
            for j in vertex:
                if self.adjacent(i,j):
                    edge.append({i,j})
        edge = self.getRing().uniq(edge)
        return list(map(tuple,edge))
    def orde(self):
        return len(self.vertex())
    def size(self):
        return len(self.edge())
    def neighboor(self,vertex):
        if vertex not in self.vertex() : 
            return "Bilangan tidak termasuk dalam himpunan titik graf"
        edge = []
        for i in self.vertex():
            if self.adjacent(i,vertex):
                edge.append(i)
        return edge
    def degree(self, vertex):
        return len(self.neighboor(vertex))
    def adjacent(self,vertex1,vertex2):
        return vertex1 != vertex2 and vertex1 in self.unionOfIdealMax() and vertex2 in self.unionOfIdealMax()
    def unionOfIdealMax(self):
        if len(self.getIdealMax()) == 0:
            return []
        if len(self.getIdealMax()) == 1:
            return [*self.getIdealMax()]
        gabungan = self.getRing().union(self.getIdealMax()[0], self.getIdealMax()[1])
        for i in self.getIdealMax():
            temp = self.getRing().union(gabungan, i)
            if len(temp) < len(gabungan):
                gabungan = [*temp]
        return gabungan
    def matrixAdjencey(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if self.adjacent(i,j):
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix
