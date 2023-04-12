listaNombres = []

nombreUsuario = input("\nPor favor, introduzca su nombre ───► ")
listaNombres.append(nombreUsuario)
decision = input("\n¿Desea añadir otro nombre?")

while decision == 'si' or decision == 'SI':
    nombreUsuario = input("\nPor favor, introduzca otro nombre ───► ")
    listaNombres.append(nombreUsuario)
    decision = input("\n¿Desea añadir mas nombres?")

print(f"Los nombres introducidos son {listaNombres}")
