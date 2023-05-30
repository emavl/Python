import json 
from os import system
###### json  ------>  Java Script objet nototation ########

# es un standard que nacio en javaScipt y fue adoptado en otros lenguajes de programacion para la transferencia de datos
# por ejemplo cuando un cliente y un servidor tienen que transferir datos o informacion lo hacen en formato jason, el mismo es de tipo string 

# su equivalencia sería un diccionario de python, donde tenemos claves y valores con el mismo formato 

# XML es un archivo de texto plano, antes se diagramaba así pero fue superado 
# por el formato json ya que ocupa menos caracteres y es mas facil de leer
# es menos berboso --> se utilizan menos caracteres + legible 

# En todos los lenguajes vamos a encontrar alguna funcion o biblioteca  que nos permite convertir 
# un objeto en memoria, a una cadena en formato json o viceberza.


system('cls')

archivo_json = open(r'UTN\file\archivo.json', 'w+')

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

with open(r'UTN\file\archivo.json') as otro_file:
    for line in otro_file:
        print (line)
        
# para solo leer el archivo utilizo load 

print ("\nutilizo load para poder cargar el archivo y lo imprimo\n"
       "al hacerlo lo asigno a una variable que pasa a ser del tipo diccionario\n")
carga_json = json.load(open('UTN\\file\\archivo.json'))
print (carga_json)
print (type(carga_json))
