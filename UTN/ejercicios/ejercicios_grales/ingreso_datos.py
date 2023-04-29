cliente = {}

for i in range(0, 2):
    cliente = {'nombre': (input("ingrese un nombre ")),
               'apellido': (input("ingrese un apellido "))}

for clave,valor in cliente.values():
    print(f"su {clave} y su apellido es {valor}")


nombre = {}
apellido = {}
cliente = {}

for i in range(0, 3):
    nombre[i] = input("\n ingrese su nombre ")
    apellido[i] = input(" ingrese su apellido ")

for i in nombre:
    print(f"su nombre es {nombre[i]} y su apellido es {apellido[i]}")

