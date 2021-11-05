# from sympy.polys import GroebnerBasis
from sympy.polys.polytools import LM, LT, groebner, lcm, rem, div
from sympy.abc import z,y,x
from sympy.polys import Poly

f1 = Poly(2*x**2*y+x**3*z+y**2*z)
f2 = Poly(3*z**2+x**2*y**2)
f3 = Poly(y*z+x*y)

print(groebner([f1,f2,f3],z,y,x,order = 'lex'))
print(groebner([f1,f2,f3],z,y,x,order = 'grevlex'))
print(groebner([f1,f2,f3],x,y,z,order = 'lex'))
print(groebner([f1,f2,f3],x,y,z,order = 'grevlex'))