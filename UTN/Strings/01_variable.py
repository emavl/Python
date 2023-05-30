from os import system
system("cls")

# declaro y defino la variable
nombre = "lucas"
print(nombre)

# redefino
nombre = "pedro"
print(nombre)
# bienvenida = "hola " + nombre + " ¿Como estas?"

# para concatenar de otra manera
bienvenida = f"hola {nombre} ¿como estas?"

print(bienvenida)
# para borrar una variable alojada en memoria utilizaremos el "DEL" ej
del nombre
# print(nombre)

cadena = "hola"

print(list(cadena))
print(tuple(cadena))
print(set(cadena))