import Bilangan as bil
import Graf as gf
import networkx as nx
import matplotlib.pyplot as m
import TopologiIndex as ti

class show():
    def __init__(self):
        self.graph = input('masukkan jenis graf : ').lower()
        self.run()
    g={
        'jacobson':gf.GrafJacobson,
        'annihilator':gf.GrafAnnihilator,
        'unit':gf.GrafUnit,
        'zero divisor':gf.GrafZeroDivisor,
        'total zero divisor':gf.GrafTotalZeroDivisor,
        'total':gf.GrafTotal,
        'identity':gf.GrafIdentity,
        'maximal': gf.GrafMaximal,
    }
    t = {
        'first zagreb': ti.FirstZagreb,
        'second zagreb' : ti.SecondZagreb,
        'first multiple zagreb': ti.FirstMultipleZagreb,
        'second multiple zagreb': ti.SecondMultipleZagreb,
        'narumi katayama': ti.NarumiKatayama,
        'radic': ti.Randic,
        'forgotten': ti.ForgottenTopological,
        'reciprocal radic': ti.ReciprocalRandic,
        'reduce reciprocal radic': ti.ReducedReciprocalRandic,
        'first zagreb coindex': ti.FirstZagrebCoindex,
        'second zagreb coindex': ti.SecondZagrebCoindex,
        'reduced second zagreb': ti.ReducedSecondZagreb,
        'abc': ti.AtomBondConectivity,
        'harmonic': ti.Harmonic,
        '4th abc': ti.FouthVersionABC,
        'augmented zagreb': ti.AugmentedZagreb,
        'geometric aritmethic': ti.GeometricAritmethic,
        '5th ga': ti.FifthVersionGA,
        'sum connectivity': ti.SumConnectivity
    }
    
    def run(self):
        number = input("masukkan angka : ").split(',')
        operation = input("masukkan operation : ")
        topologi = input('masukkan topologi indeks : ').lower()
        for i,e in enumerate(number):
            self.temp_graph(self.g[self.graph],e,operation)
            ring = 'Z_'+e
            G = nx.Graph()
            graf = self.g[self.graph](ring,operation)
            G.add_nodes_from(graf.vertex())
            G.add_edges_from(graf.edge())
            nx.draw_circular(G, with_labels = True, node_color='r', edge_color='b', font_weight='300', font_color='w', font_size='small')
            if topologi != False:
                self.temp_topologi(graf,topologi)
            m.savefig(f'hasil/img/graf {self.graph} pada {ring}')
            self.create(ring,operation,self.graph,topologi)
    def temp_graph(self,graph, number, operation):
        print(f'Ring & operation anda : (Z_{number}, {operation})')
        ring = 'Z_'+number
        graf = graph(ring,operation)
        modulo = bil.Modulo(graf.getNumber(),operation)

        print('-'*10 +'start' + '-'*10)
        print('')
        print(f'element dari {number} :\n{modulo.element()}')
        print('-'*25)
        print(f'simpul graf {self.get_key(graph,self.g)} pada ring Z_{number}: \n{graf.vertex()}')
        print('-'*25)
        print(f'sisi graf {self.get_key(graph,self.g)} pada ring Z_{number}: \n{graf.edge()}')
        print('-'*25)
        print(f'orde dari graf {self.get_key(graph,self.g)} pada ring Z_{number}: \n{graf.orde()}')
        print('-'*25)
        print(f'size dari graf {self.get_key(graph,self.g)} pada ring Z_{number}: \n{graf.size()}')
        print('-'*25)
        print('')
        print('-'*10+'end' + '-'*10)
    def get_key(self,val,arr):
        for key, value in arr.items():
            if val == value:
                return key
        return "key doesn't exist"
    def temp_topologi(self, graph, topologi):
        print(f'indeks {topologi}nya adalah {self.t[topologi](graph).topologi()}')
    def create(self, ring, operator, graph, topologi):
        f = open(f"hasil/graf {graph} pada {ring} dan topologi {topologi}.txt", "w")
        graf = self.g[graph](ring,operator)
        topo = self.t[topologi](graf)
        text = f'graf : {graph}\nring : {ring}\noperator : {operator}\n\tsimpul : {graf.vertex()}\n\tsisi : {graf.edge()}\n\torde : {graf.orde()}\n\tsize : {graf.size()}\n =============== \n\ttopologi indeks : {topologi} => nilainya : {topo.topologi()}'
        f.write(text)
show()
