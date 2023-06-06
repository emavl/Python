import re
from os import system

system('cls')

def buscar_caracteristica(input_text, caracteristicas):
    # completions = [caracteristica for caracteristica in caracteristicas if re.findall(input_text, caracteristica, re.IGNORECASE)]

    lista = []
    for caracteristica in caracteristicas:
        if re.findall(input_text, caracteristica, re.IGNORECASE):
            lista.append(caracteristica)
            
    return lista


caracterisitcas = ["color", "size","Resolución Full HD", "500gb", "compatible con linux", "compatible con windows"]

# Solicitar entrada del usuario
caract = input("Ingrese una característica: ")
caract_encontrada = buscar_caracteristica(caract, caracterisitcas)   

if len(caract_encontrada) > 0:
    print("Opciones sugeridas:")
    for item in caract_encontrada:
        print(item)
else:
    print("no se encontro esa caracteristica")