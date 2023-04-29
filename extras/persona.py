
# con la palabra reservada self podremos crear los atributos(caract.)
# los cual nos permitira utilizarlos en cualquier lugar de nuestro metodo.
# los metodos son acciones.
class persona:

	def __init__(self):  # importante inicializar para evitar errores.
		self.nombre = ""
		self.edad = 0

	def datos(self,nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def saludar(self):
		print("hola me llamo", self.nombre,"y tengo",self.edad)


persona1 = persona() 
persona2 = persona() 
persona3 = persona() 

persona1.datos("lautaro",15)
persona2.datos("hernan",33)
persona3.datos("german",21)

persona1.saludar()
persona2.saludar()
persona3.saludar()