# Manejo de strings

[Contar letras -](#contar-letras)
[Eliminar caracter -](#eliminar-caracteres)
[Contar palabras -](#contar-palabras)
[remplazar palabras -](#reemplazar-palabras)
[Buscar palabras -](#buscar-patrón)

## *Contar letras*

1. Crea una función que tome una cadena de texto como argumento y
 cuente el número de letras que contiene.

```py

def cuenta_cadena(cadena:str):
    
    for letra in cadena:
        num_letra = cadena.index(letra)

    print(num_letra)  
    
cuenta_cadena('hola buenas noches')

```

## *Eliminar caracteres*

2 - Crea una función que tome una
cadena de texto y un carácter como argumentos, y
elimine todas las ocurrencias de ese carácter en la
cadena.

```py
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

```

****
  
## Contar palabras

3; Crea una función que tome una
cadena de texto como argumento y
 cuente el número de palabras que contiene.
 Suponga que las palabras están separadas por un
espacio.

```py

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

```

****

## Reemplazar palabras

****
4; Crea una función que tome una cadena de texto, una palabra y otra palabra como
argumentos, y reemplace todas las ocurrencias de la
primera palabra por la segunda en la cadena.

```py


def reemplazar_palabra(cadena: str, palabra1: str, palabra2: str):
    # Separo las cadenas en una lista.
    palabras = cadena.split()
    i = 0

    # Itéro a través de las palabras y reemplazar si corresponde
    for i in range(len(palabras)):
        if palabras[i] == palabra1:
            palabras[i] = palabra2

    nueva_cadena = ' '.join(palabras)

    return nueva_cadena

print(reemplazar_palabra("hola buena gente como andan?", 'buena','soleado')) 

```

## *Buscar patrón*

5.: Crea una función que tome dos cadenas de texto como argumentos: una cadena principal y un
patrón. La función debe encontrar todas las ocurrencias del patrón en la cadena principal y devolver una lista con las posiciones donde se encontró el patrón.

```python


def busca_patron(string: str, patrón: str) -> None:
    
    palabras = string.split()
    ocurrencias = 0
    posicion = 0
    lista_posiciones = []

    print(palabras)
    for i in range(len(palabras)):
        if palabras[i] == patrón:
            ocurrencias += 1
            posicion = i
            lista_posiciones.append(posicion)

    return lista_posiciones

print(busca_patron("la casa esa la casa mas linda de todas las casas del parque", 'casa'))


```
