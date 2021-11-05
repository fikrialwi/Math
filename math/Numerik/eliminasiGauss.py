def elimGauss(A):
    print('-'*20)
    print('Eliminasi Gauss')
    print('-'*20)
    n = len(A)
    print(f'A = \n {A}')
    x = [0]*n
    for i in range(len(A)):
        if A[i][i] == 0.0:
            print("Ora iso bagi karo 0.0 bos")
            return
        for j in range(i+1,n):
            rasio = A[j][i]/A[i][i]

            for k in range(n+1):
                A[j][k] -= rasio * A[i][k]
        print("-"*25)
        print(f"A = {A}")

    for i in range(n):
        rasio = A[i][i]
        for j in range(n+1):
            A[i][j] /= rasio
    print("-"*25)
    print(f"A = {A}")

    for i in range(n-1,0,-1):
        for j in range(i-1,-1,-1):
            rasio =  A[j][i]
            for k in range(n+1):
                A[j][k] -= rasio*A[i][k]
        print(f'A = \n{A}')

    for i in range(n):
        x[i] = A[i][n]
    print("Solution :\n")
    for i,j in enumerate(x):
        print(f'x{i} : {j}')
    return x 

A = [[2,3,-1,5],[4,4,-3,3],[-2,3,-1,1]]

elimGauss(A)