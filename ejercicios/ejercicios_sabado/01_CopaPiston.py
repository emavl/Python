
"""
3) Copa pistón!!!
Se deberá generar un programa para registrar las estadísticas de los 10 integrantes de una carrera de autos.
Se pedirá el ingreso de:
nombre
 edad (mayor a 18)
nacionalidad del piloto (argentino, inglés, francés, brasilero, estadounidense)
 cantidad de carreras ganadas (no pueden ser números negativos)
 número del vehículo (no puede ser un número negativo)
se necesita saber:

*Nacionalidad del piloto más joven.
*Cantidad de vehículos con número par.
*Nombre del piloto con menos victorias y el número de auto impar.
*Cantidad de pilotos mayores de 25 años con número de vehículo impar.
*Nombre del piloto más joven con más victorias.
*Nacionalidad del piloto más veterano con menos victorias.
*Promedio de edad de los pilotos que tiene un vehículo con número par.

"""
piloto_joven = " "
divisor = 0
mayores_25 = 0
participantes = 1
vehiculos_Par = 0
vehiculos_Impar = 0
flag = 0
flag_edad = 0
victorias = 0
suma_edad = 0
mas_Joven = 0
veterano = 0
nac_veterano = " "
piloto_perdedor = None

while participantes < 3:
    print(participantes)
 # ───────────────────────────── NOMBRE ─────────────────────────────
    nombre_corredor = input("\nPor favor, introduzca su nombre ───► ")
    
 # ───────────────────────────── NACIONALIDAD ─────────────────────────────  
    nacionalidad = input("\nPor favor, introduzca su Nacionalidad ───► "
                    "\nargentino\ninglés\nbasilero\nfrancés\nestadounidense\n ───► ")

    while nacionalidad != "argentino" and nacionalidad != "inglés" and nacionalidad != "francés" and nacionalidad != "brasilero" and nacionalidad != "estadounidense":
        nacionalidad = input("\nError!! el participante debe ser de nacionalidad" 
              "\n  argentino - ingles - brasilero - frances o estadounidense \n"
              "Respuesta ───► ")
        

 # ───────────────────────────── EDAD ───────────────────────────── 
    edad = int(input("\nPor favor, ingrese su edad ───► "))

    while (edad < 18) or (edad > 50):
        edad = int(input("\nError el participante debe de ser mayor a 18\n y si tenés mas de 50 estas un poco grandesito ───►"))

    if flag_edad == 0:
        mas_Joven = edad
        veterano = edad
        flag_edad = 1       

    # Nacionalidad del piloto más joven.
     
    if edad < mas_Joven:         # Mas joven 
           mas_Joven = edad
           nacJoven = nacionalidad

    if edad > veterano:         # Mas veterano  
            veterano = edad
            
 

 #  ───────────────────────────── NUMERO DEL VEHICULO ─────────────────────────────
    numero_Vehiuculo = int(input("\nIngrese el numero del vehiculo ───► "))

    while numero_Vehiuculo < 0:
        numero_Vehiuculo = int(input("\nError el n° del vehiculo debe de ser mayor a 0 ───► "))

    # VEHICULOS PARES 
    if numero_Vehiuculo % 2 == 0:
        vehiculos_Par += 1
    # *Cantidad de vehículos con número par. OK
    
 # ───────────────────────────── CARRERAS GANADAS ─────────────────────────────
    carreras_Ganadas = int(input("\nPor favor, ingrese las carreras ganadas ───►"))
    
    while carreras_Ganadas < 0:
       carreras_Ganadas = int(input("\nError!!, la cantidad de carreras deben de ser mayores a 0 ───► "))
       victorias = carreras_Ganadas
       
    if flag == 0:
        menos_victorias = carreras_Ganadas
        mas_victorias = victorias
        flag = 1

    # Menos victorias 
    if victorias < menos_victorias :
        menos_victorias = victorias
        
        if numero_Vehiuculo % 2 != 0:
            piloto_perdedor = nombre_corredor
            vehiculo_Impar = numero_Vehiuculo  
    # *Nombre del piloto con menos victorias y el número de auto impar. OK

    if edad > 25 and numero_Vehiuculo % 2 != 0: 
        mayores_25 += 1
    # Cantidad de pilotos mayores de 25 años con número de vehículo impar.
    
    if victorias > mas_victorias and edad < mas_Joven :
        mas_victorias = victorias 
        piloto_joven = nombre_corredor
    # Nombre del piloto más joven con más victorias.

    if veterano > edad and menos_victorias < victorias:
        nac_veterano = nacionalidad
    # Nacionalidad del piloto más veterano con menos victorias.

    if numero_Vehiuculo % 2 != 0:
        divisor += 1
        suma_edad = suma_edad + edad
        prom_edad = suma_edad / divisor
    # Promedio de edad de los pilotos que tiene un vehículo con número par.
    if participantes == 10:
        print("\n Ultimo participarnte")
    else:
        print("\nSiguiente corredor ...\n")
        linea = "─"
        print(linea*50)


    participantes += 1

print("\nLa nacionalidad del piloto mas joven es {}" .format(nacionalidad.title()) )

if vehiculos_Par > 0:
    print("\nCantidad de vehiculos con número par es {}" .format(vehiculos_Par))
else:
    print("\nNo hay vehiculos cuyos números sean pares") 

print("\n{} es el piloto con menos victorias y su vehiculo es el {}". format(piloto_perdedor,vehiculo_Impar))

if mayores_25 > 0 :
    print("\nLa cantidad de pilotos mayores de 25 cuyo auto es impar es: {}". format(mayores_25))
else:
    print("\nNo hay pilotos mayores de 25 cuyos autos contengan números impares") 
        
print("\nEl nombre del piloto mas joven con mas victorias es" + piloto_joven)
print("\nNacionalidad del piloto mas veterano con menos victorias" + nac_veterano)
print("\nEl promedio de edad de los pilotos que tienen vehículo con número par es: {}" .format(prom_edad))


