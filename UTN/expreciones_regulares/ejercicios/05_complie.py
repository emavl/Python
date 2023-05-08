import re
from os import system

system('cls')

# Con expresiones regulares, podremos buscar todo tipo de patrones
# Por ejemplo, podremos filtrar las palabras con acentos

patron = ('w*[ñáéíóúÑÁÉÍÓÚ]w*')
palabras = re.compile(patron)
print(palabras.findall("Niño, Acción, Perro, Lobo, Expresión, Español"))

