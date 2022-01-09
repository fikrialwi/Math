def unitZ(n):
    unit = []
    for i in range(n):
        for j in range(n):
            if i != j and i*j%n == 1:
                unit.append(i)
    return unit