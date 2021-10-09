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
            if i < j :
                if cek(setVertex[i][2]+setVertex[j][2],unitSet(x)) and nipotent(setVertex[i][1]+setVertex[j][1],x) and nipotent(setVertex[i][0]+setVertex[j][0],x):
                    setUnit.append([setVertex[i],setVertex[j]])
                    print((setVertex[i],"->",setVertex[j]))
    return setUnit
def nipotent(x,n):
    for i in range(100):
        if (x**i)%n == 0:
            return True
    return False
print(len(unitGraph(3)))

                