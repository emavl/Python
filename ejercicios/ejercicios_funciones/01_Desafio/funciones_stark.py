from os import system
from data_stark import lista_personajes

system("cls")


# ----------------------- F u n c i o n e s -----------------------

def limpiar_consola() -> None:
    """ Funcion que limpia a consola """
    print("\n")
    system("pause")
    system("cls")


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


def ejecutar_menu():
    opcion = pedir_numero_min_max("=================================\n"
                                  "         Stark Industries        \n"
                                  "=================================\n"
                                  " 1) listar por héroe por genero M \n"
                                  " 2) listar por héroe por genero F \n"
                                  " 3) Héroe más alto\n"
                                  " 4) Heroína mas alta\n"
                                  " 5) Heroína mas baja\n"
                                  " 6) Promedio altura de los héroes\n"
                                  " 7) Promedio altura de las heroínas\n"
                                  " 8) Nombre del superhéroe asociado a los puntos ( C a F )\n"
                                  " 9) Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n"
                                  "10) Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n"
                                  "11) Listar por tipo de inteligencia 'si lo tiene'\n"
                                  "12) Listar todos los superhéroes agrupados por color de ojos.\n"
                                  "13) Listar todos los superhéroes agrupados por color de pelo.\n"
                                  "14) Listar todos los superhéroes agrupados por tipo de inteligencia.\n"
                                  "15) salir.\n"
                                  "\n opcion n° ────► ",
                                  "\nError, Thanos ira a por ti, escribe bien ‼ \n", 1, 15)
    return opcion

# ----------------------- L i s t a r   p o r   c a r a c t e r i s t i c a  -------------------


def traer_caract(lista: list[dict], key: str) -> list:
    """
    esta funcion carga a una lista,
    la caracteristica indicada por el usuario.    

    Args:   list -> lista de personajes

    return -> colores de ojos

    """
    elemento = []

    for heroe in lista:
        elemento.append(heroe[key])

    return elemento


def listar(lista_personajes: list[dict], valor: str, comparacion: str, imprime: str) -> None:
    """
    esta funcion muestra el color ojolos que tienen  los personajes 

    Args:   

    list -> lista de personajes

    string -> color

    return -> None

    """
    for heroe in lista_personajes:
        if valor == heroe[comparacion]:
            print(f"\t{heroe[imprime]}")


def lista_filtrada(lista_personajes: list[dict], lista_caract: list, valor: str, decripcion_1: str, decripcion_2: str):
    """ 
    esta funcion me agrupa los personajes por color ojo

    Args: 

    list -> lista de personajes

    list -> lista_colores

    return -> None      

    """
    for valor in lista_caract:
        print(valor)
        listar(lista_personajes, valor, decripcion_1, decripcion_2)


def lista_por_caracteristica(lista_personajes: list[dict], valor: str, comparacion: str, decripcion_1: str, decripcion_2: str):
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

    caracteristica = set(traer_caract(lista_personajes, comparacion))
    lista_filtrada(lista_personajes, caracteristica,
                   valor, decripcion_1, decripcion_2)

    # "nombre": "Howard the Duck",
    # "identidad": "Howard (Last name unrevealed)",
    # "empresa": "Marvel Comics",
    # "altura": "79.349999999999994",
    # "peso": "18.449999999999999",
    # "genero": "M",
    # "color_ojos": "Brown",
    # "color_pelo": "Yellow",
    # "fuerza": "2",
    # "inteligencia": ""

# ------------------------  L i s t a s   A g r u p a d a s -------------------


def agregar_segun_caract(lista: list[dict], key: str, value: str):
    elementos = []

    for item in lista:
        if item[key] == value:
            elementos.append(item[key])

    return elementos


def listar_por_keyValue(lista: list[dict], key: str, value: str, imprime: str) -> None:

    for item in lista:
        print("\n"+key + " " + item + "\n")
    for heroe in lista_personajes:
        if item == heroe[key] and heroe[key] == value:
            print(f"\t{heroe[imprime]}")


def lista_agrupada(lista: list[dict], key: str, value: str, imprime: str) -> None:

    lista_seteada = set(agregar_segun_caract(lista, key, value))
    listar_por_keyValue(lista_seteada, key, value, imprime)


def tipo_inteligencia():

    lista_agrupada(lista_personajes, 'inteligencia', 'average', 'nombre')
    lista_agrupada(lista_personajes, 'inteligencia', 'good', 'nombre')
    lista_agrupada(lista_personajes, 'inteligencia', 'high', 'nombre')

# ------------------------  L i s t a s   D e t e r m i n a d a s -------------------


def cantidad_elementos(list: list, key: str, value: str):
    elementos = 0

    for item in list:
        if item[key] == value:
            elementos += 1

    return elementos


