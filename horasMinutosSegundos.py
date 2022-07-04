"""
 Ingresar cantidad de segundo y muestre cuantas horas min, seg.

"""
segundos=int(input("Ingrese la cantidad de segundos por favor: "))

horas = segundos//3600 # Division entera es con dos slash !!! Atencion a eso 

resto = segundos% 3600

minutos = resto//60

resto1 = resto% 60

print("Son", horas, "horas", minutos, "Minutos y",segundos,"segundos")

    