from os import system
system("cls")

### Formato Texto ###


with open("UTN\\file\prueba.txt", "r") as file:
    lista = []
    for line in file:
        lista.append(line.replace("\n", ""))

for linea in lista:
    print(linea)


## Formato CSV ###


with open(r"UTN\file\personas.csv", "r") as file:
    contenido = file.read()


print(type(contenido))   # es un tipo objeto 'str'
print(contenido)   # es un tipo objeto 'str'

lista = contenido.split(r"^,")
print(lista)  # es un tipo objeto '
