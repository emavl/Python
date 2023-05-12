
personas = []

for indice in range(3):
    while True:
        nombres = input("\n Por favor ingrese su nombre ───► ")
        if nombres.isalpha():
            personas.append(nombres)
            break
        print("\nError . . ingreso un dato invalido")
# fin for


#     print(personas)        

# for i in personas:
#     print(i)
    
# imprimiendo en la misma linea.
nombres_en_linea = ", ".join(indice for indice in personas)
print(nombres_en_linea)
    
# ───► ───► ───► ───► ───► Apunte 
# para agregar datos a una lista 
    
# mi_lista = []

# nombre = input("ingrese nombre")

# mi_lista.append(nombre)

# print(mi_lista)