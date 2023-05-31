from os import system

system("cls")


def pedir_caracter(mensaje: str, mensaje_error: str, min: str, max: str) -> str:
    """
    Peticion al usuario de un caracter
    verificando un rango minimo y maximo.


    """
    while True:
        try:
            caracter = input(mensaje)
            if caracter > min and caracter > max:
                raise ValueError
            break
        except ValueError:
            print(mensaje_error)

    return caracter


# ----------------------------------------------------------------
# pedir_caracter("letra","error","a","i")

# import re

# def autocomplete(text, options):
#     pattern = re.compile(f"({'|'.join(map(re.escape, options))})(.*)")
#     match = pattern.match(text)
#     if match:
#         prefix = match.group(1)
#         suffix = match.group(2)
#         completions = [prefix + option + suffix for option in options if option.startswith(suffix)]
#         return completions
#     return []

# # Ejemplo de uso
# input_text = input("Input text")
# input_options = ["apple", "application", "banana", "cat"]
# results = autocomplete(input_text, input_options)
# print(results)

import re

    

def autocomplete_features(input_text, features):
    pattern = re.compile(f".*{''.join(map(re.escape, input_text))}.*", re.IGNORECASE)  
    
    completions = [opcion for opcion in features if re.match(pattern, opcion)]
    return completions

# Ejemplo de uso
feature_list = ["color", "size", "material", "brand", "weight"]
user_input = input("Ingrese una característica: ")
suggested_features = autocomplete_features(user_input, feature_list)
print("Opciones sugeridas:")
print(suggested_features)

lista = ['compatible con windows','Velocidad de hasta 3100Mbps', 'Procesador dual-core de 1.4GHz', 'Tecnología MU-MIMO']
