def gaussSeidel(A,v,nIter = 10):
    print("-"*20)
    print(f"Metode Gauss Seidel")
    print("-"*20)
    n = len(A)
    nAwal = [0]*n
    x = [0]*n
    p = [0]*n
    x = nAwal[:]
    for i in range(n):
        res = 0
        for j in range(n):
            res+= A[i][j]*x[j]
        p[i] = res
    Tabel = []
    Tabel.append(['0']+nAwal+p)

    for i in range(nIter):
        for j in range(n):
            row = 0
            for k in range(n):
                if j != k:
                    row += A[j][k]*x[k]
            x[j] = (v[j]-row)/A[j][j]
        for j in range(n):
            hasil = 0
            for k in range(n):
                hasil += A[j][k]*x[k]
            p[j] = hasil

        Tabel.append([i+1]+x+p)
    print("="*20)
    print(f"Tabel:\n")
    for i in Tabel:
        print(i)
    return Tabel
# gaussSeidel(A,v,nAwal,nIter)