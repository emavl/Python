from os import system
system('cls')
#### Strings #####

texto = "   buenos dias   "
result = texto.upper()
print(result)   # ouput --------> BUENOS DIAS 

# determinando el  indice

result1 = texto[0].upper() 
print(result1)  # output -------> B

result2 = texto.lower()
print(result2) # ouput --------> buenos dias   

result3 = texto.split() 
# Devuelva una lista de las subcadenas en la cadena, usando SEP como la cadena de separador.
# Str.Split () es principalmente útil para datos que han sido delimitados intencionalmente.
# Con texto natural que incluye puntuación, considere usar el módulo de expresión regular.
print("\nSeparando en elementos con .split ")
print(result3) # ouput --------> ['buenos', 'dias']

print("\nAcomodamos el string con .strip ")
result4 = texto.strip() # Devuelva una copia de la cadena con el espacio en blanco liderante y posterior eliminado.
# Si se da Chars y no ninguno, elimine los caracteres en Chars.
print(result4) #

print("\n Manejando un criterio de separacion utilizando la T ")
texto1 = " Este es el texto de federico"
resutlado = texto1.split("t")
print(resutlado) # ouput --------> [' Es', 'e es el ', 'ex', 'o de federico']

print("\n Utilizando el join - que une ")

a = "Aprender"
b = "python"
c = "es"
d = "genial"

e = " ".join([a,b,c,d])

print(e)

# o bien puedo separar una fecha 
separador = "/"

dia = 10
mes = 7 
año = 23

fecha = separador.format(dia, mes, año)
print(fecha) #

# para buscar algo dentro del fragmento del texto

result4 = texto.find("b")

print("\n con find buscamos \n en que posicion se encuentra la letra b ──► "+str(result4))

# el indice es 3

texto2 = " buenos dias a vos "

result5 = texto2.replace("vos","todos")
print("\n utilizando replace cambiariamos el texto,"+texto2+"\n por el texto, "+result5)

# los strings son inmutables, no puedo cambiar los valores de sus indices
# por ejemplo
#nombre = "Karina"
#nombre[0] = "K"
#print(nombre)
# esto va a dar error no se cambia ni el contenido ni su nombre
print()

# podemos multiplicar los string
n1 = "kari "
n2 = "na "

print(n1*3 + n2*3) # output ------> kari kari kari na na na

print()
poema = """ Mil pequeños peces 
blancos como si hirviera
 el color del agua """
# puedo hacer saltos de linea con las 3 comillas
print(poema)
print()
print("\n utilizando in (buscando si se encuentra el string)")
# operadores de pertenencia !!!
print("agua" in poema) # output -----> True 
print("sol" in poema)  # si se encuentra en el string
# output -----> False 
print("sol" not in poema) # si no se encuentra en el string
# output -----> True 

print()
print("\n Utilizando .len ")
print("el largo es: "+ str(len(poema)))

# strings . . .

my_string = "Mi cadena"
my_other_string = "segunda cadena mas larga"
numero = "1245"
print(len(my_string))
print(len(my_other_string))

print(my_string + ", " + my_other_string + "\n\n")

print("(capitalize) " + my_string.capitalize())
print("(upper) " + my_string.upper())
print( my_string.startswith("my")) # Comienza con ( output False )
print( my_string.isnumeric()) # output False porque no es numerico
print("1".isnumeric()) # output ----> True
print(my_string.count("a")) # output ----> 2 (cuenta cuantas letras "a" encontró)
print(my_string.lower().isupper()) # output -----> False
numero = numero.zfill(6) # me va a completar con 2 Ceros a la izquierda
print(numero) # output ----> 001245
print()

# en python para crear una constante debemos hacerlo con mayusculas ej: CONST_NAME = name 







