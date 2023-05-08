import re
from os import system

system('cls')

cadena = "Aprendiendo expreciones regulares"
texto_a_Buscar = "Aprendiendo"

if re.search("Aprendiendo", cadena, re.I):
    print('texto encontrado')
else:
    print('texto NO encontrado')

texto_encontrado = re.search(texto_a_Buscar, cadena, re.I)

print("El  texto encontrado inicia en el caracter: ", texto_encontrado.start())
print("El  texto encontrado termina en el caracter: ", texto_encontrado.end())
print("El  texto encontrado va desde los caracteres: ", texto_encontrado.span())