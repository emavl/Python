# Crear la lista de listas con los insumos y sus características
insumos = [
    ["Insumo1", "Caracteristica1", "Caracteristica2", "Caracteristica3"],
    ["Insumo2", "Caracteristica2", "Caracteristica3", "Caracteristica4"],
    ["Insumo3", "Caracteristica1", "Caracteristica4", "Caracteristica5"],
    # Agrega más listas de insumos con sus características según sea necesario
]

# Obtener la característica a buscar mediante input
caracteristica_buscada = input("Ingrese la característica que desea buscar: ")

# Buscar la característica en los insumos y mostrar los insumos que la contienen
insumos_encontrados = []
for insumo in insumos:
    if caracteristica_buscada in insumo:
        insumos_encontrados.append(insumo[0])

# Mostrar los resultados por consola
if insumos_encontrados:
    print("Los siguientes insumos contienen la característica", caracteristica_buscada + ":")
    for insumo_encontrado in insumos_encontrados:
        print("- " + insumo_encontrado)
else:
    print("No se encontraron insumos con la característica", caracteristica_buscada)
