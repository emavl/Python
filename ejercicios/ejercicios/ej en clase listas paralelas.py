import os 
os.system("cls")

notas_p1 = []
notas_p2 = []
alumnos = []
promedio = []
size = 2



print("  Ingreso Notas alumnos  UTN ")
print("¯"*30)

for i in range(size):
    # ───────────────────────────► N o m b r e
    while True:
        nombre = input("Por favor ingrese su nombre ───► ")
        if nombre.isalpha():
            alumnos.append(nombre)
            break
        print("\nError, ingrese un nombre valido")
        
    # ───────────────────────────► N o t a _1
    while True:
        try:
            primer_parcial = int(input("\nIngrese la primer nota  ───► "))
            if primer_parcial < 1 or primer_parcial > 10:
                raise ValueError # me devuelve el print de ValueError.
            break
        except ValueError:
            print("\nError, ingrese una nota valida ───► ")
    # ───────────────────────────► N o t a _2
    while True:
        try:
            segundo_parcial = int(input("\nIngrese la segunda nota ───► "))
            if segundo_parcial < 1 or segundo_parcial > 10:
                raise ValueError # me devuelve el print de ValueError.
            break
        except ValueError:
            print("\nError, ingrese una nota valida ───► ")
    os.system("cls")
    # asigno las notas y promedios
    notas_p1.append(primer_parcial)
    notas_p2.append(segundo_parcial)
    promedios = (primer_parcial + segundo_parcial)/2
    promedio.append(promedios)

# fin del ingreso de datos    

# for i in range(size):
    
#     print("alumnos")
#     print(alumnos)
#     print("notas")
#     print(notas_p1)
#     print(notas_p2)
#     print("promedio")
#     print(promedio)



print(" "+"_"*42)   
print( f" {'|     Alumno':^13}|{'nota P1':^8}|{'nota P2':^5}|{'Promedio ':^10}|")
print(" "+"¯"*42)
for it in range(size):
    print(f" |   {alumnos[it]:>8} |{str(notas_p1[it]):^7}| {str(notas_p2[i]):^7}|{str(promedio[it]):^10}|" )
print(" "+"¯"*42) 
    
input("Precione tecla Enter para finalizar programa, muchas gracias ‼") 
 
