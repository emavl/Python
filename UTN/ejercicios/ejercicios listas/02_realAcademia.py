from mi_biblioteca import *
import os

# La real academia española nos pide desarrollar un pequeño programa
# que contenta el diccionario de la lengua española y su traducción al inglés.
# Para esto necesitamos un algoritmo que nos permita el ingreso de una palabra en español
# y su traducción al ingles y guardarlo en una lista. 
# Si la palabra no existe, debemos agregarla, y si la palabra existe debemos informar que la palabra ya existe 
# y su índice dentro del listado, esta carga debe ser hasta que el usuario se canse de ingresar palabras. 
# Al finalizar se debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en inglés. Recordar validar los datos de forma correcta.

palabra_español = []
traduccion = []
resp = "si"
repeticiones = 0

os.system("cls")
while resp.lower() == "si":
   
    
    palabra = pedir_texto("Ingrese la palabra en español ───► ",
                          "Error - valor equivocado")
    
    for elemento in palabra_español:
        if elemento == palabra:
            repeticiones += 1
    
   # OK
    if repeticiones > 0 :
        print("La palabra esta repetida")
    else:
        palabra_español.append(palabra)
        palabra_traducida = pedir_texto("\nIngrese la traduccion de la palabra ───► ",
                                        "Error - valor equivocado")
        traduccion.append(palabra_traducida)
        
    # OK 
    # if palabra_español.count(palabra) >= 1:
    #     print("palabra repetida")
    # else:
    #     palabra_español.append(palabra)
    #     palabra_traducida = pedir_texto("\nIngrese la traduccion de la palabra ───► ",
    #                                     "Error - valor equivocado")
    #     traduccion.append(palabra_traducida)

        
        
    # if palabra in palabra_español:
    #     print(f"\n palabra existente en posicion {palabra_español.index(palabra)}")
    # else:  
    #     palabra_español.append(palabra)
    #     palabra_traducida = pedir_texto("\nIngrese la traduccion de la palabra ───► ",
    #                                     "Error - valor equivocado")
    #     traduccion.append(palabra_traducida)


    resp = input("\nDesea continuar ───► si/ no ")
    os.system("cls") 
 

print(" "+"_"*24)   
print( f" {'| Español  ':^12}|{'Traduccion':^8}|")
print(" "+"¯"*24)
for i in range(len(palabra_español)):
    print(f" |  {palabra_español[i]:>8} |{(traduccion[i]):>8}  | " )
print(" "+"¯"*24)

