from interfaz import Interfaz
"""
 Ingresamos el valor de un numero importando la funcion geNumber 
 para poder pedirle al usuario un valor numerico que determinara
 si el numero ingresado es el mayor.
 
"""

def determinarMayor(num1, num2, num3):
    mayor = num1
    if num1 >= num2 and num1 >= num3:
        mayor = num1
    elif num2 >= num3:
        mayor = num2
    else:
        mayor = num3

    return mayor


interfaz = Interfaz()
num1 = interfaz.getNumber("\ningrese un numero por favor: ")
num2 = interfaz.getNumber("\ningrese otro numero por favor: ")
num3 = interfaz.getNumber("\ningrese uno mas numero por favor: ")
print("el numero mayor es " + str(determinarMayor(num1, num2, num3)))
