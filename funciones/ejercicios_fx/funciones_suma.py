listaNumeros = []


def carga_numeros(lista):
    decision = ''
    numero_usuario = int(input("\nPor favor, introduzca un numero ───► "))
    listaNumeros.append(numero_usuario)
    decision = input("\n¿Desea añadir otro numero?")

    while decision == 'si' or decision == 'SI':
        numero_usuario = int(input("\nPor favor, introduzca otro numero ───► "))
        lista.append(numero_usuario)
        decision = input("\n¿Desea añadir mas numeros?")

        suma(lista)


def suma(lista):
    total = 0

    for arg in lista:
        total += arg

    return print("\n La suma es " + str(total))


carga_numeros(listaNumeros)

print(type(listaNumeros))

