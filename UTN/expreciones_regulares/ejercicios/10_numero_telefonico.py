import re
from os import system

system("cls")

texto = "Mi numero es +54 11 4635-1238"

patron = r'\+\d{2}\s\d{2}\s\d{4}-\d{4}'

remplazo = re.sub(patron,"(numero oculto)",texto)

print(remplazo)