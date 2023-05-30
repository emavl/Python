# una CLASE es un molde el cual vamos a usar par almacenar disitintos datos que pertenecen a la misma entidad
# la varible que creamos a partir de nuetra clase va a ser nuestro OBJECTO

# digamos que queremos crear un objecto que va a ser una Persona, claramente todas las personas sondiferentes, pero tienen propiedades en comun: tienen 2 ojos, una boca, una nariz etc

class Persona:
    # cuando hablamos de self nos referimos a la instancia de una variable que pertenece a la clase donde estamos parados

    def __init__(self, id, nombre, apellido, edad) -> None:

        # usamos self.id para crear una propiedad id que solamente va a pertenecer a esta clase, y le asignamos el id que nos llega por parametro

        self.id = id
        self.__nombre = nombre
        self.apellido = apellido
        self.__edad = edad

    # podemos crear metodos para que nuestro objeto haga determinada accion
    # importante usar self para apuntar a la variable del objecto donde estamos parados

    def presentarse(self):
        print(f"Hola, mi nombre es {self.__nombre}")

    def set_edad(self, value):
        if value > 0 and value < 100:
            self.__edad = value

    def get_edad(self):
        return self.__edad

    # usamos @property para establecer un getter, d esta forma podemos acceder a la varaible como si fuera un atributo en vez de como un metodo

    @property
    def nombre(self):
        return self.__nombre


# Ahora podemos crear todos los objetos que queramos reutilizando el mismo molde
persona1 = Persona(1, "Juan", "Mosquella", 27)
persona2 = Persona(2, "Pablo", "Luchetti", 22)

print(persona1.nombre)
print(persona2.nombre)
print(persona1.presentarse())

# la idea es que nuestra clase sea robusta y no se pueda cambiar las variables de nuestro objecto desde fuera, a menos que sea con una funcion setter o getter que valide lo que le estamos mandando. Para esto creamos los respectivos metodos y los validamos desde dentro de la clase, luego a la variable en cuestion le ponemos doble guion bajo para que sea privada. por ej: __edad

# este codigo no va a cambiar la edad porque justamente lo protegi, solo puede cambiarse usando get_edad()

persona1.__edad = 21

print(persona1.get_edad())
print(persona1.nombre) 