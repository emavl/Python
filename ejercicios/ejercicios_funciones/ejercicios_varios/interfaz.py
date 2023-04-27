# funcion que me permite el ingreaso de un dato, solisitado al usuario.

class Interfaz:
    def getNumber(self, mensaje):
        numero = input(mensaje)
        try:
            valorNum = int(numero)
        except ValueError:
            print("Error - valor invalido")

        return valorNum



