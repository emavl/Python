from os import system
system("cls")


##### Manejos de ficheros #####

#   >>>---------> Lectura

# lo abrimos, lo leemos (r) y lo almacenamos en la variable
# archivo = open("archivos\\prueba.txt", "r")
archivo = open("archivos\\prueba.txt", "r+")  # Leer y escribir (r+)

# print(prueba_txt.read()) # me imprime el archivo completo
# print(prueba_txt.read(19)) # esto imprime hasta el indice pasado por parametro" esto es un archivo"
# print(prueba_txt.readline()) # esto imprime la primer linea " esto es un archivo de texto plano"
# print(prueba_txt.readlines()) # esto imprime una lista  " ['esto es un archivo de texto plano\n', ...]"

for lineas in archivo.readlines(): 
    print(lineas)
    # llamamos a readlines para que me traiga 
    # todas las lineas en un listado y así printearlas 

#   >>>---------> Escritura

archivo.write("Seguimos aprendiendo ahora utilizaremos la escritura")

print(archivo.readlines())

#######################################################

# Con lo aprendido podemos crear un archivo escribirlo y también eliminarlo. 
# lo vemos en el 03_archivo

#######################################################