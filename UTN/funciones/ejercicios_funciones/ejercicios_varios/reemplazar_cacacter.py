from os import system

system("cls")

def reemplazar_caract(cadena:str, letra:str, reemplazo:str):
    lista = list(cadena)
    contador = 0
    
    for i in range(len(lista)):
        if lista[i] == letra:
            lista[i] = reemplazo
            contador += 1
    cadena = "".join(lista)
    
    return (cadena, contador)
            
   
print(reemplazar_caract("Hola mundo", 'u','uuu'))    
print(type(reemplazar_caract("Hola mundo", 'u','uuu')))    
        