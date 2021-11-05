def intLagrange(x,data):
    result = 0
    for i in range(len(data)):
        suku = data[i][1]
        for j in range(len(data)):
            if (i != j):
                suku *= (x-data[i][0])/(data[i][0]*data[j][0])
        result += suku
    return result