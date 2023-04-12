lista = ['a','b','c']

for letra in lista:
    print("letra "+letra)

for letra in lista:
    num_letra = lista.index(letra)
    print("letra "+letra)

# otra forma de realizar un for utilizando " startswith
# comienza " con "
lista1 = ['pablo', 'laura', 'fede', 'luis', 'julia']

print("\nUtilizando \"startswith \" seleccionando la letra l como condicion ")
print("\nlos nombres que comienzan con l son: ")
for nombre in lista1:
    if nombre.startswith('l'):
        print(nombre)

print("─"*30)
numeros = [1,2,3,4,5]
miValor = 0

for numero in numeros:
    miValor = miValor + numero
    # si lo tabulo cambia y quedaría dentro del for
    print(miValor)

# de esta forma imprimo fuera del for
print(miValor)

print("─"*30)

# puedo o no declarar la variable  y funcionaría igual
# ej: palabra = python

for letra in "python":
    print(letra)

print("─"*30)
# al igual que si quiesiera utilizar una lista dentro del for

for listas in [1,2,3]:
    print(listas)

print("─"*30)
# o bien varias listas u objetos

for objeto in [[1,2],[3,4],[5,6]]:
    print(objeto)

print("─"*30)

# creando 2 variables como ( a y b )
# podemos imprimir las variables por separado
# donde (a) se caga con la informacion 1 : (1,3,5)
# y (b) se carga con la informacion 2 : ( 2,4,6)
# así iteramos una lista dentro de otra
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

print("─"*45)
print("de esta forma imprimimos las claves solamente")
dic = {'clave1': 'a', 'clave2':'b', 'clave3': 'c'}

for item in dic:
    print(item)

print("\nPara imprimir de forma completa")

for item in dic.items():
    print(item)

print("\nPara imprimir los valores de la lista")

for item in dic.values():
    print(item)

print("\nOtra manera distinta de "
      "imprimir los valores de la lista")

for a,b in dic.items():
    print(a,b)

print("─"*45)

my_tupla = (35, "emanuel", "vidal", 1.76)

miSet1 = set((1,2,3,(4,5,6),7,8,9))

cliente = {'nombre': (input("\ningrese un nombre ")),
           'apellido': (input("ingrese un apellido ")),
           'peso': int(input("ingrese su peso ")),
           'altura': float(input("ingrese su altura: ")),
           "lengujes":{"python","swift","kotlin"}}

print("─"*45)
print("\nimprimo la tupla")

for element in my_tupla:
    print(element)

print("─"*45)
print("\nimprimo el set")

for element in miSet1:
    print(element)

print("─"*45)
print("\nimprimo el cliente\n")

for element in list(cliente.items()):
    print(element)

for element in list(cliente.values()):
    print(element)    

for element in cliente:
    print(element)    
    if element == "altura":
        break
else:
    print("el bucle for para dicc. a finalizado")