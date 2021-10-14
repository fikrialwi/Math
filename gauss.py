def gauss(X):
    n = len(X)
    x = [0]*n
    for i in range(n):
        if X[i][i] == 0.0:
            return "Sorry can't excute" 
        for j in range(i+1,n):
            rat = X[j][i]/X[i][i]
            for k in range(n+1):
                X[j][k] = X[j][k] - rat*X[i][k]
    print(X)
    x[n-1] = X[n-1][n]/X[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = X[i][n]
        for j in range(i+1,n):
            x[i] -= X[i][j]*x[j]
        x[i] /= X[i][i]
        print(x[i])
    print(x)
    return x
X = [[2,3,4,7],[2,-1,1,4],[1,3,-5,2]]
gauss(X)
