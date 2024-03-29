from data_stark import lista_personajes
from os import system

# forma de funciones para imprimir los heroes
# por color de ojos, pero no es la mejor manera.

system("cls")


# para buscar una clave especifica

# def listar():
#     dic = lista_personajes[0]
#     for clave in dic:
#         print (clave)


# def lista_por_color_ojos(lista_personajes: list):
#     colores = []

#     for heroe in lista_personajes:
#         colores.append(heroe['color_ojos'])

#     lista_filters = set(colores)

#     for color in lista_filters:
#         print(color)
#         for heroe in lista_personajes:
#             if color == heroe['color_ojos']:
#                 print (f"\t{heroe['nombre']}")


def listar():
    dic = lista_personajes[0]
    for clave in dic:
        print(clave)


def fx_1(lista_personajes: list):
    colores = []
    flag = True

    for heroe in lista_personajes:
        if heroe['genero'] == 'M':
            colores.append(float(heroe['altura']))

    lista_filters = set(colores)

    for altura in lista_filters:
        if flag or altura > mas_altura:
            mas_altura = altura
            flag = False

    for heroe in lista_personajes:
        if mas_altura == float(heroe['altura']):
            print(f"\t{heroe['nombre']}")


def lista_por_alturas(lista: list[dict], value: str):
    alturas = []

    for heroe in lista:
        if heroe['genero'] == value:
            alturas.append(float(heroe['altura']))

    return alturas


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


print_alturas(lista_personajes, 'M')
