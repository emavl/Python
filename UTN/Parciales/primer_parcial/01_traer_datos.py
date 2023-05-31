from os import system
import re

system("cls")

# ---------------------------------- F u n c i o n e s ------------------------------------------------

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
             marca = campos[2].strip()
             precio = float(campos[3].replace('$', ''))
             caracteristicas = campos[4].split("|!*|")
             insumo = {'id': id, 'nombre': nombre, 'marca': marca, 'precio': precio,'caracteristicas': caracteristicas}

             insumos.append(insumo)
             
    print("Se han cargado los datos del archivo Insumos.csv correctamente")
        
    return insumos





# -------------------------------------------------------------------------------------------------------

archivo = normalizar_datos("insumos.csv")

# print(datos[2])

dic_marcas = {'marca': None ,'cantidad': None}



# muestro las marcas.
# for item in datos[]['marca']:
#        print(item)


# for item in datos:
#     for nombre in item:
#        for key,value in dic_marcas.items():
#         dic_marcas[key] = item['marca']
#     print(dic_marcas)
  
marca = {}
lista = []  
  
for insumo in archivo:
    if insumo['marca'] not in marca:
        marca[insumo['marca']] = 1
    else:
        marca[insumo['marca']] += 1

print("| marca | cantidad |")
for marca, cantidad in marca.items():
    print(f" {marca},  {cantidad}")
        

