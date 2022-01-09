import Bilangan as bil
import Graf as graf

def run(type = 'default'):
    if type == 'default':
        ring = input("masukkan ring : ")
        operation = input("masukkan operation : ")

        print(f'Ring & operation anda : ({ring}, {operation})')
        jacobs = graf.GrafJacobson(ring,operation)
        modulo = bil.Modulo(jacobs.getNumber(),operation)

        print('-'*10 +'start' + '-'*10)
        print('')
        print(f'element dari {ring} :\n{modulo.element()}')
        print('-'*25)
        print(f'element unit dari {ring} :\n{modulo.unit()}')
        print('-'*25)
        print(f'ideal maksimal dari {ring} :\n{modulo.idealMax()}')
        print('-'*25)
        print(f'jacobson dari {ring} :\n{jacobs.get_jacobson()[0]}')
        print('-'*25)
        print(f'simpul graf jacobson pada ring {ring}: \n{jacobs.vertex()}')
        print('-'*25)
        print(f'sisi graf jacobson pada ring {ring}: \n{jacobs.edge()}')
        print('-'*25)
        print('')
        print('-'*10+'end' + '-'*10)
    elif type == 'multiple':
        data = input('masukkan data: ').split(',')
        operation = input("masukkan operation : ")

        print('-'*10 +'start' + '-'*10)
        print('')
        for i in data:
            ring = 'Z_'+i
            print(f'Ring & operation anda : ({ring}, {operation})')
            jacobs = graf.GrafJacobson(ring,operation)
            modulo = bil.Modulo(jacobs.getNumber(),operation)
            print(f'element dari {ring} :\n{modulo.element()}')
            print('-'*25)
            print(f'element unit dari {ring} :\n{modulo.unit()}')
            print('-'*25)
            print(f'ideal maksimal dari {ring} :\n{modulo.idealMax()}')
            print('-'*25)
            print(f'jacobson dari {ring} :\n{jacobs.get_jacobson()}')
            print('-'*25)
            print(f'simpul graf jacobson pada ring {ring}: \n{jacobs.vertex()}')
            print('-'*25)
            print(f'sisi graf jacobson pada ring {ring}: \n{jacobs.edge()}')
            print('-'*25)
        print('')
        print('-'*10+'end' + '-'*10)
run(type='multiple')