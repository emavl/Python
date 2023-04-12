



numeroUno = int(input("Ingrese un numero: "))
numeroDos = int(input("Ingrese un numero: "))

dosCifras = numeroUno % 100 # entrega las 2 ultimas cifras 
tresCifras = numeroDos % 1000 # Entrega las 3 ultimas cifras 

print("El numero es", dosCifras, tresCifras)
