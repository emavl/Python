import os


def pedir_texto(mensaje: str, mensaje_error: str) -> str:
    """chequea que el texto igresado
    por el usuario no contenga numeros,
    espacio o salto de linea, retornando el texto.

    Arg:
        mensaje (str) ──► Peticion del usuario en formato string.
        mensaje_error (str) ──► Error del dato ingresado.

    Return:
        Texto (str) ──► El string ingresado.
    """
    while True:
        try:
            texto = input(mensaje)
            size = texto.split()
            for i in size:
                if i.isalpha():
                    break
                raise ValueError
            break
        except ValueError:
            print(mensaje_error)

    return texto


def pedir_caracter(mensaje: str, mensaje_error: str, min: str, max: str) -> str:
    """
    Peticion al usuario de un caracter
    verificando un rango minimo y maximo.

    arg:

    mensaje (str) -> Mensaje del usuario para peticion de datos.
    mensaje_error (str) -> mensaje de error

    min (str) -> valor inicial de min.
    max (str) -> valor final de max.

    """
    while True:
        try:
            caracter = input(mensaje)
            if caracter > min and caracter > max:
                raise ValueError
            break
        except ValueError:
            print(mensaje_error)

    return caracter


def pedir_numero_min_max(mensaje, mensaje_error, min, max):
    while True:
        try:
            num = int(input(mensaje))
            if num > min and num < max:
                raise ValueError
            break
        except ValueError:
            print(mensaje_error)

    return num


def pedir_numero(mensaje: str, mensaje_error: str) -> int:
     
    """
    Peticion al usuario de un numero
    
    arg:

    mensaje (str) -> Mensaje del usuario para peticion de datos.
    mensaje_error (str) -> mensaje de error

    """     
    while True:
        try:
            num = input(mensaje)
            if num.isalpha:
                num = int(num)
                raise ValueError
            break
        except ValueError:
            print(mensaje_error)

    return num

def limpiar_consola():
    print("\n")
    os.system("pause")
    os.system("cls")


def cargar_lista_de_caracter(mensaje: str, mensaje_error: str) -> list:
    """Recive el ingreso de un string simple o compuesto

    Arg:
        mensaje (str) ──► Peticion del usuario en formato string.
        mensaje_error (str) ──► Error del dato ingresado.

    Return:
        Lista (str) ──► El string ingresado.
    """
    lista = []
    texto = pedir_texto(mensaje, mensaje_error)
    lista.append(texto)

    return lista


def cargar_lista_de_caracteres(mensaje, mensaje_error):
    lista = []
    while True:
        texto = pedir_texto(mensaje, mensaje_error)
        if texto == "salir":
            break
        lista.append(texto)
    return lista


def cargar_lista_numerica(mensaje, mensaje_error):
    lista = []
    while True:
        texto = pedir_numero(mensaje, mensaje_error)
        if texto == "salir":
            break
        lista.append(texto)
    return lista


def cargar_lista_numerica_min_max(mensaje, mensaje_error, minimo, maximo):
    lista = []
    while True:
        texto = pedir_numero_min_max(mensaje, mensaje_error, minimo, maximo)
        if texto == "salir":
            break
        lista.append(texto)
    return lista
