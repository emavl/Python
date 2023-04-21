# Debemos hacer un programa para que el usuario recuerde las reglas de estilo de
# python, entonces debemos pedirle al usuario un número entre el 1 y el 8,
# al ingresar el número debemos mostrarle que regla de estilo representa y su
# descripción (Sacar la información de las diapositivas de las reglas de estilo).
# En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario “Error,
# regla de estilo inexistente”

import os 
os.system("cls")

# ----------------------- F u n c i o n e s -----------------------
def limpiar_consola():
  print("\n")
  os.system("pause")
  os.system("cls")
  
def pedir_numero_min_max(mensaje,mensaje_error,min,max):

    while True:
      try:    
          num = int(input(mensaje))
          if(num < min and num < max):
              raise ValueError
          break
      except ValueError:
          print(mensaje_error)
  
    return num  
         
def ejecutar_menu():
  opcion = pedir_numero_min_max("=================================\n"
                        "         Reglas de estilo        \n"
                        "=================================\n"
                        "1) ¿Cuál es el sentido?\n"
                        "2) ¿Qué es PEP?\n"
                        "3) ¿Qué es PEP8\n"
                        "4) Identado\n"
                        "5) Tamaño máximo\n"
                        "6) Líneas en blanco\n"
                        "7) Comentarios\n"
                        "8) Nombres\n"
                        "9) Salir\n"
                        "\n opcion n° ────► ",
                        "\nError, regla de estilo inexistente\n", 0, 9)
  return opcion

def reglas_de_estilo():

  while True:
    match (ejecutar_menu()):
        case 1: # ───► ¿ Cuál es el sentido ?
          os.system("cls")
          print("  Según Guido van Rossum, el código es leído más veces que escrito,\n"
                "por lo que resulta importante escribir código que no sólo funcione,\n"
                "sino que además pueda ser leído con facilidad.\n")           
          limpiar_consola()
        case 2: # ───► ¿ Que es PEP ?
          os.system("cls")
          print(" Python Enhancement Proposal es un documento\n"
                "que proporciona información a la comunidad de\n"
                "Python, o que describe una nueva característica\n")
          limpiar_consola()
        case 3: # ───► ¿ Que es PEP8 ?
          os.system("cls")
          print("Es un conjunto de recomendaciones cuyo objetivo\n"
                "es ayudar a escribir código más legible y abarca\n"
                "desde cómo nombrar variables, al número máximo\n"
                "de caracteres que una línea debe tener\n")
          limpiar_consola()
        case 4: # ───► Identado
          os.system("cls")
          print("Python no usa {} para designar bloques de código\n"
               " como otros lenguajes de programación, sino que\n"
                "usa bloques identados para indicar que un\n"
                "determinado bloque de código pertenece a por\n"
                "ejemplo un if.\n")
          print(" if ( condicion_a and\n"
                "           condicion_b:\n"
                "        print('hola mundo')\n\n")
          print(" def mi_funcion(primer_parametro,segundo_parametro,\n"
                "                tercer_parametro, cuarto_parametro,\n"
                "                quinto_parametro):\n   "
                "        print('hola mundo')")
          limpiar_consola()
        case 5: # ───► Tamaño máximo
          os.system("cls")
          print("Se recomienda limitar el tamaño de cada línea a\n"
                "79 caracteres, para evitar tener que hacer scroll a\n"
                "la derecha\n")
          print("resultado = ( variable_a\n"
                "          + variable_b\n"
                "          + (variable_c - variable_d)\n"
                "          - variable_e\n"
                "          - variable_f")
          limpiar_consola()
        case 6: # ───► Lineas en blanco
          os.system("cls")
          print("El uso de espacios en blanco mejora la legibilidad\n"
                "del código, y es por lo que la PEP8 indica dónde\n"
                "debemos usar espacios y dónde no.\n")
          print("# Lo correcto es:  x = 5      var_a = 0\n"
                "                if x == 5:    variable_b = 10\n"
                "                     pass     otra_variable_C = 3\n")
          print("\n# Lo incorrecto es:  x=5      var_a           = 0\n"
                "                  if x==5:    variable_b      = 10\n"
                "                     pass     otra_variable_C = 3\n")
          limpiar_consola()
        case 7: # ───► Comentarios
          os.system("cls")
          print("Cualquier comentario que contradiga el código es\n"
                 "peor que ningún comentario.\n"
                 "Si actualizamos el código, se debe actualizar los\n"
                 "comentarios para evitar crear inconsistencias\n"
                 "\nEvitar comentarios poco descriptivos que no\n"
                    "aporten nada más allá de lo que ya se ve a simple\n"
                    "vista.\n")
          print("\n# Lo incorrecto es:  x = x * 1.21  # Multiplica por 1.21 a la variable x\n"
                
                "\n# Lo correcto es:  x = x * 1.21  # Agrega el 21% de IVA\n")
          limpiar_consola()
        case 8: # ───► Nombres 
          os.system("cls")
          print("\nFunciones: Uso de snake_case, letras en"
                  "minúscula separadas por guión bajo: mi_funcion."
                  "Variables: Al igual que las funciones: variable,"
                  "mi_variable."
                  "Clases: Uso de CamelCase, usando mayúscula y"
                  "sin barra baja: MiClase, ClaseDePrueba"
                  "Métodos: Al igual que las funciones, usar snake"
                  "case: metodo, mi_metodo"
                  "Constantes: Nombrarlas usando mayúsculas y"
                  "separadas por guión bajas: UNA_CONSTANTE"
                  "Módulos: Igual que las funciones: modulo.py,"
                  "mi_modulo.py.")
          limpiar_consola()
          pass 
        case 9: # ───► Salir
          os.system("cls")
          print("Siga estudiando usted puede ‼\n")
          break

# -----------------------------------------------------------------        
        
# Programa:
reglas_de_estilo()        
        
              