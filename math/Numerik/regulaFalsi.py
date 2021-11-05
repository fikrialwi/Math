from math import sin,cos
def regulaFalsi(f,a,b,it,n = 8):
    print('-'*20)
    print('Regula Falsi')
    print('-'*20)
    fa = f(a)
    fb = f(b)

    tabel = []

    for i in range(it+1):
        fa,fb = round(f(a),n),round(f(b),n)

        c = round(b - fb*(b-a)/(fb-fa),n)
        fc = round(f(c),n)

        tabel.append([i,a,c,b,fa,fc,fb])

        if fa*fc < 0:
            b = c
        else:
            a = c
    print('Tabel : \n')
    print('i  a  c  b  fa  fb  fc')
    for i in tabel:
        print(f'{i}')
        print('-'*10)
    return tabel
f = lambda x: cos(x)-sin(x**2) 
def regulaFalsi2(f,a,b,eps,n = 8):
    print('-'*20)
    print('Regula Falsi')
    print('-'*20)
    tabel = []
    fa = f(a)
    fb = f(b)
    c = b - fb*(b-a)/(fb-fa)
    fc = f(c)
    tabel.append([0,a,c,b,fa,fc,fb])
    i = 1
    while abs(fc) > eps:
        if fa * fc < 0:
            b = c
        else:
            a = c
        fa = round(f(a),n)
        fb = round(f(b),n)
        c = round(b-fb*(b-a)/(fb-fa),n) 
        fc = round(f(c),n)
        tabel.append([i,a,c,b,fa,fc,fb])
        i+=1
    print('Tabel :\n')
    print('[i  a   c    b   f(a)   f(c)   f(b)]')
    for i in tabel:
        print(f'{i}')
        print('-'*10)
    return tabel

regulaFalsi2(f = f, a = 0, b = 3, eps = 0.00001)