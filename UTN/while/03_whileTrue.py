while True:
     valor = input("por favor, ingrese su nombre")
     if valor.isalpha():
        break
     print("Error, con el valor ingresado")
    
while True:
    edad = input("\n Ingrese su edad por favor ­───► ")
    if edad.isdigit():
        edad = int(edad)
        break
    print("\nError, ingrese un numero por favor")
     
        