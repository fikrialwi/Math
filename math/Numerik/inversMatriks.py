import numpy as np

def matrInv(A,v):
    n = len(A)
    x = [0]*n
    
    a = np.zeros((n,2*n))

    for i in range(n):
        for j in range(n):
            a[i][j] = A[i][j]
    for i in range(n):
        for j in range(n):
            a[i][j+n] = 1
    
    print(f"A = {a[:,:3]}")
    print(f"A' = {a[:,3:]}")
    print("-"*20)

    for i in range(n):
        if a[i][i] == 0.0:
            print("sepurane gak iso diitung kui")
            break
        for j in range(n):
            if i != j:
                rasio = a[j][i]/a[i][i]

                for k in range(2*n):
                    a[j][k] -= rasio * a[i][k]
                
                print(f"A = \n{a[:,:3]}")
                print(f"A' = \n{a[:,3:]}")

                print("-"*20)
    for i in range(n):
        div = a[i][i]
        for j in range(2*n):
            a[i][j] /= div

    print(f"A = {a[:,:3]}")
    print(f"A' = {a[:,3:]}")

    inv = a[:,3:]
    for i in range(n):
        result = 0
        for j in range(n):
            result += inv[i][j]*v[j]
        x[i] = result

    print(f"x = {x}")
    return x

A = [[4,-1,-1],[-2,6,1],[-1,1,7]]
v = [3,9,-6]

matrInv(A,v)
           
