import re
from os import system
system('cls')

# La cadena en la que se buscarán los patrones
text = "La fecha es 23/06/2021 y el telefono es +54-9-1124256338"

# El patrón a buscar.
# aca se busca 2 veces un numero donde ----> \d de digito {2} luego una barra y así ... etc
pattern = r"\d{2}/\d{2}/\d{4}"

# El texto con el que se reemplazará el patrón
remplazo = "Fecha oculta"

# Remplaza todas las apariciones del patrón en la cadena de texto.
nuevo_texto = re.sub(pattern, remplazo, text)

print(" texto modificado: ", nuevo_texto)
