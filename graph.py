def unit(x):
    result = []
    for i in range(x):
        for j in range(x):
            if (i*j)%x == 1:
                result.append([i,j])
    return result
def unitSet(x):
    result = []
    for i in range(x):
        for j in range(x):
            if (i*j)%x == 1:
                result.append(i)
    return result
def combine(x):
    result = []
    for i in range(x):
        for j in range(x):
            for k in range(x):
                result.append([i,j,k])
    return result
def cek(x,X):
    return x in X
def unitGraph(x):
    setUnit = []
    setVertex = combine(x)
    for i in range(len(setVertex)):
        for j in range(len(setVertex)):
                if cek(setVertex[i][2]+setVertex[j][2],unitSet(x)) and nilpotent(setVertex[i][1]+setVertex[j][1],x) and nilpotent(setVertex[i][0]+setVertex[j][0],x):
                    setUnit.append((setVertex[i],setVertex[j]))
                    # print(f'{setVertex[i]}->{setVertex[j]}')
    return setUnit
def numEdge(x):
     return len(unitGraph(x))
def nilpotent(x,n):
    for i in range(x):
        if (x**i)%n == 0:
            return True
    return False
    
def edgeOf(x,X,n):
    result = []
    for i in X:
        if cek(x[2]+i[2],unitSet(n)) and nilpotent(x[0]+i[0],n) and nilpotent(x[1]+i[1],n):
            result.append(i)
    return result

def isPrime(x):
     if x < 2:
          return False 
     for i in range(2,x):
          if x%i == 0:
               return False
     return True
def prime(x):
     result = []
     for i in range(x+1):
          if isPrime(i):
               result.append(i)
     return result
def numVertex(x,n):
     return x**n
prima = prime(7)
for i in prima:
     print(f'e({i}) -> {numEdge(i)}')
     print(f'v({i}) -> {numVertex(i,5)}')
