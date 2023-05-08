import re
from os import system

system('cls')

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


artista = re.findall('QUEVEDO', cadena_remplazada)
tipo = re.findall('BZRP MUSIC SESSIONS', cadena_remplazada)
numero = re.findall('52', cadena_remplazada)

reproductiones = str(tema.pop('views'))
reproductiones = re.sub('227192970', '227 M', reproductiones)

duracion = str(tema.pop('length'))
duracion = re.sub('204', '204 segundos', duracion)

codigo = re.findall('A_g3lMcWVy0', tema['img_url'])
codigo = codigo.pop(0)

fecha = re.sub('2022-07-06 00:00:00', '6/7/2022',tema['date'])

hora = re.findall('00:00', tema['date'])
hora = hora.pop(0)

numero = numero.pop(0)
artista = artista.pop(0)
tipo = tipo.pop(0)

print("Tipo : " + tipo)
print("Artista: " + artista )
print("Numero: " + numero )
print("Reproducciones: " + reproductiones )
print("Duracion: " + duracion )
print('Codigo: '+ codigo)
print('Fecha de carga: '+ fecha)
print('Hora de carga: '+ hora)
