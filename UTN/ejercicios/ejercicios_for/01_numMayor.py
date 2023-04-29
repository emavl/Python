import os 
os.system("cls")

# Numero mayor
size = 5
lista_numeros = []

for i in range(size):
    while True:
        try:
            numero = int(input("\nIngrese un numero por favor ───► "))
        except ValueError:
            print("\nEso no es un número ")
        else:
            break 
    lista_numeros.append(numero)
    os.system("cls")      
# fin input

mayor = lista_numeros[0]
for numero in lista_numeros:
    if numero > mayor:
        mayor = numero
# fin numero mayor.

# ────────── P r i n t ──────────
print("  "+"_"*20)   
print( f" {'|Numeros ingresados ':^20}|")
print("  "+"¯"*20)  

for numeros in lista_numeros:
    print(f" |{numeros:^19}|")

# ────────── P r i n t ──────────
print("  "+"¯"*20)         
print(f"\nY el numero mayor es {mayor}")

# de otra manera utilizando el MAX
print(f"Y el numero mayor utilizando el max {max(lista_numeros)}")
