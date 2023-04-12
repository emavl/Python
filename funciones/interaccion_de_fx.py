from random import shuffle

# Lista de palitos
palitos = ['-' ,'--' ,'---' ,'----']


# Mezclar palitos
def mezcla(lista):
    shuffle(lista)
    return lista


# probar suerte

def probar_suerte():
    intento = ''
    while intento not in ['2' ,'1' ,'3' ,'4']:
        intento = input("\nElige un numero del 1 al 4")

        return int(intento)
