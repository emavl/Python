#  List ! -  estamos hablando de una estructura - no es lo mismo un array 
# pero podemos hacer mas cosas que una array que es inamobible. 
# esto es un dato compuesto y de diferentes tipos de dato a diferencia de los arrays que son del mismo tipo.



my_list = list()

my_other_list = []

print(len(my_list))

my_list = [35,23,26,67,42]

print(my_list)
print(len(my_list))

my_other_list = [43, 2.34, "emanuel", "vidal",43]

print(type(my_other_list))
print(my_other_list)
print( my_list.count(43)) # cuanta la cantidad de elementos.

# podemos desempaquetar la lista de la siguiente forma
edad, altura, nombre, apellido, fortuna = my_other_list

print("y va a imprimir el nombre de la lista " + nombre)
print()

# se pueden concatenar las listas 

print ( my_list + my_other_list)

print()
# para incertar en la lista 

my_other_list.insert(1,"azul")
print(my_other_list)
print()

# el remove quita el primero encontrado de la lista
my_other_list.remove("vidal")
print(my_other_list)
print()
print(my_list)

# con el pop puedo sacar un elemento especifico con su indice de la lista y guardarlo en otra variable.  
my_pop_element = my_list.pop(2)
print(my_list)
print(my_pop_element)

# para copyar la lista completa.
my_newList = my_list.copy()

# para borrar la lista completa.
my_list.clear()




