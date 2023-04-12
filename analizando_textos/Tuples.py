"""
  conjunto de variables que son inmutables, no pueden cambiarse
las usamos por que ocupan menos espacio en memoria
se usa en estructuras que no deben de ser modificadas

"""

mi_tuple = (1,2,3,4,5)
# con integrers

# podemos tambien buscar
print(mi_tuple[1])
print(mi_tuple[-2])

segundo_tuple = 1,3,(12,33),5,6

print(segundo_tuple[2][0])

# tambien podemos asignarlo

t = 1,2,3

a,b,c = t

print(a,b,c) # siempre teniendo los mismos elementos

print(t.count(1)) # me permite saber cuantas veces aparece el valor
#dentro de mi tuple

# mas sobre tuplas - podemos trabajar con sus valores dentro pero 
# no podemos modificarlos, son si o si inmutables. 

my_tupla = (35, "emanuel", "vidal", 1.76)
print(my_tupla.index("emanuel")) # me devuelve la posicion en la cual se encuentra el indice algo que en listas no se puede 

# En una tupla no podemos asignar así como así 
# ej: my_tupla[1] = 1.80

# Para poder cambiar esos valores y que dejen de ser inmutables 
# lo pasamos a ser una Lista de la siguiente manera.

my_tupla = list(my_tupla)
print(type(my_tupla))

my_tupla.insert(2, "azul")
print(my_tupla)

# de esta manera algo que no puede cambiarse lo cambiamos por alguna razón en especial.
