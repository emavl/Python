from os import system

system("cls")

lista = ["a","b","c"]
indice = 0

for item in lista:
    print(indice,item)
    indice +=1
# Imprime su indice y el valor de cada item
# 0 a
# 1 b
# 2 c

print("─"*20)
# pero con el enumerador facilitamos de esta forma

for indice,item in enumerate(lista):
    print(indice,item)
# Imprime su indice y el valor de cada item utilizando la funcion enumerate()    
# 0 a
# 1 b
# 2 c


print("─"*20)

for indice,item in enumerate(range(1,10)):
    print(indice,item)

