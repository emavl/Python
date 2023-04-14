edad = input("ingrese su edad ")

try:
    i = int(edad)+1
    print("el proximo año tendra: ", i)
except ValueError:
    print("Error encontrado")
