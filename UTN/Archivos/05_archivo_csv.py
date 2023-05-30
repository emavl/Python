# import csv
from os import system
import re
system("cls")

######## Archivos CSV ##########

# vamos abrir el archivo de csv 
# archivo_csv = open('archivos/archivo.csv', 'w+')

# csv_escrito = csv.writer(archivo_csv, delimiter = ',')
# csv_escrito.writerow(['nombre', 'apellido', 'edad', 'lenguajes'])
# csv_escrito.writerow(['Emanuel', 'vidal', 35, 'python'])

# archivo_csv.flush()


personajes = []

with open(r"UTN\file\archivo.csv") as archivo:
    for linea in archivo:
        # Usamos expresiones regulares para buscar los valores separados por comas
        # aqui decimos con las una exprecion regular. Separar por lo que comience en ',' o salto de linea y que contengan uno o mas
        # permite buscar todas las ocurrencias  de una expresion regular y las devuelve como una lista
        campos = re.findall(r'[^,\n]+', linea)
        
        nombre = campos[0]
        apellido = campos[1]
        edad = campos[2]
        lenguajes = campos[3]
        
        # id = int(campos[0])
        # nombre = campos[1]
        # raza = campos[2]
        # if raza == "Shin-jin" or raza == "Three-Eyed People":
        #     razas = [raza]
        # else:
        #     razas = campos[2].split("-")
        # poder_pelea = int(campos[3])
        # poder_ataque = int(campos[4])
        # habilidades = campos[5].split("|$%")
        personaje = {'nombre': nombre, 'apellido':apellido, 'edad':edad, 'leguaje':lenguajes} 

        personajes.append(personaje)
        
print(personajes)        
  