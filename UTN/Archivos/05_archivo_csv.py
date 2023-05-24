import csv
from os import system
system("cls")

######## Archivos CSV ##########

# vamos abrir el archivo de csv 
archivo_csv = open('archivos/archivo.csv', 'w+')

csv_escrito = csv.writer(archivo_csv, delimiter = ',')
csv_escrito.writerow(['nombre', 'apellido', 'edad', 'lenguajes'])
csv_escrito.writerow(['Emanuel', 'vidal', 35, 'python'])


