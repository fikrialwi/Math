def bisection(f,a,b,it,n=7):
    print('---------Bisection---------')
    print('iterasi ke-n')
    Tabel = []
    for i in range(it+1):
        c = round((a+b)/2,n)
        fa,fb,fc = round(f(a),n),round(f(b),n), round(f(c),n)

        Tabel.append([i,a,c,b,fa,fc,fb])

        if fa*fc < 0:
            b = c
        else:
            a = c
    print(['i   a   c   b   f(a)    f(c)    f(b)'])
    for i in Tabel:
        print(f'{i}\n--------------')
    return Tabel

def bisection2(f,a,b,eps,n=7):
    print('---------Bisection---------')
    print('f(x) < epsilon')
    Tabel = []
    i = 0
    fc = 100
    while abs(fc) > eps:
        c = round((a+b)/2,n)
        fa,fb,fc = round(f(a),n),round(f(b),n), round(f(c),n)
        Tabel.append([i,a,c,b,fa,fc,fb])

        if fa*fc<0:
            b = c
        else:
            a = c
        i += 1
    print(['i   a   c   b   f(a)    f(c)    f(b)'])
    for i in Tabel:
        print(f'{i}\n--------------')
    return Tabel

def bisection3(f,a,b,eps,n=7):
    print("="*20)
    print("------Bisection-------")
    c, cLama = abs(a+b+10),(a+b)/2
    tabel = []
    i = 0
    while abs((c-cLama)/c) > eps:
        cLama = c
        c = round((a+b)/2,n)
        fa,fb,fc = round(f(a),n),round(f(b),n),round(f(c),n)
        tabel.append([i,a,c,b,fa,fc,fb, round(1-(cLama/c),n)])

        if fa*fc < 0:
            b = c
        else:
            a = c
        i += 1

    print(['i   a   c   b   f(a)    f(c)     f(b)    galat'])
    for i in tabel:
        print(i)
    return tabel