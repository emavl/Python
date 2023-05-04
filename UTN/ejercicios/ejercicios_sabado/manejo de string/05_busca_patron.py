

# 5.: Crea una función que tome dos cadenas de texto como argumentos: una cadena principal y un patrón.
# La función debe encontrar todas las ocurrencias del patrón en la cadena principal 
# y devolver una lista con las posiciones donde se encontró el patrón.

def busca_patron(string: str, patrón: str) -> None:
    
    palabras = string.split()
    ocurrencias = 0
    posicion = 0
    lista_posiciones = []
    print(palabras)
    for i in range(len(palabras)):
        if palabras[i] == patrón:
            ocurrencias += 1
            posicion = i
            lista_posiciones.append(posicion)

    

    return lista_posiciones

print(busca_patron("la casa esa la casa mas linda de todas las casas del parque", 'casa'))



