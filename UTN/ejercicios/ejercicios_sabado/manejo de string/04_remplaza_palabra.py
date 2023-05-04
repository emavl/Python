from os import system

# 4.Reemplazar palabras:
# Crea una función que tome una cadena de texto
# , una palabra y otra palabra como
# argumentos, y reemplace todas las ocurrencias de la
# primera palabra por la segunda en la cadena.

system('cls')


def reemplazar_palabra(cadena: str, palabra1: str, palabra2: str):
    # Separo las cadenas en una lista.
    palabras = cadena.split()

    # Itéro a través de las palabras y reemplazar si corresponde
    for i in range(len(palabras)):
        if palabras[i] == palabra1:
            palabras[i] = palabra2

    nueva_cadena = ' '.join(palabras)

    return nueva_cadena


print(reemplazar_palabra("hola buena gente como andan?", 'buena', 'soleado'))
