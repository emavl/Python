# Uso basico de la funcion print.

print("\nUtilizamos todo tipo de datos" ,end=" ")
print("unimos siguiente linea con el \"end =\" ")
print()
print("python" ,"es" ,"temendo" ,sep=' ')

nombre = "juan"
apellido = "perez"
print()
print("Utilizando el format")
print("nombre {} y appellido es {} ".format(nombre.title(), apellido.title()))
print(f"nombre {nombre.title()} y apellido es {apellido.title()} ")
import datetime

ahora = datetime.datetime.now()
print()
print(ahora)
print()
print("O bien podemos imprimir por pantalla de esta otra forma")
print(ahora.strftime('fecha %d/%m/%y y la hora %H:%M:%S'))

