from os import system
import re
insumo_csv = (r"UTN\Parciales\primer_parcial\insumos.csv")


# ---------------------------------- F u n c i o n e s ------------------------------------------------

def fx_normalizar_datos(lista: str):
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

def fx_cantidad_marcas( lista: list):

    marca = {}
    
    for insumo in archivo:
        if insumo['marca'] not in marca:
            marca[insumo['marca']] = 1
        else:
            marca[insumo['marca']] += 1

    system("cls")
    print(" "+"_"*30)   
    print( f"| {'Marca':^16}|{' Cantidades':^9} |")
    print(f" "+"─"*30)
    for marca, cantidad in marca.items():
        print(f"| {marca:^15} | {cantidad:^10} |")
        print(f"─"*31)

# -------------------------------------------------------------------------------------------------------

archivo = fx_normalizar_datos(insumo_csv)

# fx_cantidad_marcas(archivo)

for caracteristicas in archivo:
    print(str(caracteristicas['caracteristicas'])+'\n')

