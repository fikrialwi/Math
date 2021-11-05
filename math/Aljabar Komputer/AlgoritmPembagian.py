from sympy.abc import x, y
from sympy.polys import LM, LT, Poly, rem


def division(f,g):
    # inialisasi nilai u[n], r, dan h
    u = [0]*len(f)
    r = 0
    h = g
    lm = list(map(LM, f))
    while h != 0:
        for i in range(len(lm)):
            r = rem(lm[i],LM(h))
            if r == 0:
                u[i] += LT(h)/LT(f[i])
                h -= LT(h)/LT(f[i])*f[i]
        else:
            r += LT(h)
            h -= LT(h)
    return [u, r]
f2 = Poly(2*x*y**2+3*x+4*y**2)
f1 = Poly(y**2-2*y-2)
g = Poly(x**3*y**3+2*y**2)
print(division([f1,f2],g))
