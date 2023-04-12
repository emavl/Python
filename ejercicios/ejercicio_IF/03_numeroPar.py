
# Escribir un programa que le pida al usuario que ingrese un número entero, y
# luego imprima "El número ingresado es par" si el número es divisible por 2, o
# "El número ingresado es impar" si el número no es divisible por 2.

numero =int(input("\nPor favor ingrese un numero positivo "))

if numero % 2 == 0:
    print("\nEl numero ingresado es par")
else:
    print("\nEl numero ingresado es impar")
        