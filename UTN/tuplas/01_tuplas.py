## Tuples

# Una tupla es una colección de diferentes tipos de datos que se ordenan
#  inmutables .Las tuplas están escritas con soportes redondos,
# .Una vez que se crea una tupla, no podemos cambiar sus valores.No podemos usar agregar, insertar, eliminar métodos en una tupla porque no es modificable (mutable).A diferencia de la lista, Tuple tiene pocos métodos.Métodos relacionados con tuplas:

# - tuple (): para crear una tupla vacía
# - count (): para contar el número de un elemento especificado en una tupla
# - index (): para encontrar el índice de un elemento especificado en una tupla
# - + Operador: unir dos o más tuplas y crear una nueva tupla

# creando una tupla vacía 
tupla_vacia = ()
tupla_vacia = tuple()

# con valores iniciales
tupla_1 = ('item1', 'item2','item3')

frutas = ( 'banana', 'mandarinas', 'anana')

# podemos usar el metodo len()
print("\nel tamaño de la tupla frutas es :")
print(len(frutas))

# podemos acceder aon su indice al igual que listas.
primer_fruta = frutas[0]
segunda_fruta = frutas[1]

# podemos pasar la tupla frutas a una lista
lista = list(frutas)





