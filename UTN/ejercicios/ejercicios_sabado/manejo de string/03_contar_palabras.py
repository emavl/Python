

# 3.Contar palabras: Crea una función que tome una
# cadena de texto como argumento y
#  cuente el número de palabras que contiene.
#  Suponga que las palabras están separadas por un
# espacio.


def cuenta_palabras(string: str) -> str:
    palabras = 0
    en_palabra = False

    for caracter in string:
        if caracter == ' ':
            #   Esto indica si esta dentro de la palabra o no.
            en_palabra = False
        elif not en_palabra:
            #   Por ende si no esta dentro de la palabra me suma 1 a la cantidad de palabras que tengo.
            palabras += 1
            en_palabra = True

    return palabras


print(cuenta_palabras('buenas tardes como estamos?'))
