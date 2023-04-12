texto = "buenos dias"

result = texto.upper()

print(result)

# determinando el  indice

result1 = texto[0].upper()

print(result1)

result2 = texto.lower()

print(result2)

result3 = texto.split()
print("\n Separando en elementos ")
print(result3)
print("\n Manejando un criterio de separacion utilizando la T ")
texto1 = " Este es el texto de federico"
resutlado = texto1.split("t")
print(resutlado)

print("\n Utilizando el join - que une ")

a = "Aprender"
b = "python"
c = "es"
d = "genial"

e = " ".join([a,b,c,d])

print(e)

# para buscar algo dentro del fragmento del texto

result4 = texto.find("b")

print("\n con find buscamos \n en que posicion se encuentra la letra b ──► "+str(result4))


texto2 = " buenos dias a vos "

result5 = texto2.replace("vos","todos")
print("\n utilizando replace cambiariamos el texto,"+texto2+"\n por el texto, "+result5)





