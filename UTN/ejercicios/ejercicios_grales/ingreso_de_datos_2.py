listaNumeros = []

numeroUsuario = int(input("\nPor favor, introduzca un número ───► "))
listaNumeros.append(numeroUsuario)
decision = input("\n¿Desea añadir mas numeros?")

while decision == 'si' or decision == 'SI':
    numeroUsuario = int(input("\nPor favor, introduzca otro número ───► "))
    listaNumeros.append(numeroUsuario)
    decision = input("\n¿Desea añadir mas numeros?")

print(f"Los numeros introducidos son {listaNumeros}")
