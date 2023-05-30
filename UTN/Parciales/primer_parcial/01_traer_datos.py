from os import system
import re

system("cls")

def normalizar_datos(lista: str):
    """
    Lee un archivo de texto con información sobre personajes y devuelve una lista de diccionarios con la información normalizada.
    Args:
        lista (str): El nombre del archivo que contiene los datos a normalizar.
    Returns:
        list: Una lista de diccionarios, donde cada diccionario representa un personaje y contiene su información normalizada.
    """
    primera = True
    insumos = []
    with open(lista, encoding="utf8") as archivo:
        for linea in archivo:
            if primera:
               lista = linea
               primera = False
            else:    
             campos = re.findall(r'[^",\n]+', linea)  
             id = int(campos[0])
             nombre = campos[1]
             marca = campos[2]
             precio = float(campos[3].replace('$', ''))
             caracteristicas = campos[4].split("|!*|")
             insumo = {'id': id, 'nombre': nombre, 'marca': marca, 'precio': precio,'caracteristicas': caracteristicas}

             insumos.append(insumo)
             
    return insumos



datos = normalizar_datos(r"UTN\Parciales\primer_parcial\insumos.csv")

print(datos[0]['marca'])

# for item in datos:
#     for nombre in item:
#         print(item['marca'])
    
