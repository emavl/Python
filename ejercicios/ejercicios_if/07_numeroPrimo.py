

# Escribir un programa que le pida al usuario que ingrese un número entero
# positivo, y luego imprima "El número es primo" si el número es primo, o "El
# número no es primo" si el número no es primo.

numero = int(input("\nPor favor ingrese un número "))


if numero > 1:
      # para ser numero primo debe de ser mayor a 1 
    for i in range(2, numero):
        if numero % i == 0:
            print("El número no es primo")
            break
    else:
        print("El número es primo")
else:
    print("El número no es primo")
    

            