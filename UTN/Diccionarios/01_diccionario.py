# declaramos   clave y valor, las claves no pueden repetirse

# a diferencia del valor que si se puede repetir
diccionario = { 'c1' : 'valor1', 'c2':'valor2'}
print(type(diccionario))
print("\n")
print("imprimimos el contenido de diccionario")
print(diccionario)

print("si imprimo la clave 1 me trae")

resultado = diccionario ['c1']
print(resultado)

cliente = {'nombre': (input("\ningrese un nombre ")),
           'apellido': (input("ingrese un apellido ")),
           'peso': int(input("ingrese su peso ")),
           'altura': float(input("ingrese su altura: ")),
           "lengujes":{"python","swift","kotlin"}}

print("\nconsultamos el apellido")
consulta = (cliente['apellido'])
print(consulta)

print(cliente)

# una de las particularidades es su facil acceso a los valores.
# como agregar un nuevo campo
cliente["Direccion"] = "Carabelas 124"
print(cliente)
print("\n") 

del cliente ["Direccion"]
print(cliente)
print("\n") 

print(cliente.items())
print(cliente.keys())
print(cliente.values())
# print(cliente.fromkeys())