monedas = 5


while monedas > 0:
    print(f"tengo {monedas} monedas")
    monedas -= 1
else: print("No hay mas monedas")

respuesta = input("\n Desea continuar ")

while respuesta == 'si':
    print("Entonces comencemos ! ")
    break
else:
    print("Hasta luego...")

nombre = input("\nIngrese su nombre por favor ")

for letra in nombre:
    if letra == 'r':
        break

    print(letra)


