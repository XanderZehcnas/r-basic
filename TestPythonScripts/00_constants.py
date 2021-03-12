# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Constantes en python
import math
math.pi
math.tau
math.nan
math.inf
print("Pi="+str(math.pi))


# Representacion numerica
print(math.ceil(3.75))
math.floor(3.2)
math.trunc(3.6)

print(math.copysign(3,-2))

math.fabs(-5.0)
math.factorial(3)

print(2**5)

x=5
y=2

z = math.factorial(x) / (math.factorial(y) * math.factorial(x-y))
print(z)

# Obtener el resto (x%y solo enteros)
math.fmod(5,3)
math.remainder(5, 2)

print(math.modf(5.25))

# Numeros muy cercanos entre si
math.isclose(2,2)

#Maximo comun divisor
print(math.gcd(27,3))
