from data_stark import lista_personajes
from os import system

# reduccion de functiones

system("cls")


def traer_caract(list: list[dict], valor: str) -> list:
    """
    esta funcion carga a una lista,
    la caracteristica indicada por el usuario.    

    Args:   list -> lista de personajes

    return -> colores de ojos

    """
    elemento = []

    for heroe in list:
        elemento.append(heroe[valor])

    return elemento

def agregar_segun_caract(lista_personajes: list, key: str, value: str):
    elementos = []

    for item in lista_personajes:
        if item[key] == value:
            elementos.append(item[key])

    return elementos

def listar_por_keyValue(lista: list, key: str, value: str, imprime: str) -> None:

    for item in lista:
        print("\n"+key + " " + item + "\n")
    for heroe in lista_personajes:
        if item == heroe[key] and heroe[key] == value:
            print(f"\t{heroe[imprime]}")

def lista_agrupada(lista_personajes: list, key: str, value: str, imprime: str) -> None:

    lista_seteada = set(agregar_segun_caract(lista_personajes, key, value))
    listar_por_keyValue(lista_seteada, key, value, imprime)

def tipo_inteligencia():

    lista_agrupada(lista_personajes, 'inteligencia', 'average', 'nombre')
    lista_agrupada(lista_personajes, 'inteligencia', 'good', 'nombre')
    lista_agrupada(lista_personajes, 'inteligencia', 'high', 'nombre')

def cantidad_elementos(list: list, key: str, value: str):
    elementos = 0

    for item in list:
        if item[key] == value:
            elementos += 1

    return elementos

def iteraciones(lista: list, key: str):

    lista_set = set(traer_caract(lista, key))

    for item in lista_set:
        ret = cantidad_elementos(lista, key, item)
        print(
            f"\n la cantidad de heroes que tienen el {key} {item} son ---> {ret}")



def pedir_numero_min_max(mensaje, mensaje_error, min, max):

    while True:
        try:
            num = int(input(mensaje))
            if (num < min or num > max):
                raise ValueError
            break
        except ValueError:
            print(mensaje_error)

    return num



