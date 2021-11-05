def newtonRaphson(f,g,x,n):
    """
    f adalah fungsi
    g adalah turunan
    """
    print('---------Newton Raphson----------')
    tabel = []
    for i in range(n+1):
        tabel.append([i, x, f(x)])
        x -= f(x)/g(x)
    print('='*25)
    print(['i  x   f(x)'])
    for i in tabel:
        print(i)
    return tabel 
def newtonRaphson2(f,g,x,eps):
    print("="*20)
    print("-------Newton Raphson-------")
    print("epsilon-R < epsilon")
    """
    f adalah fungsi
    """
    xLama = x+2*eps*x
    tabel = []
    i = 0
    while abs(xLama - x)/x > eps:
        tabel.append([i, round(x,3), round(f(x),3), round(abs((xLama-x)/x),3)])
        xLama = x
        x = x - f(x)/g(x)
        i += 1
    print(['i  x   f(x)  xLama'])
    for i in tabel:
        print(i)
    return tabel 
