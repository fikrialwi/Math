def biseks(f,a,b,n,iterate):
    result = []
    for i in range(iterate+1):
        c = round((a+b)/2,c)
        fa,fb,fc = round(f(a),n), round(f(b),n), round(f(c),n)
        result.append([i,a,c,b,fa,fc,fb])
        print(result)
        if fa*fc < 0:
            b = c
        a = c
    return