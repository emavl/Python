
# Escribir un programa que le pida al usuario que ingrese un número entero
# positivo, y luego imprima 
#  "El número ingresado es positivo" si el número es mayor que cero,
# "El número ingresado es cero o negativo" si el número es menor o igual a cero.

numero =int(input("\nPor favor ingrese un numero positivo "))

if numero > 0:
    print("\nEl numero ingresado es positivo")
else:
    print("\nEl numero es cero o negativo")
        