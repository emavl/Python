import re

tema = {
    'title': 'QUEVEDO || BZRP Music Sessions #52',
    'views': 227192970,
    'length': 204,
    'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg',
    'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',
    'date': '2022-07-06 00:00:00'
}

# Tipo : BZRP MUSIC SESSIONS
# Artista: QUEVEDO
# Numero: 52
# Reproducciones: 227 M
# Duración: 204 segundos
# Codigo: A_g3lMcWVy0
# Fecha de carga:6/7/2022
# Hora de carga: 00:00

cadena_remplazada = re.sub('BZRP Music Sessions',
                           'BZRP MUSIC SESSIONS', tema['title'])
print(cadena_remplazada)
artista = re.findall('QUEVEDO', cadena_remplazada)
tipo = re.findall('BZRP MUSIC SESSIONS', cadena_remplazada)
print(artista + tipo)
