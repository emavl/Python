1.Contar letras: Crea una función que tome una cadena de texto como argumento y
 cuente el número de letras que contiene.
```py

def cuenta_cadena(cadena:str):
    
    for letra in cadena:
        num_letra = cadena.index(letra)

    print(num_letra)  
    
def main():
    
    texto = input("ingrese palabra ")
    
    cuenta_cadena(texto)

main()

```

2.Eliminar caracteres: Crea una función que tome una
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

3.Contar palabras: Crea una función que tome una
cadena de texto como argumento y
 cuente el número de palabras que contiene.
 Suponga que las palabras están separadas por un
espacio.

4.Reemplazar palabras: Crea una función que tome una cadena de texto, una palabra y otra palabra como
argumentos, y reemplace todas las ocurrencias de la
primera palabra por la segunda en la cadena.

5.Buscar patrón: Crea una función que tome dos cadenas de texto como argumentos: una cadena principal y un
patrón. La función debe encontrar todas las ocurrencias del patrón en la cadena principal y devolver una lista con las posiciones donde se encontró el patrón.