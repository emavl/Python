from mi_biblioteca import *

# Debemos desarrollar un algoritmo que permita computar los votos del Senado de Berlinberlín.
# Se deberá ingresar el nombre de cada senador y si está Presente o no en la sesión.
# Si el senador está presente, se deberá pedir el valor del voto
# El voto de los senadores berliberlineses puede ser Afirmativo, Negativo o Abstención (validar).
# El valor por defecto para los senadores ausentes será Abstención.

# Se deberá Informar:
# o Cantidad total de senadores.
# o Cantidad de senadores presentes.
# o Cantidad y porcentaje de votos afirmativos.
# o Cantidad y porcentaje de votos negativos.
# o Cantidad y porcentaje de abstenciones.
# o Generar una lista de senadores por cada tipo de voto y mostrarlas por pantalla.


nombres_senadores = []
votos = []
resp = "si"
acc_afir = 0
acc_neg = 0
acc_abst = 0
senador_presente = 0


os.system("cls")

while resp.lower() == "si":

    senador = pedir_texto(
        "Ingrese el nombre del senador por favor ", "Error de tipeo ")
    nombres_senadores.append(senador)
    asistencia = pedir_texto(
        "\n¿Se encuentra presente/ausente en la sesión? - ", "Error de tipeo ")

    if asistencia.lower() == "presente":
        senador_presente += 1
        voto = pedir_texto("\nIngrese el voto siendo ( afirmativo - negativo o abstención )"
                           "\nresuesta ------> ", "Error de tipeo ")
        while (voto != "afirmativo") and (voto != "negativo") and (voto != "abstención"):
            voto = pedir_texto("\nError !!! - Reingrese el voto siendo ( afirmativo - negativo o abstención )"
                               "resuesta ------> ", "Error de tipeo ")

        if voto == "afirmativo":
            acc_afir += 1
            votos.append(voto)

        elif voto == "negativo":
            acc_neg += 1
            votos.append(voto)

        else:
            acc_abst += 1
            votos.append(voto)

    else:
        acc_abst += 1
        votos.append("abstencion")

    resp = pedir_texto("\ndesea continuar ? si/no \n", "Error de tipeo ")
    os.system("cls")

os.system("cls")

# --------- Calculos
porcentaje_af = ((acc_abst + acc_afir + acc_neg) * acc_afir) / 100
porcentaje_neg = ((acc_abst + acc_afir + acc_neg) * acc_neg) / 100
porcentaje_abst = ((acc_abst + acc_afir + acc_neg) * acc_abst) / 100

print(" "+"_"*39)
print(f" |{' Senadores  ':^21}| {'Votos':^14} |")
print(" "+"¯"*39)
for i in range(len(nombres_senadores)):
    print(
        f" |  {nombres_senadores[i].capitalize():>18} |  {votos[i].capitalize():>12}  | ")
print(" "+"¯"*39)


print(f"\n\n La cantida de senadores es {len(nombres_senadores)}")
print(f"Cantidad de senadores presentes {senador_presente}.")
print(
    f"\nCantidad de votos afirmativos es {acc_afir } y porcentaje es {porcentaje_af}%.")
print(
    f"\nCantidad de votos negativos es {acc_neg } y porcentaje es {porcentaje_neg}%.")
print(
    f"\nCantidad de votos abstenciones es {acc_abst} y porcentaje es {porcentaje_abst}%.")
