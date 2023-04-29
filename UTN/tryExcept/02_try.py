        
while True:
    try:    
        edad = int(input("\n Ingrese su edad por favor ­───► "))
        if(edad >17 and edad <66):
            break
        else:
            print("\nEdad invalida")
    except ValueError:
        print("\nEso no es un numero")
        

        