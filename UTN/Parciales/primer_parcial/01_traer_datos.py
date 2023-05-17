from os import system
import csv

system("cls")

primera = True
insumos = []

with open("Parciales\\Primer_parcial\\insumos.csv", "r", encoding="utf-8") as file:

    lisata_deListas = csv.reader(file)

    for lista in lisata_deListas:
        if primera:
            llaves = lista
            primera = False
        else:
            diccionario = {}


# imprimo insumos
# for insumo in insumos:
#     print(insumo)

# print(type(insumos))
print(llaves)
