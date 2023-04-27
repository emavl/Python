from data_stark import lista_personajes
from os import system

# reduccion de functiones

system("cls")


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
    elementos = []

    for item in list:
        if item[key] == value:
            elementos.append(item[key])
    
    for item in elementos:        
        print(elementos)
    # size = str(len(elementos)) 

    # for diccionario in list:
    #     for clave, valor in diccionario.items():
    #         if clave == 'color_pelo':
    #             print(f"la cantidad de heroes que tienen el {key} {valor} son {size}")

        # print()  # Imprime una línea en blanco después de cada diccionario



cantidad_elementos(lista_personajes, 'color_pelo','color_pelo')









