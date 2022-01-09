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
    @abc.abstractclassmethod
    def edge(self):
        return self
    @abc.abstractclassmethod
    def vertex(self):
        return self
    @abc.abstractclassmethod
    def matrixAdjencey(self):
        return self

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
        return self.getJacobson().jacobson()
    def vertex(self):
        element = self.getJacobson().element()
        jacobson = self.getJacobson().jacobson()[0]
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
                    e = (1-(i*j))%self.getNumber()
                    if e not in self.getRing().unit():
                        edge.append({i,j})
        return self.getRing().uniq(edge)
    def degVertex(self):
        return len(self.vertex())
    def degEdge(self):
        return len(self.edge())
    def edgeofVertex(self,vertex):
        if vertex not in self.vertex() : 
            return "Bilangan tidak termasuk dalam himpunan titik graf"
        edge = []
        for i in self.vertex():
            e = (1-(i*vertex))%self.getNumber()
            if e not in self.getRing().unit():
                edge.append(i)
        return edge
    def degEdgeofVertex(self, vertex):
        return len(self.edgeofVertex(vertex))
    def isEdgeof(self,vertex1,vertex2):
        return (1-vertex1*vertex2)%self.getNumber() not in self.getRing().unit()
    def matrixAdjencey(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if i != j and self.isEdgeof(i,j):
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
                if i+j%self.getNumber() in self.getUnit():
                    edge.append(i)
        return edge
    def degVertex(self):
        return len(self.vertex())
    def degEdge(self):
        return len(self.edge())
    def edgeofVertex(self,vertex):
        if vertex not in self.vertex() : 
            return "Bilangan tidak termasuk dalam himpunan titik graf"
        edge = []
        for i in self.vertex():
            e = (i+vertex)%self.getNumber()
            if e in self.getRing().unit():
                edge.append(i)
        return edge
    def degEdgeofVertex(self, vertex):
        return len(self.edgeofVertex(vertex))
    def isEdgeof(self,vertex1,vertex2):
        return (vertex1*vertex2)%self.getNumber() in self.getRing().unit()
    def matrixAdjencey(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if i != j and self.isEdgeof(i,j):
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
                    edge.append(i)
        return edge
    def degVertex(self):
        return len(self.vertex())
    def degEdge(self):
        return len(self.edge())
    def edgeofVertex(self,vertex):
        if vertex not in self.vertex() : 
            return "Bilangan tidak termasuk dalam himpunan titik graf"
        edge = []
        for i in self.vertex():
            e = (i*vertex)%self.getNumber()
            if e ==0 :
                edge.append(i)
        return edge
    def degEdgeofVertex(self, vertex):
        return len(self.edgeofVertex(vertex))
    def isEdgeof(self,vertex1,vertex2):
        return (vertex1*vertex2)%self.getNumber() == 0
    def matrixAdjencey(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if i != j and self.isEdgeof(i,j):
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
                if i+j%self.getNumber() in self.getZeroDivisor():
                    edge.append(i)
        return edge
    def degVertex(self):
        return len(self.vertex())
    def degEdge(self):
        return len(self.edge())
    def edgeofVertex(self,vertex):
        if vertex not in self.vertex() : 
            return "Bilangan tidak termasuk dalam himpunan titik graf"
        edge = []
        for i in self.vertex():
            e = (i+vertex)%self.getNumber()
            if e in self.getZeroDivisor() :
                edge.append(i)
        return edge
    def degEdgeofVertex(self, vertex):
        return len(self.edgeofVertex(vertex))
    def isEdgeof(self,vertex1,vertex2):
        return (vertex1*vertex2)%self.getNumber() in self.getZeroDivisor()
    def matrixAdjencey(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if i != j and self.isEdgeof(i,j):
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
                if (i+j)%self.getNumber() in self.getZeroDivisor() and (i*j)%self.getNumber() == 0 :
                    edge.append(i)
        return edge
    def degVertex(self):
        return len(self.vertex())
    def degEdge(self):
        return len(self.edge())
    def edgeofVertex(self,vertex):
        if vertex not in self.vertex() : 
            return "Bilangan tidak termasuk dalam himpunan titik graf"
        edge = []
        for i in self.vertex():
            if (i+vertex)%self.getNumber() in self.getZeroDivisor() and  (i*vertex)%self.getNumber() == 0:
                edge.append(i)
        return edge
    def degEdgeofVertex(self, vertex):
        return len(self.edgeofVertex(vertex))
    def isEdgeof(self,vertex1,vertex2):
        return (vertex1*vertex2)%self.getNumber() in self.getZeroDivisor() and (vertex1+vertex2)%self.getNumber() == 0
    def matrixAdjencey(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if i != j and self.isEdgeof(i,j):
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
        return self.getUnit()
    def edge(self):
        vertex = self.vertex()
        edge = []
        for i in vertex:
            for j in vertex:
                if (i*j)%self.getNumber() == 1:
                    edge.append(i)
        return edge
    def degVertex(self):
        return len(self.vertex())
    def degEdge(self):
        return len(self.edge())
    def edgeofVertex(self,vertex):
        if vertex not in self.vertex() : 
            return "Bilangan tidak termasuk dalam himpunan titik graf"
        edge = []
        for i in self.vertex():
            if (i*vertex)%self.getNumber() == 1:
                edge.append(i)
        return edge
    def degEdgeofVertex(self, vertex):
        return len(self.edgeofVertex(vertex))
    def isEdgeof(self,vertex1,vertex2):
        return (vertex1*vertex2)%self.getNumber() == 1
    def matrixAdjencey(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if i != j and self.isEdgeof(i,j):
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix
