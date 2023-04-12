""" 
 Creamos 2 objetos que se interconectan
importando del archivo "carta" una clase llamada carta

definimos una clase llamada mazo, cramos el constructor de clase init que recibirá por parametro
la palabra reservada self. dentro colocamos 2 atributos(caract) que seran instancias(obj) 
de clase carta siendo un obj del tipo carta.

"""

from Carta import Carta

class Mazo():

	def __init__(self):
		self.carta1 = Carta(7,"diamantes")
		self.carta2 = Carta(4,"espadas")
	
	def imprimir(self):
		self.carta1.imprimir()
		self.carta2.imprimir()


mazo1 = Mazo()
mazo1.imprimir()