
"""
  La clase es un molde que sirve para crear un objeto. Podemos pensar en la clase como
 un boceto(prototipo) de una casa (los simientos).
 Contiene todos los detalles - siendo el ejemplo la casa sería (ventana, puertas, pisos, etc...) 
 éstas estan conformadas por atributos y por metodos.

  Un objeto tambien llamado (instancia) es creado a partir de una clase(molde,boceto)
 El proceso de creacion de este objeto se denomina instanciación.

 El constructor __init__ Es aquel método que sirve para inicializar algunos atributos(caract.)
 de un objeto, se ejecuta justo despúes de cear un objeto a partir de una clase.

  Parametro __self__ : Primer parametro de __init__ "self" sirve para trabajar con un objeto fututo
 dentro de una clase (Que será creada posteriormente en el codigo ). Permitiendo agregar y leer 
 atributos y metodos desde la definición misma de la clase.

Con esto tenemos un constructor que se ejecutara cuando creemos una instancia.

"""
class Carta:
	def __init__(self,numero,palo):
		self.palo = palo
		self.numero = numero


	def imprimir(self):
		print(self.numero, "de", self.palo)





