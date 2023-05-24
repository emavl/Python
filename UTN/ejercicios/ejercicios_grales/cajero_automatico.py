from os import system
import os
system('cls')
# Hacer un programa que simule un cajero automatico con un saldo inicial de $1000
# y tendrá el siguiente menú

# 1. ingresar dinero en la cuenta
# 2. Retirar dinero.
# 3. Mostrar dinero disponible
# 4.Salir


def limpiar_consola():
    print("\n")
    os.system("pause")
    os.system("cls")


def pedir_numero_min_max(mensaje, mensaje_error, min, max):
    while True:
        try:
            num = int(input(mensaje))
            if num > min and num > max:
                raise ValueError
            break
        except ValueError:
            print(mensaje_error)

    return num


def ejecutar_menu():
    opcion = pedir_numero_min_max("=================================\n"
                                  "       Bienvenido a Bancthon     \n"
                                  "=================================\n"
                                  " Que desea hacer ?\n"
                                  "1. Ingresar dinero a la cuenta\n"
                                  "2. Retirar dinero de la cuenta\n"
                                  "3. Mostrar dinero disponible\n"
                                  "4. Salir\n",
                                  "\nError, escriba una opcion correcta \n", 1, 4)
    return opcion


def ingreso_en_cuenta(monto: int) -> int:

    if monto == 1000:
        print("Recuerde que cuenta con un monto inicial de $1000\n")

    saldo = pedir_numero_min_max(
        "\nIngrese el dinero a la cuenta ", "error valor invalido", 0, 100000000000000000)

    saldo_total = saldo + monto

    return saldo_total


def retiro_de_cuenta(monto: int) -> int:

    if monto == 1000:
        print("Recuerde que cuenta con un monto inicial de $1000\n")

    while True:
        saldo = pedir_numero_min_max(
            "\nIngrese el dinero que va a retirar de la cuenta ", "error valor invalido", 0, 100000000000000000)
        saldo_total = monto - saldo

        if saldo_total < 0:
            print("\nNo puede retirar esa cantidad de dinero de la cuenta")
        else:
            break

    return saldo_total


def main():

    flag = True

    while True:
        if flag:
            saldo = 1000

        match (ejecutar_menu()):
            case 1:
                system("cls")
                saldo = ingreso_en_cuenta(saldo)
                flag = False
                limpiar_consola()
            case 2:
                system("cls")
                saldo = retiro_de_cuenta(saldo)
                flag = False
                limpiar_consola()
            case 3:
                system("cls")
                print(f"Saldo disponible {saldo}")
                limpiar_consola()
            case 4:
                system('cls')
                print("\nGracias por utilizar nuestros servicios ...")
                break


main()
