#  List ! -  estamos hablando de una estructura - no es lo mismo un array
# pero podemos hacer mas cosas que una array que es inamobible.
# esto es un dato compuesto y de diferentes tipos de dato a diferencia de los arrays que son del mismo tipo.

import os

os.system("cls")



my_list = list()
my_other_list = []
my_list = [35, 23, 26, 67, 42]
my_other_list = ["emanuel", "vidal", "C.Rivadavia 554 ", 96, 1.78, 36]

print()
print()
print(my_list)
print("Tamaño de la lista")
print(len(my_list))
print()

print("Tipo de dato")
print(type(my_other_list))
print(my_other_list)
print("Cuenta las veces que se encuentra el dato, pasado por parametro en la funcion")
print(my_other_list.count("emanuel"))  # cuanta la cantidad de elementos.

print("\npodemos desempaquetar la lista de la siguiente forma")
print("nombre, apellido, direccion, peso, altura, edad = my_other_list")
nombre, apellido, direccion, peso, altura, edad = my_other_list
print(nombre)
print("y va a imprimir el nombre de la lista " + nombre)
print()

# se pueden concatenar las listas
print("\nConcatenamos listas my_list & my_other_list")
print(my_list + my_other_list)

print()
# para incertar en la lista

print("\nutilizamos el .insert para insetar el color azul en lista")
my_other_list.insert(1, "azul")
print(my_other_list)
print()

# el remove quita el primero encontrado de la lista
print("\nutilizamos el .remove para quitar el apellido de lista")
my_other_list.remove("vidal")
print(my_other_list)
print()
print(my_list)

# con el pop puedo sacar un elemento especifico con su indice de la lista y guardarlo en otra variable.
my_pop_element = my_list.pop(2)
print("\nutilizamos el .pop(2) para quitar un valor especifico de la lista")
print(my_list)
print(my_pop_element)

# para copyar la lista completa.
my_newList = my_list.copy()
print("\n podemos también copiar con el .copy y borrar con .clear datos de la lista")
# para borrar la lista completa.
my_list.clear()

print("\nPara meter lista dentro de otra")
# Para meter una lista dentro de otra
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_mayor = []

print("\nusanado append()")
# Usando append()
lista1.append(lista2)
print(lista1)  # [1, 2, 3, [4, 5, 6]]

lista1.remove(lista2)
print("\nusanado += ")
# Usando +=
lista1 += [lista2]
print(lista1)  # [1, 2, 3, [4, 5, 6]]
lista1.remove(lista2)

print("\nusanado .apend de lista 1 y 2 para incorporarla en una gral.")
lista_mayor.append(lista1)
lista_mayor.append(lista2)
print(lista_mayor)
print("\n\n")
