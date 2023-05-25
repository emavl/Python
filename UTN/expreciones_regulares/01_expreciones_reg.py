import re
from os import system

##  M a t c h 

system("cls")
# tratan de ispeccionar una cadena de texto
print("-"*40)
print("-"*40)
print("## Match\n")
mi_cadena = "Esto se trata de expresiones regulares, donde trata las repeticiones"
mi_cadena2 = "Esto no va a tratase de expresiones regulares"


print("imprimo el match\n"
      "donde uno me muestra que encontro algo dentro del texto\n"
      "y en donde no pudo me imprime None")

print(re.match("Esto se trata", mi_cadena2))
print(re.match("Esto se trata", mi_cadena))
match = re.match("Esto se trata", mi_cadena)
print(match)

print("-"*40)

print("\n imprimo span\n que es una tupla formada por dos valores el que inicia y el que termina")
comienzo, final = match.span()
print(f"donde el comienzo es {comienzo} y el final es {final}")

print("-"*40)

# para comprobar el None podemos utilizar estas 3 formas
# if not(match == None)
# if match != None:
print("\nChequeamos , si mach no es None con un condicional")

if match is not None:
    print("contiene el texto")
else:
    print("No contiene el texto")


###    S e a r c h


print()
print("-"*40)
print("-"*40)
print("## search\n")

buscar = re.search("Esto se trata", mi_cadena, re.I)
print(buscar)
comienzo, final = buscar.span()
print(f"donde el comienzo es {comienzo} y el final es {final}")

print(mi_cadena[comienzo:final])



print()
print("-"*40)
print("-"*40)
print("## Findall\n")

encontrar_todo = re.findall("trata", mi_cadena, re.I)
print("Findall nos muestra la cantidad de ocurrencias colocandolo en una lista")
print(encontrar_todo)
txt = "Modelo de expliiiicacion de expreciones"
print("Como tambien nos muestra la cantidad de ocurrencias de la misma si estan repetidas")
print(re.findall("i+", txt)) # Donde el + significa(encontrame la letra i más en el caso de ser repetidas)
print("\nPuedo pedirle que me encuentre todos los espacios en blanco")

print(re.findall(" ", txt)) 

print()
print("-"*40)
print("-"*40)
print("## split\n")
print("## split, nos va a separar a donde le indiquemos por ejemplo\n")
mi_otraCadena = "Clase 1: Aprendemos expreciones regulares"
print(re.split(":", mi_otraCadena))


print("-"*40)
print("-"*40)
print("## Sub\n")
print("Nos permite reemplazar\n")
mi_cadena3 =" esta Leccion es para darnos una leccion de una list"
print(mi_cadena)
# reemplazo parte de la cadena por otra
print(re.sub("Esto se trata","hoy vamos a hablar", mi_cadena))
print(re.sub("leccion","LECCION", mi_cadena3))
print(re.sub("leccion|Leccion","LECCION", mi_cadena3))
print(re.sub("[l|L]eccion","LECCION", mi_cadena3))


print("-"*40)
print("-"*40)
print("## Conjunto de caracteres: \n")

print("Donde el grupo contiene [a-e]")
print(re.findall("[a-e]", mi_cadena3))

print("Donde el grupo contiene [a-e]")
regex_pattern = r'[Mm]anzana' # este corchete significa A o a
txt = 'La Manzana y la banana son frutas. Un viejo dicho dice que una manzana y una banana al día mantiene al médico muy lejos.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Manzana', 'manzana']