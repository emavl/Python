from os import system
from functools import reduce
system("cls")
### Funciones de orden superior ###

def los_suma(value1: int, value2: int) -> int: 
    return value1 + value2

def los_multiplica(value1, value2):
    return value1 * value2

def calcular(valor1: int, valor2: int, fx_los_suma: int) -> int:
    return fx_los_suma(valor1, valor2)

print ()
print(calcular(5, 5, los_suma)) # output (10)
print(calcular(5, 5, los_multiplica)) # output (25)

### Cierres ------> Closures ###
print("\n### Cierres o Closueres con retorno a funcion\n")
# funcion que retorna una funcion 


def funcion_1():       
    def add(value):
        return value + 10
    return add

retorno_fx = funcion_1()

print(retorno_fx(20)) # output (30

def funcion_2(valor_original):
    def add(value):
        return value + valor_original
    return add

retorno_fx = funcion_2(10)
print(retorno_fx(2)) # output 12 (la suma de fx2 y retorno_fx )

funcion_2(10)(2)
print(funcion_2(10)(2)) # output (12)

### funciones incorporadas por python (de orden superior) ### 

# M a p

numeros = [10, 20, 30, 40, 50, 60]

def multiplica_dos(numero):
    return numero * 2

print(map(multiplica_dos, numeros))  # <map object at 0x0000027809DB3DC0>
# Map itero sobre cada valor de la lista que le pasamos y, a ejecutado sobre cada valor
# la funcion multiplicar que le pase como parametro.
print(list(map(multiplica_dos, numeros)))  # output [20, 40, 60, 80, 100, 120]
print(list(map(lambda num: num * 2, numeros)))  # output [20, 40, 60, 80, 100, 120]
#    tambien podemos pasarle un lambda 


# F i l t e r

numeros = [ 2, 5, 11, 16, 20, 42]

def filtro_mayot_diez(numero):
    if numero > 10:
        return True
    return False

print(list(filter(filtro_mayot_diez, numeros))) # output [11, 16, 20, 42]
print(list(filter(lambda num: num < 20, numeros))) # output [2, 5, 11, 16]

# R e d u c e

def sumar(num_1, num_2):
    return num_1 + num_2

print(reduce(sumar, numeros)) # output 96

def sumar(num_1, num_2):
    print(num_1)
    print(num_2)
    return num_1 + num_2

print(reduce(sumar, numeros)) # output



