import os
os.system("cls")

def pedir_numero(mensaje,mensaje_error):

    while True:
        num = input(mensaje)
        if num.isdigit():
            num = int(num)
            break
        print(mensaje_error)
    
    return num   
# Dado un número entero n, imprimir la suma de los números pares menores o
# iguales a n.


n = pedir_numero("Por favor ingrese un numero ────► ","Error ‼ - debe ingresar numeros")
suma = 0

for numeros in range(n+1):
    if numeros % 2 == 0:
        suma += numeros

print(f"\nNumero ingresado es: {n}")        
print(f"la suma de los numeros pares menores o iguales al numero ingresado es : {suma} ")        