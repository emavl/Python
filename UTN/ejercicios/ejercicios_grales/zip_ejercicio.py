nombre = ['Ana', 'hugo', 'lautaro']
apellido = ['perez', 'monaco', 'saucos']
ciudades = ['Mexico', 'londres', 'peru']

combinados = list(zip(nombre, apellido, ciudades))

for nombre, apellido, ciudades in combinados:
    print(f"nombre {nombre} y apellido {apellido} nacido en {ciudades}")

