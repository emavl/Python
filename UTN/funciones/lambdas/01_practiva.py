### Lambdas ###

suma_dos_valores = lambda num1, num2: num1 + num2

print(suma_dos_valores(100, 100))

multiplicador = lambda num1, num2:  num1 * num2

print(multiplicador(400,2))

def suma_3_valores(valores):
    return lambda num1, num2: valores + num1 * num2

print(suma_3_valores(100)(33,3))


