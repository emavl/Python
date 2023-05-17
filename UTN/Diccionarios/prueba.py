from os import system
system("cls")

mi_diccionario = {}

print(mi_diccionario)
num_claves = int(input("Ingrese el número de claves que desea agregar: "))

for _ in range(num_claves):
    clave = input(f"Ingrese la clave: {mi_diccionario}")
    valor = input("Ingrese el valor para la clave '{}': ".format(clave))
    mi_diccionario[clave] = valor

print(mi_diccionario)
