
respuesta = input("\nSabe hablar ingles ")
respuesta1 = input("\nSabe programar en python ")
# ---------------------------------

if respuesta == 'si':
    habla_ingles = True
else:
    habla_ingles = False

# ----------------------------------
if respuesta1 == 'si':
    sabe_python = True
else:
    sabe_python = False
# ----------------------------------

if habla_ingles and sabe_python:
    print("\nCumples con los requisitos para postularte")

elif (habla_ingles == False) and (sabe_python == False):
    print("\nPara postularte, necesitas saber programar en Python y tener conocimientos de inglés")

elif habla_ingles== False and sabe_python:
    print("\nPara postularte, necesitas tener conocimientos de inglés")

else:
    print("\nPara postularte, necesitas saber programar en Python")