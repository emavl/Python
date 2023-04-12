text = "ABCDEFGHIJKLMN"
#             [desde : hasta ]
fragmento = text[2:5]
#   [ desde : hasta el final]
fragmento1 = text[2:]
#  [ desde el inicio hasta 5 ]
fragmento2 = text[:5]
#  desde el caracter numero 2 hasta el 10 - pero salteandose de a 2
fragmento3 = text[2:10:2]
# de esta forma podemos tomar toda la cadena pero al revez
fragmento4 = text[::-1]

print("\n comenzando desde el indince 2 y terminando en el 5 ──► "+ fragmento)
print("\n comenzando desde el indince 2 hasta el final ──► "+ fragmento1)
print("\n desde el inicio hasta el indice 5 ──► "+ fragmento2)
print("\n desde el indice 2 hasta el 10 salteandose 2 ──► "+ fragmento3)
print("\n lo ordena al revez ──► "+ fragmento4)