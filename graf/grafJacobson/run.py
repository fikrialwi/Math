import Bilangan as bil
import Graf as gf
import networkx as nx
import matplotlib.pyplot as m

class show():
    def __init__(self):
        self.graph = input('masukkan jenis graf : ')
        self.run()
    g={
        'jacobson':gf.GrafJacobson,
        'annihilator':gf.GrafAnnihilator,
        'unit':gf.GrafUnit,
        'zero divisor':gf.GrafZeroDivisor,
        'total zero divisor':gf.GrafTotalZeroDivisor,
        'total':gf.GrafTotal
    }
    
    
    def run(self):
        number = input("masukkan angka : ").split(',')
        operation = input("masukkan operation : ")
        if len(number) == 1:
            self.temp(self.g[self.graph],number[0],operation)
            ring = 'Z_'+number[0]
            G = nx.Graph()
            graf = self.g[self.graph](ring,operation)
            G.add_nodes_from(graf.vertex())
            G.add_edges_from(graf.edge())
            nx.draw_circular(G, with_labels = True, node_color='r', edge_color='b', font_weight='300', font_color='w', font_size='small')

        else:
            for i,e in enumerate(number):
                self.temp(self.g[self.graph],e,operation)
                ring = 'Z_'+e
                G = nx.Graph()
                graf = self.g[self.graph](ring,operation)
                G.add_nodes_from(graf.vertex())
                G.add_edges_from(graf.edge())
                nx.draw_circular(G, with_labels = True, node_color='r', edge_color='b', font_weight='300', font_color='w', font_size='small')
                ax = m.subplot(len(number)//2,3,i+1)
        m.show()
    def temp(self,graph, number, operation):
        print(f'Ring & operation anda : (Z_{number}, {operation})')
        ring = 'Z_'+number
        graf = graph(ring,operation)
        modulo = bil.Modulo(graf.getNumber(),operation)

        print('-'*10 +'start' + '-'*10)
        print('')
        print(f'element dari {number} :\n{modulo.element()}')
        print('-'*25)
        print(f'simpul graf {self.get_key(graph)} pada ring Z_{number}: \n{graf.vertex()}')
        print('-'*25)
        print(f'sisi graf {self.get_key(graph)} pada ring Z_{number}: \n{graf.edge()}')
        print('-'*25)
        print(f'orde dari graf {self.get_key(graph)} pada ring Z_{number}: \n{graf.orde()}')
        print('-'*25)
        print(f'size dari graf {self.get_key(graph)} pada ring Z_{number}: \n{graf.size()}')
        print('-'*25)
        print('')
        print('-'*10+'end' + '-'*10)
    def get_key(self,val):
        for key, value in self.g.items():
            if val == value:
                return key
        return "key doesn't exist"
show()
