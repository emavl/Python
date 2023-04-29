# Diferentes formas de formateo
from unicodedata import numeric

numero1 = 10
numero2 = 15

print("\n\nLos valores son "+str(numero1)+" y "+str(numero2))

# utilizando el format

print("\nLos valores son {} y {} ".format(numero1,numero2))

# reutilizando  mas codigo.

print("\nLos suma de los valores {} y {} es ──► {} ".format(numero1,numero2,numero1+numero2))

# con otro tipo de datos

color = "rojo"
matricula = 51233

print(f"\n El auto es {color} y su matricula es {matricula}")