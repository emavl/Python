from os import system
system('cls')
### Comprension de listas ###

lista_ema =['a', 'b', 'c', 'd', 'e']

# copio a la lista = [ por cada elemento en la lista_ema copialo al elemento ]
copia_lista = [ elemento for elemento in lista_ema]
print('lista copiada ' + str(copia_lista))

lista_original = [0, 1, 2, 3, 4, 5, 6, 7]
print(lista_original)

my_range = range(8)
print(list(my_range)) # puedo crear una lista con el rango

# Definición

lista = [i for i in lista_original]
print(lista)

# Por cada numero agregado a la lista le suma 1
lista = [i + 1 for i in range(8)]
print(lista)

# Por cada numero agregado a la lista lo multiplica por 2.
lista = [i * 2 for i in range(8)]
print(lista)

# Por cada numero agregado a la lista se multiplica por si mismo.
lista = [i * i for i in range(8)]
print(lista)


def sumar_cinco(number):
    return number + 5

# agregi una funcion que a cada numero agregado le va a sumar 5.
lista = [sumar_cinco(i) for i in range(8)]
print(lista)