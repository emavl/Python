from data_stark import lista_personajes
from os import system

# forma de funciones para imprimir los heroes 
# por color de ojos, pero no es la mejor manera.

system("cls")


# para buscar una clave especifica

def listar():
    dic = lista_personajes[0]
    for clave in dic:
        print (clave)


def lista_por_color_ojos(lista_personajes: list):
    colores = []
    
    for heroe in lista_personajes:
        colores.append(heroe['color_ojos'])
        
    lista_filters = set(colores)
    
    for color in lista_filters:
        print(color)
        for heroe in lista_personajes:
            if color == heroe['color_ojos']:
                print (f"\t{heroe['nombre']}")  



lista_por_color_ojos(lista_personajes)