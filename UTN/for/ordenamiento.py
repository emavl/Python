from os import system
system('cls')

lista = [5, 2, 6, 7, 3, 4, -4, -12, 21]
lista_personas = [{"nombre": "Juan", "edad": 13},
                  {"nombre": "claudia", "edad": 23},
                  {"nombre": "santiago", "edad": 41},
                  {"nombre": "bernardo", "edad": 65},
                  {"nombre": "ana", "edad": 65}]


for i in range(len(lista)-1):
    for j in range(i+1, len(lista)):
        if lista[i] < lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux


# for i in lista:
#     print(i)

print()
print()
print()

for i in range(len(lista_personas)-1):
    for j in range(i+1, len(lista_personas)):
        if lista_personas[i]["edad"] > lista_personas[j]["edad"]:
            auxiliar = lista_personas[i]
            lista_personas[i] = lista_personas[j]
            lista_personas[j] = auxiliar
        elif lista_personas[i]["edad"] == lista_personas[j]["edad"]:
            if lista_personas[i]["nombre"] > lista_personas[j]["nombre"]:
                auxiliar = lista_personas[i]
                lista_personas[i] = lista_personas[j]
                lista_personas[j] = auxiliar


# for item in lista_personas:
#     print(item)


for i in range(len(lista_personas)-1):
    for j in range(i+1, len(lista_personas)):
        if lista_personas[i]["edad"] < lista_personas[j]["edad"] or (lista_personas[i]["edad"] == lista_personas[j]["edad"] and lista_personas[i]["nombre"] > lista_personas[j]["nombre"]):
            # o achico aun mas 
            lista_personas[i],lista_personas[j] = lista_personas[j],lista_personas[i]
            # el elemento en la posición j se asigna a la posición i en la lista,
            # y el elemento en la posición i se asigna a la posición j.
            
            #------------------------------------------------
            # auxiliar = lista_personas[i]
            # lista_personas[i] = lista_personas[j]
            # lista_personas[j] = auxiliar


for item in lista_personas:
    print(item)