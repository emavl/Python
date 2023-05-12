from os import system

system("cls")


def pedir_caracter(mensaje: str, mensaje_error: str, min: str, max: str) -> str:
    """
    Peticion al usuario de un caracter
    verificando un rango minimo y maximo.


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


# ----------------------------------------------------------------
pedir_caracter("letra","error","a","i")