import os
# 1.Contar letras: Crea una función que tome una cadena
# de texto como argumento y
# cuente el número de letras que contiene.
os.system("cls")


def cuenta_cadena(cadena: str):

    for letra in cadena:
        num_letra = cadena.index(letra)

    print(num_letra)


def main():

    texto = input("ingrese palabra ")

    cuenta_cadena(texto)


main()
