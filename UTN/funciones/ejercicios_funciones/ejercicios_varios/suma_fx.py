# funciones

def sumar(valor1, valor2):
	resultado = valor1 + valor2
	return resultado


def numUsuario():
	variable1 = input("ingrese un valor ")
	try:
		varNumerica = int(variable1)
	except ValueError: # o bien podemos colocar " as error, para que le diga al usuario cual fue el error especifico
		print("El dato ingresado es erroneo")
		varNumerica = 0

	return varNumerica


var1 = numUsuario()
var2 = numUsuario()

resultadoSum = sumar(var1, var2)
print("El resultado de la suma es:", resultadoSum)
