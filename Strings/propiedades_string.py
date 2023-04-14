# los strings son inmutables, no puedo cambiar los valores de sus indices
# por ejemplo
#nombre = "Karina"
#nombre[0] = "K"
#print(nombre)
# esto va a dar error no se cambia ni el contenido ni su nombre

# podemos multiplicar los string
n1 = "kari "
n2 = "na "

print(n1*3 + n2*3)

poema = """ Mil pequeños peces 
blancos como si hirviera
 el color del agua """
# puedo hacer saltos de linea con las 3 comillas
print(poema)

# operadores de pertenencia !!!
print("agua" in poema)
print("sol" in poema)  # si se encuentra en el string
print("sol" not in poema) # si no se encuentra en el string

print("el largo es: "+ str(len(poema)))

# strings . . .

my_string = "Mi cadena"
my_other_string = "segunda cadena mas larga"

print(len(my_string))
print(len(my_other_string))

print(my_string + ", " + my_other_string + "\n\n")

print("(capitalize) " + my_string.capitalize())
print("(upper) " + my_string.upper())
print( my_string.startswith("my"))
print( my_string.isnumeric())
print("1".isnumeric())
print(my_string.count("a"))
print(my_string.lower().isupper())
print()

# en python para crear una constante debemos hacerlo con mayusculas ej: CONST_NAME = name 

