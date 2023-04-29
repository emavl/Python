import re
import os

os.system("cls")

# regex o regular expression significado de  "re"

texto = " Esto es una frase para usar de modelo en la explicacion de expreciones regulares"

retorno = re.search("o", texto)

if (retorno):
    print("Se encontro")
else:
    print("No se encontro")
   
# tomar nota de esta clase    