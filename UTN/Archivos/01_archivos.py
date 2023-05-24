from os import system
system("cls")

with open("archivos/prueba.txt","r") as file:
    lista = []
    for line in file:
        lista.append(line.replace("\n",""))
    
for linea in lista:        
    print (linea)