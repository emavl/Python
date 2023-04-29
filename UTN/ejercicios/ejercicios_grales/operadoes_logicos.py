nombre = input("\nIngrese su nombre ")
nombre1 = input("\nIngrese el otro nombre ")
edad = int(input("\nIngrese la edad de "+nombre+" "))
edad1 = int(input("\nIngrese la edad de "+nombre1+" "))

if edad > edad1:
    print(nombre+" es mayor")
else:
    print(nombre1+" es mayor")
