import json 
from os import system
###### json ########

system('cls')

archivo_json = open('archivos/archivo.json', 'w+')

json_datos = {
    "nombre":"Emanuel",
    "apellido":"Vidal",
    "edad":35,
    "lenguaje": ["python", "C", "C#"],
    "localidad":"Bernal"
}

##### con .dump escribimos el archivo y lo identamos #####

# json.dump(json_datos,archivo_json)

json.dump(json_datos,archivo_json,indent = 2)
# podemos identarlo para que nos quede organizado generando espacios de separacion 

archivo_json.close()

##### con el operador de archivos abro el archivo como json_file #####

with open('archivos/archivo.json') as otro_file:
    for line in otro_file:
        print (line)
        
# para solo leer el archivo utilizo load 

print ("\nutilizo load para poder cargar el archivo y lo imprimo\n"
       "al hacerlo lo asigno a una variable que pasa a ser del tipo diccionario\n")
carga_json = json.load(open('archivos/archivo.json'))
print (carga_json)
print (type(carga_json))
