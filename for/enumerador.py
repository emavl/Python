lista = ["a","b","c"]
indice = 0

for item in lista:
    print(indice,item)
    indice +=1
print("─"*20)
# pero con el enumerador facilitamos de esta forma

for indice,item in enumerate(lista):
    print(indice,item)

print("─"*20)

for indice,item in enumerate(range(1,10)):
    print(indice,item)