def determinar_caract(lista: list, key: str):

    lista_set = set(traer_caract(lista, key))

    for item in lista_set:
        ret = cantidad_elementos(lista, key, item)
        print(
            f"\n la cantidad de heroes que tienen el {key} {item} son ---> {ret}")

# ----------------------- L i s t a s  -   A l t u r a  -----------------------


def lista_por_alturas(lista: list[dict], value: str):
    alturas = []

    for heroe in lista:
        if heroe['genero'] == value:
            alturas.append(float(heroe['altura']))

    return alturas


def set_alturas(lista: list[dict]):
    flag = True
    lista_filters = set(lista)

    for altura in lista_filters:
        if flag or altura > mas_altura:
            mas_altura = altura
            flag = False

    for heroe in lista_personajes:
        if mas_altura == float(heroe['altura']):
            print(f"\t{heroe['nombre']}")


def set_altura_baja(lista: list[dict]):
    flag = True
    lista_filters = set(lista)

    for altura in lista_filters:
        if flag or altura < mas_baja:
            mas_baja = altura
            flag = False

    for heroe in lista_personajes:
        if mas_baja == float(heroe['altura']):
            print(f"\t{heroe['nombre']}")


def print_alturas(lista: list[dict], value: str):

    altura = lista_por_alturas(lista, value)
    set_alturas(altura)


def print_altura_baja(lista: list[dict], value: str):

    altura = lista_por_alturas(lista, value)
    set_altura_baja(altura)

# ------------- P r o m e d i o s --------------


def promedio_alturas(lista: list[dict]):
    acc = 0
    suma = 0

    for altura in lista:
        suma += float(altura)
        acc += 1

    promedio = suma/acc
    if promedio > 200:
        print(f"El promedio de la altura en los heroes es {promedio:.2f}\n")
    else:
        print(f"El promedio de la altura de las heroinas es {promedio:.2f}\n")


def print_alturas_promedio(lista: list[dict], value: str):

    altura = lista_por_alturas(lista, value)
    promedio_alturas(altura)

# ----------------------- M e n ú   -   P r i n c i p a l  -----------------------


def codigo_principal():

    while True:
        match (ejecutar_menu()):
            case 1:  # 1) listar por héroe por genero M
                system("cls")
                lista_agrupada(lista_personajes, 'genero', 'M', 'nombre')
                limpiar_consola()
            case 2:  # 2) listar por héroe por genero F
                system("cls")
                lista_agrupada(lista_personajes, 'genero', 'F', 'nombre')
                limpiar_consola()
            case 3:  # 3) Héroe más alto
                system("cls")
                print_alturas(lista_personajes, 'M')
                limpiar_consola()
                pass
            case 4:  # 4) Heroína mas alta
                system("cls")
                print_alturas(lista_personajes, 'F')
                limpiar_consola()
            case 5:  # 5) Heroína mas baja
                system("cls")
                print_altura_baja(lista_personajes, 'F')
                limpiar_consola()
            case 6:  # 6) Promedio altura de los héroes
                system("cls")
                print_alturas_promedio(lista_personajes, 'M')
                limpiar_consola()
            case 7:  # 7) Promedio altura de las heroínas TODO
                system("cls")
                print_alturas_promedio(lista_personajes, 'F')
                limpiar_consola()
                pass
            # 8) Nombre del superhéroe asociado a los puntos ( C a F ) TODO
            case 8:

                pass
            case 9:  # Determinar cuántos superhéroes tienen cada tipo de color de ojos.
                system("cls")
                determinar_caract(lista_personajes, 'color_ojos')
                limpiar_consola()
                pass
            case 10:  # Determinar cuántos superhéroes tienen cada tipo de color de pelo.
                system("cls")
                determinar_caract(lista_personajes, 'color_pelo')
                limpiar_consola()
                pass
            case 11:  # ------> Listar por tipo de inteligencia 'si lo tiene'
                system("cls")
                tipo_inteligencia()
                limpiar_consola()
                pass
            # ------> Listar todos los superhéroes agrupados por color de ojos.
            case 12:
                system("cls")
                lista_por_caracteristica(
                    lista_personajes, 'color', 'color_ojos', 'color_ojos', 'nombre')
                limpiar_consola()
            # ------> Listar todos los superhéroes agrupados por color de pelo.
            case 13:
                system("cls")
                lista_por_caracteristica(
                    lista_personajes, 'color', 'color_pelo', 'color_pelo', 'nombre')
                limpiar_consola()
            case 14:  # 14) Listar todos los superhéroes agrupados por tipo de inteligencia. TODO
                system("cls")
                lista_por_caracteristica(
                    lista_personajes, 'inteligencia', 'inteligencia', 'inteligencia', 'nombre')
                limpiar_consola()
            case 15:
                break
