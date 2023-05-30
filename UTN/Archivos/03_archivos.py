from os import system
# import os
system("cls")

######  Creando un archivos ##### 

# va a intentar leer el archivo como no existe lo crea 
archivo = open(r"UTN\file\mi_archivo.txt","w+") # Lo abro en lectura/escritura

archivo.write("\nCreamos y abrimos el archivo nuevo")

for line in archivo.readlines():
    print(line)

archivo.close()

# y si quisiera eliminar ese archivo utilizo
# os.remove("./archivos/mi_archivo.txt")

# luego vuelvo abrirlo para poder leerlo
archivo = open("UTN\\file\mi_archivo.txt", "r+") 

for line in archivo.readlines():
    print(line)
    
archivo.close()