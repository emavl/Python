

# Escribir un programa que le pida al usuario que ingrese dos números enteros,
# y luego imprima "El primer número es mayor" si el primer número es mayor
# que el segundo, "El segundo número es mayor" si el segundo número es
# mayor que el primero, o "Los dos números son iguales" si los dos números
# son iguales.

numero_1 =int(input("\nPor favor ingrese un numero "))
numero_2 =int(input("\nPor favor ingrese otro numero "))

if numero_1 > numero_2:
    print("\nEl primer número es el mayor")
elif numero_1 == numero_2:
    print("\nLos numeros son iguales")
else:        
    print("\nEl segundo número es el mayor")