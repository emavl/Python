### Expreciones regulares #####
from os import system
system('cls')
import re


### Split 

# print(re.split(" ", "Bienvenido al mundo de las expreciones regulares"))
# output ----> ['Bienvenido', 'al', 'mundo', 'de', 'las', 'expreciones', 'regulares']
# me devuelve una lista 

print("##### Split ")
print()
# busca de la 'a hasta la z' y si encuentra el patron me lo devuelve como un caracter vacío
print(re.split("[a-z]", "Expreciones regulares 123")) # output -----> ['E', '', '', '', '', '', '', '', '', '', ' ', '', '', '', '', '', '', '', '', ' 123'] 
print(re.split("[a-z ]", "Expreciones regulares 123")) # output -----> ['E', '', '', '', '', '', '', '', '', '', ' ', '', '', '', '', '', '', '', '', ' 123']  y agrega el espacio de [a-z' ']
print(re.split("[a-z ]+", "Expreciones regulares 123")) # output -----> ['E', '123']
print(re.split("[0-9 ]+", "Expreciones regulares 123")) # output -----> ['Expreciones', 'regulares', '']
print(re.split("hola|chau", "hola mundo chau")) # output -----> ['', ' mundo ', '']

print()
print("##### Search ")
print()

print(re.search("como","hola como estan?").span()) # output (5, 9)
print(re.search("como","hola como estan?").start()) # output (5)
print(re.search("como","hola como estan?").end()) # output (9)
# o bien buscar numeros
print(re.search("[*0-9]","las patentes son 1542123 y debe haber 546 letras").group()) # output 1542123

texto = "las patentes son 1542123 y debe haber 546 letras"

span = re.search("[0-9]+", texto).span()

print(texto[span[0]:span[1]]) # output -----> 1542123
print()
print("##### Findall ")
print()
texto_1 = "Las patentes pueden ser 1 o 2 o 3 o 2324 "

print(re.findall("[0-9]", texto_1)) # output -----> ['1', '2', '3', '2', '3', '2', '4']
print(re.findall("[0-9]+", texto_1)) # output -----> ['1', '2', '3', '2324']
print(re.findall("[a-z]+", texto_1)) # output -----> ['1', '2', '3', '2324']
print(re.findall("[a-z]{3}", texto_1)) # output -----> ['pat', 'ent', 'pue', 'den', 'ser'] solo las minusculas
print(re.findall("[a-zA-Z]{3}", texto_1)) # output -----> ['pat', 'ent', 'pue', 'den', 'ser'] minusculas y mayusculas
print(re.findall("[a-zA-Z]{3,6}", texto_1)) # output -----> ['Las', 'patent', 'pueden', 'ser'] {minimo 3 maximo 6}

print()
print("##### Sub ")
print()

texto_2 = "buenas noches hoy es un hermoso dia"

result = re.sub("noches", "dias",texto_2)
print(result) 

fecha = "25 5 2023"
# la r determina que es una exprecion regular, por ende no va a ser necesario poner doble //
result = re.sub(r'\s','/',fecha)
print(result)




