def iterJacobi(A,v,nIter=10):
    print("-----------\nMetode Iterasi Jacobi\n-----------")
    n = len(A)
    x = [0]*n
    nAwal = x[:]
    p = x[:]
    print(f"A = {A}")
    print("="*10)
    for i in range(n):
        res = 0
        for j in range(n):
            res += A[i][j]*x[j]
        p[i] = res

    Tabel = []
    Tabel = [[0]+nAwal+p]
    for i in range(nIter):
        xLama = x[:]
        for j in range(n):
            row  = 0
            for k in range(n):
                if j != k:
                    row += A[j][k]*xLama[k]
            x[j] = (v[j]-row)/A[j][j]
        for j in range(n):
            hasil = 0
            for k in range(n):
                hasil += A[j][k]*x[k]
            p[j] = hasil
        Tabel.append([str(i+1)]+x+p)
    print("="*20)
    print(f"Tabel:\n")
    for i in Tabel:
        print(i)
    return Tabel