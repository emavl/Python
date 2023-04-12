from multiprocessing import Condition

num = int(input("\nIngrese un numero por favor: "))

cond = num > 10 and num < 100
22
print("\n¿El numero esta entre 10 y 100?", cond)

# Utilizando condicional