from sympy.physics.mechanics import *

q1, q2 = dynamicsymbols('q1 q2')
q1d, q2d = dynamicsymbols('q1 q2', 1)
L = q1d**2 + q2d**2

LM = LagrangesMethod(L, [q1, q2])

mechanics_printing(pretty_print=False)
equations = LM.form_lagranges_equations()

print(equations)
