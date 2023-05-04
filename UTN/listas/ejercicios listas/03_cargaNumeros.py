from mi_biblioteca import *
import os
# Realizar una carga indefinida de números
# , añadirlos a una lista e indicar 
# que posición de memoria es la que mas ocurrencias
# tiene dentro de esa lista.

ocurrencias = {}
numeros = []
resp = "si"
concurrencia = 0

while resp.lower() == "si":
    
    numero = pedir_numero("\nIngrese un numero por favor ───► ")
    numeros.append(numero)
    
    resp = input("\nDesea continuar ───► si/ no ")
    os.system("cls") 
    
 
        
print(f"la posicion de memoria {}")        
