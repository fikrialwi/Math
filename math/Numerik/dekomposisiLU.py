import numpy as np
def dekomLU(A,v):
    print('------Dekomposisi LU-------')
    n = len(A)
    y = x = [0]*n

    print(f'A =\n{A}')

    U = A
    L = np.eye(n)

    for i in range(n-1):
        if U[i][i] == 0.0:
            print('ora iso porogapit kambek 0')
            return U
        for j in range(i+1,n):
            rasio = U[j][i]/U[i][i]
            L[j][i] = rasio

            for k in range(n):
                U[j][k] -= rasio*A[i][k]
            
            print("-"*25)
            print(f'L =\n{L}')
            print(f'U =\n{U}')
    y[0] = v[0]

    for i in range(1,n):
        y[i] = v[i]
        for j in range(0,i):
            y[i] -= y[j]*L[i][j]
    print(f'y : \n{y}')

    x[n-1] = y[n-1]/U[i][i]

    for i in range(n-2,-1,-1):
        x[i] = y[i]

        for j in range(i+1,n):
            x[i] -= U[i][j]*x[j]
        x[i] /= U[i][i]
    print('Solution :')
    for i, j in enumerate(x):
        print(f'x{i}: {j}')
    return x