### Lambdas ###

def suma_dos_valores(num1, num2): return num1 + num2


print(suma_dos_valores(100, 100))


def multiplicador(num1, num2): return num1 * num2


print(multiplicador(400, 2))


def suma_3_valores(valores):
    return lambda num1, num2: valores + num1 * num2


print(suma_3_valores(100)(33, 3))


lista = [
    {
        "Nombre": "Emanuel",
        "Apellido": "vidal",
        "Edad": 35,
        "Lenguajes": {"Python", "Swift", "Kotlin"},
        1: 1.77
    }, 
    {
        "Nombre": "juancho",
        "Apellido": "peyrot",
        "Edad": 36,
        "Lenguajes": {"Python", "Swift", "Kotlin"},
        1: 1.74
    }
]

apellido, nombre = list(map(lambda item : (item['Apellido'], item['Nombre']), lista))

print (apellido, nombre)

suma = lambda a, b: a + b
resultado = suma(3, 5)
print(resultado)  # Salida: 8

es_par = lambda num: num % 2 == 0
print(es_par(4))   # Salida: True
print(es_par(7))   # Salida: False

numeros = [1, 2, 3, 4, 5]
duplicados = list(map(lambda x: x * 2, numeros))
print(duplicados)  # Salida: [2, 4, 6, 8, 10]

 # Ejemplo de filtrado de números pares en una lista:
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4]

# Ejemplo de ordenamiento de una lista de cadenas por su longitud
palabras = ["perro", "gato", "elefante", "ratón"]
ordenadas = sorted(palabras, key=lambda x: len(x))
print(ordenadas)  # Salida: ['gato', 'perro', 'ratón', 'elefante']

personas = [
    {"nombre": "Juan", "edad": 25},
    {"nombre": "María", "edad": 30},
    {"nombre": "Pedro", "edad": 18},
    {"nombre": "Ana", "edad": 40}
]
mayores_de_edad = list(filter(lambda persona: persona["edad"] >= 18, personas))
print(mayores_de_edad)  # Salida: [{'nombre': 'Juan', 'edad': 25}, {'nombre': 'María', 'edad': 30}, {'nombre': 'Ana', 'edad': 40}]

# -------> F i l t e r 

# Filtrar números pares de una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4, 6, 8, 10]

# Filtrar palabras que comienzan con una letra específica en una lista
palabras = ["manzana", "banana", "pera", "mango", "uva"]
letra = "m"
filtradas = list(filter(lambda x: x.startswith(letra), palabras))
print(filtradas)  # Salida: ['manzana', 'mango']

# Filtrar personas mayores de edad en una lista de diccionarios:
personas = [
    {"nombre": "Juan", "edad": 25},
    {"nombre": "María", "edad": 17},
    {"nombre": "Pedro", "edad": 30},
    {"nombre": "Ana", "edad": 20}
]
mayores_de_edad = list(filter(lambda x: x["edad"] >= 18, personas))
print(mayores_de_edad)  # Salida: [{'nombre': 'Juan', 'edad': 25}, {'nombre': 'Pedro', 'edad': 30}, {'nombre': 'Ana', 'edad': 20}]

