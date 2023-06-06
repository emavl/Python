import re

def autocomplete_features(input_text, features):
    pattern = re.compile(f".*{''.join(map(re.escape, input_text))}.*", re.IGNORECASE)
    completions = [feature for feature in features if re.findall(pattern, feature)]
    return completions

# Lista de características
feature_list = ["color", "size", "material", "brand", "weight", "compatible con windows"]

# Solicitar entrada del usuario
user_input = input("Ingrese una característica: ")
suggested_features = autocomplete_features(user_input, feature_list)

# Imprimir opciones sugeridas
print("Opciones sugeridas:")
for feature in suggested_features:
    print(feature)


import re

# Definir una lista de características y opciones
characteristics = {
    "color": ["rojo", "azul", "verde", "amarillo"],
    "forma": ["círculo", "cuadrado", "triángulo"],
    "tamaño": ["pequeño", "mediano", "grande"]
}

# Solicitar al usuario que ingrese una característica
user_input = input("Enter a characteristic: ")

# Use regular expressions para Encuentre todas las opciones para la característica ingresada
for characteristic in characteristics.keys():
    if re.search(characteristic, user_input, re.IGNORECASE):
        options = characteristics[characteristic]
        pattern = "|".join(options)
        matches = re.findall(pattern, user_input, re.IGNORECASE)
        if matches:
            print(f"Posibles opciones para {characteristic}: {matches}")