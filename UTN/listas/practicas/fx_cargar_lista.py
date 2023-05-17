from mi_bibliotecas import *
import os

os.system("cls")

# lista = cargar_lista_de_caracteres("\nIngrese los nombres que necesite "
#                                    "\nsi desea finalizar escriba 'salir'\n\n"
#                                    ,"\nError de tipeo !")

# print(lista)


def cargar_lista_de_caracter(mensaje, mensaje_error):
    lista = []
    texto = pedir_texto(mensaje, mensaje_error)
    lista.append(texto)
    
    return lista
 
lista = cargar_lista_de_caracter("ingrese el dia","error") 
 
   
print(lista)   
