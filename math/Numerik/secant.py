def secant(f,a,b,it):
    print("="*20)
    print('------Metode Secant--------')
    tabel = [[0,a,round(f(a),6)],[1,b,round(f(b),6)]]
    for i in range(2,it):
        c = a - f(a)*(b-a)/(f(b)-f(a))
        fc = f(c)

        tabel.append([i,round(c,3),round(fc,6)])
        a,b = b,c
    print('Tabel :\n')
    print(['i  c   f(c)'])
    for i in tabel:
        print(i)
    return tabel
