# Inicioamos con python !  
""" Comentamos multiples lineas 
    donde todo lo que coloquemos dentro
    sera visto por nosotros ! ! 
"""

nombre = input(" Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")
edad = input ("Ingrese su edad: ")
altura = input("Ingrese su altura: ")

print("Su nombre es: ")
print(nombre)
print("y su apellido es: ")
print(apellido)
print("Y su altura es: ")

#-------- P a s a j e   s t r i n g    a    N ú m e r o s -------------
""" Conversión:

Entero a decimal: 120 float(120)  ---> 120.0
Entero a string: 120  str(120)    ---> "120"
String a entero: "120" int(120)   ---> 120

"""
# Ejemplo : 
numeroUno = int(input("Ingrese un numero por favor: "))
numeroDos = int(input("Ingrese otro numero por favor: "))
total = numeroUno + numeroDos
print("el total es: ",total)
print(total) # podemos colocar de ambas formas  tanto dentro como fuera del print
