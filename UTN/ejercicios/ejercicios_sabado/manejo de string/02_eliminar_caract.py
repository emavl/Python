# Emanuel vidal div G
#
# 2.Eliminar caracteres: Crea una función que tome una
# cadena de texto y un carácter como argumentos, y
# elimine todas las ocurrencias de ese carácter en la
# cadena.
import os
os.system("cls")


def cuenta_cadena(cadena: str, caracter: str):
    # primera opcion.
    cadena_borrada = cadena.replace(caracter, '')

    print(f"El caracter original es {cadena}")
    print(f"sin el caracter borrado quedaría {cadena_borrada}")


def cuenta_cadena2(cadena: str, caracter: str):
    # segunda opcion
    lista_cadena = []

    for letra in cadena:
        lista_cadena.append(letra)

    for letra in cadena:
        if letra == caracter:
            lista_cadena.remove(letra)

    print(f"El caracter original es {cadena}")
    print(f"sin el caracter borrado quedaría {lista_cadena}")


def main():

    cadena = input("ingrese la cadena ")
    caracter = input("ingrese el caracter a borrar ")

    cuenta_cadena2(cadena, caracter)


main()
