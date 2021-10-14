def identity(x):
    col = []
    for i in range(x):
        row = []
        for j in range(x):
            if i == j:
                row.append(1)
            row.append(0)
        col.append(row)
    return col
def DekomLU(X,vec):
    n = len(X)
    y = x = [0]*n
    
    U = X
    L = identity(n)
    
    for i in range(n-1):
        if U[i][i] == 0:
            return "Pembagian dengan nol tidak bisa dilakukan"
        for j in range(i+1,n):
            rat = U[j][i]/U[i][i]
            L[j][i] = rat
            for k in range(n):
                U[j][k] -= rat*X[i][k]
    y[0] = vec[0]
    for i in range(1,n):
        y[i] = vec[i]
        for j in range(0,i):
            y[i] -= y[j]*L[i][j]
    x[n-1] = y[n-1]/U[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = y[i]
        for j in range(i+1,n):
            x[i] -= U[i][j]*x[j]
        x[i] /= U[i][i]
    print(x)
    return x
    
X = [[1,5,25],[1,8,64],[1,12,144]]
vec = [106.8,177.2,279.2]
DekomLU(X,vec)
