from os import system
system("cls")
# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc

### Dictionaries ###

# Definición
print('---------> Definicion\n')

mi_diccionario = dict()
otro_diccionario = {}


print("imprimo el tipo")
print(type(mi_diccionario))
print(type(otro_diccionario))

print()

otro_diccionario = {"Nombre": "Brais",
                 "Apellido": "Moure", "Edad": 35, 1: "Python"}

mi_diccionario = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print('diccionario 1 ')
print(mi_diccionario)
print()
print('diccionario 2 ')
print(otro_diccionario)
print()

print('Tamaño de los diccionarios ')
print('diccionario 1') 
print(len(mi_diccionario))
print('diccionario 2') 
print(len(otro_diccionario))

print()
# Búsqueda
print('-------> Busqueda\n')

print('Busco en la clave 1')
print(mi_diccionario[1]) # Me imprime el 1.77
print()
print('Busco en la clave nombre')
print(mi_diccionario["Nombre"])
print()

print('Moure esta en el mi diccionario?')
print("Moure" in mi_diccionario) # es falso porque buscamos por clave no por valor 
print("Apellido" in mi_diccionario) # True

# Inserción
print()
print('Inserción')

mi_diccionario["Calle"] = "Calle MoureDev"
print(mi_diccionario)

print()
print('Actualización')
# Actualización

mi_diccionario["Nombre"] = "Pedro"
print('Agrego el nombre ' + mi_diccionario["Nombre"])

print()
print('eliminacion')
# Eliminación

print('\nElimino la \'calle\'')
del mi_diccionario["Calle"]
print(mi_diccionario)

print()
# Otras operaciones
print('Otras operaciones')

print('\ndiccionario.items')
print(mi_diccionario.items())
print()
print('diccionario.keys')
print(mi_diccionario.keys())
print()
print('diccionario.values')
print(mi_diccionario.values())
print()

mi_diccionario = {}

num_claves = int(input("Ingrese el número de claves que desea agregar: "))

for _ in range(num_claves):
    clave = input("Ingrese la clave: ")
    valor = input("Ingrese el valor para la clave '{}': ".format(clave))
    mi_diccionario[clave] = valor

print(mi_diccionario)

lista_keys = ["Nombre","Apellido", "Piso", "localidad"]


print()
print(' ────────── Agrego las keys ────────────')
print()
nuevo_diccionario = dict.fromkeys(lista_keys)
print(nuevo_diccionario)
print()
print('Agrego las keys harcodeadas')
nuevo_diccionario = dict.fromkeys(("Nombre", "Apellido", "Piso", "localidad"))
print(nuevo_diccionario)
print()
print('Creo un diccionario nuevo sin valores - solo uso las keys')
nuevo_diccionario = dict.fromkeys(mi_diccionario)
print(nuevo_diccionario)
print()
nuevo_diccionario = dict.fromkeys(mi_diccionario, "Emanuel")
print(nuevo_diccionario)
print()
print()
print(' ────────── Agrego los values ────────────')

lista_values = ["Emanuel", "Vidal", 1, "Bernal"]

for key in nuevo_diccionario:
    nuevo_diccionario[key] = input(f'ingrese el {key} por favor ')
print()
print(nuevo_diccionario)

print("──────────────────────────────────────")

print('que tipo es')
my_values = nuevo_diccionario.values()
print(type(my_values))
print()

print('Con .values imprimo solo los valores')
print(nuevo_diccionario.values())
print()

print('Muestro solo los valor')
print(list(dict.fromkeys(list(nuevo_diccionario.values())).keys()))
print()
print('En cada caso tendremos una estructura diferente')
print()
print('lista')
print(list(nuevo_diccionario))
print()
print('tupla')
print(tuple(nuevo_diccionario))
print()
print('set')
print(set(nuevo_diccionario))
print()