
# Escribir un programa que le pida al usuario que ingrese su nombre, y luego
# imprima "Hola [nombre]" si el nombre ingresado es "Juan", "María" o "Pedro", o
# "Hola desconocido" si el nombre ingresado no es uno de esos tres.

nombre = input("\nPor favor, ingrese su nombre ")

if nombre != "Juan" and nombre != "María" and nombre != "Pedro":
    print("\n hola desconocido")    
else: 
   print("\nHola " + nombre)