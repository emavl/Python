import os
from mi_biblioteca import *
os.system("cls")
# Para una veterinaria se pide clasificar el ingreso de pacientes
# hasta que el usuario quiera (se limita a 1 perrito por ingreso),
# se les pide:
# nombre,
# precio de la consulta (validar entre 500$ y 2500$)
# raza: (validar entre caniche, ovejero, siberiano)
# edad (validar 1 a 15)
# peso (entre 25 y 40 kilos) determinar:

# 1. Generar un listado con todos los datos de los pacientes ordenados por edad.
# 2. Generar un listado de los perros que pesen más de 30 kilos y ordenarla por nombre.
# 3. Si la facturación en bruto supera los 5000$, hay que agregarle un 21% de impuesto por ingresos brutos e informarlo.
# 4. Informar el nombre y el peso del perro con más peso.

# --------------- V a r i a b l e s --------------------
pacientes = []
resp = "si"


while True:

    nombre_mascota = pedir_texto("\n Ingrese el nombre del la mascotita =) ", "\n Error ! - animalucho no valido ")
    
    
    resp = pedir_texto("\ndesea continuar ? si/no \n", "Error de tipeo ")
    

    
    




























