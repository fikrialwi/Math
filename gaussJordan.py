def gaussJordan(X):
    n = len(X)
    x = [0]*n
    
    for i in range(n):
        if X[i][i] == 0.0:
            return "Pembagian dengan nol tidak dapat dilakukan"
        for j in range(i+1,n):
            rat = X[j][i]/X[i][i]
            for k in range(n+1):
                X[j][k] = X[j][k] - rat*X[i][k]
        print(X)
    for i in range(n):
        rat = X[i][i]
        for j in range(n+1):
            X[i][j] /= rat
    for i in range(n-1,0,-1):
        for j in range(i-1,-1,-1):
            rat = X[j][i]
            for k in range(n+1):
                X[j][k] -= rat*X[i][k]
    for i in range(n):
        x[i] = X[i][n]
    print(f'solution : {x}')
    return x
X = [[3,-0.1,-0.2,7.85],[0.1,7,-0.5,-19.3],[0.3,-0.2,10,71.4]]
gaussJordan(X)
            
