"""
Para comprender mejor el tema de los objetos, implemente un objeto llamado Automovil con las siguientes características o atributos:
( velocidad_actual:representado por un número - marca - estado: puede ser encendido o apagado, representado por un valor booleano. )



"""


# Defina aquí su clase Automovil
class Automovil:

    def __init__(self):
        self.estado = None
        self.velocidad_actual = 0
        self.marca = ""
        self.modelo = ""

    def datos(self, velocidad_actual, marca, modelo, estado):
        self.velocidad_actual = velocidad_actual
        self.marca = marca
        self.modelo = modelo
        self.estado = (estado == "encendido")

    def inprimir(self):
        print("Su auto es", self.marca, "la velocidad final es de", self.velocidad_actual, "el auto esta encendido",
              self.estado)


automovil = Automovil()
automovil.datos(250, "toyota", "corola", "encendido")
automovil.inprimir()

# Recuerde programar el constructor de clase que inicializa los 3 atributos

# Adicionalmente agregue los 4 métodos que se encargan de modificar la velocidad y el estado

# No es necesario que cree instancias o pruebas ya que el código se evalúa automáticamenteo
