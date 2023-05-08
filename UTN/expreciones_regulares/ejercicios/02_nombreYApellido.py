import re

nombre = 'Juan carlos'
apellido = 'hernandez'

""" Una forma de hacerlo """

print('Nombre encontrado' if re.match('juan', nombre, re.I)
      else 'nombre NO encontrado')

print('Apellido encontrado' if re.search('andez', apellido, re.I)
      else 'apellido NO encontrado')


""" Otra forma de hacerlo """

# if re.match('juan', nombre, re.I):
#     print('Nombre encontrado')
# else:
#     print('Nombre NO encontrado')

# if re.search('andez', apellido, re.I):
#     print('Apellido encontrado')
# else:
#     ('apellido NO encontrado')
