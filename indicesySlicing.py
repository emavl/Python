 
# Slicing

cadena = input("Ingrese un nombre: ")
subCadena = cadena[:] # Con el ejemplo emanuel - Mantiene el mismo string ---> Emanuel.
print(subCadena)

cadena1 = input("Ingrese un nombre: ")
subCadena1 = cadena1[2:] # ej: Emanuel --> anuel
print(subCadena1)

cadena2 = input("Ingrese un nombre: ")
subCadena2 = cadena2[:3] # ej: Emanuel --> Ema.
print(subCadena2)

cadena3 = input("Ingrese un nombre: ")
subCadena3 = cadena3[-6:-1]  # ej: Emanuel --> manue.
print(subCadena3)

cadena4 = input("Ingrese un nombre: ")
subCadena4 = cadena4[-4:]  # ej: Emanuel --> manue.
print(subCadena4)
