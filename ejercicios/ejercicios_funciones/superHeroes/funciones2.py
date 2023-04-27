from data_stark import lista_personajes
from os import system

# reduccion de functiones

system("cls")

def traer_caract(lista_personajes: list[dict], valor: str) -> list:
    """
    esta funcion carga a una lista,
    la caracteristica indicada por el usuario.    
    
    Args:   list -> lista de personajes
    
    return -> colores de ojos
    
    """
    elemento = []

    for heroe in lista_personajes:
        elemento.append(heroe[valor])
    
    return elemento

def listar(lista_personajes: list, key: str, value: str, mostrar: str) -> None:
    """
    esta funcion muestra el color ojolos que tienen  los personajes 
    
    Args:   
    
    list -> lista de personajes
    
    string -> color
    
    return -> None
    
    """
    for heroe in lista_personajes:
        if key == heroe[value]:
            print(f"\t{heroe[mostrar]}")


def lista_filtrada(lista_personajes: list, lista_caract: list, valor: str, decripcion_1: str, decripcion_2: str):
    """ 
    esta funcion me agrupa los personajes por color ojo
    
    Args: 
    
    list -> lista de personajes
    
    list -> lista_colores
    
    return -> None      
    
    """
    for valor in lista_caract:
        print(valor)
        listar(lista_personajes, valor,decripcion_1, decripcion_2)    


def lista_por_caracteristica(lista_personajes: list, valor: str, comparacion: str, decripcion_1: str, decripcion_2: str):

    """
    esta funcion me imprime por consola
    de forma agrupada la caracteristica que pida el usuario.  
    
    ej: los nombres que contengan cierto color de ojos.
    
    Args: 
    
    list -> lista 
    valor -> valor que voy a usar para comparar
    comparacion -> caracteristica a comparar que pida el usuario
    description_1 -> variable principal a agrupar.
    description_2 -> descripcion de lo que voy agrupar (Ej: nombre, identidad, altura etc ...)
    
    return -> None
    """
    
    caracteristica = set(traer_caract(lista_personajes,comparacion))
    lista_filtrada(lista_personajes, caracteristica, valor, decripcion_1, decripcion_2)


#lista_por_caracteristica(lista_personajes,'color','color_pelo','color_pelo','nombre')


# traer caracterisitca: me va a cargar en una lisata la caracteristica que yo le pida.
# Listar recorre la lista comparando el "valor": contra la "clave" de la caracteristica que le pida.
# lista filtrada me imprime la lista de caracteristica que le pida