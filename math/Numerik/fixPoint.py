def fixPoint(x,f,g,n):
    g = g(x)
    f = f(x)
    table = []
    for i in range(n):
        table.append([i,x,g,f])
        x = g
        f = f(x)
        g = g(x)
    print('-------Fix Point--------')
    for i in table:
        print(i)
        print('---------')
    return table
