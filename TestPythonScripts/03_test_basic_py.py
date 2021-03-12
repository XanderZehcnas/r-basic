# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 16:35:28 2021

@author: Rhiznab
"""
# Tests exercise python


#Pregunta 1
x = float(input("Introduce un número real:"))
if (x >= 0):
    print("Numero positivo")
else:
    print("Numero negativo")

#Pregunta 2
x = float(input("Introduce un número real:"))
if (x >= -5 and x <= 5):
    print("Numero en el rango")
    
#Pregunta 3
x = int(input("Introduce coordenada X:"))
y = int(input("Introduce coordenada Y:"))
if (x>=0):
    if (y>=0):
        print("1º cuadrante")
    else:
        print("4º cuadrante")
else:
    if (y>=0):
        print("2º cuadrante")
    else:
        print("3º cuadrante")
        
#Pregunta 4
a = int(input("Introduce 1º numero:"))
b = int(input("Introduce 2º numero:"))
print("El cociente es " + str(a/b))
print("El resto es " + str(a%b))

#pregunta 5
import math
z = int(input("Introduce entero para ver si es cuadrado perfecto:"))
raiz = math.sqrt(z)
if (raiz.is_integer()):
    print("ES un cuadrado perfecto")
    
#pregunta 6
def bisiesto(x):
    return (x%4 == 0 and (x%100 != 0 or x%400 == 0))

print("Año 16: " + str(bisiesto(16)))
print("Año 2000: " + str(bisiesto(2000)))
print("Año 2100: " + str(bisiesto(2100)))
print("Año 2800: " + str(bisiesto(2800)))

#pregunta 7
ltr = input("Introduce letra entre a y h:")
num = int(input("Introduce numero entre 1 y 8:"))
letras = ["a","b","c","d","e","f","g","h"]
if (ltr in letras and num > 0 and num < 9):
    if (letras.index(ltr,0,8)%2 == 0 ^ num%2 == 0):
        print("Blanca")
    else:
        print("Negra")
else:
    print("Error")