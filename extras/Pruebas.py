from os import system

system("cls")

def pedir_caracter(mensaje, mensaje_error, min, max):

    while True:
        try:
            caracter = input(mensaje)
            if (caracter > min and caracter > max):
                raise ValueError
            break
        except ValueError:
            print(mensaje_error)

    return caracter


pedir_caracter('Ingrese una letra ', 'Error de letra', 'a', 'i')

