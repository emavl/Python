lista = [1,2,3,4]

for numeros in lista:
    print(numeros)

# pero para hacerlo de forma mas eficiente utilizaremos los rangos
# no aceptando floats
print("─"*30)
for numeros in range(5):
    print(numeros)

print("─"*30)
print("u otra forma ")

for numeros in range(25,50):
    print(numeros)

print("u otra forma salteandose pasos ")

for numeros in range(25,50,2):
    print(numeros)

# para crear una lista con cierto rango

lista = list(range(1,20))

print(lista)