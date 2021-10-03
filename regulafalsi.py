import math
def regulaFalsi(f,a,b,n,iterate):
    for i in range(iterate+1):
        result = []
        fa = round(f(a),n)
        fb = round(f(b),n)
        c = round(b-fb*(b-a)/(fb-fa),n)
        fc = round(f(c),n)
        result.append([i,a,c,b,fa,fc,fb])
        print(result)
        if fa*fc < 0:
            b = c
        else:
            a = c
    return
def f(x):
    return math.cos(x) - math.sin(x)**2
print(regulaFalsi(f,0,3,8,12))
   