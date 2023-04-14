# ahora llevamos un caso a la vida real
# a la hora de utilizar datos
cliente = {'nombre': (input("ingrese un nombre ")), 'apellido': (input("ingrese un apellido "))}
consulta = (cliente['nombre'])
consulta1 = (cliente['apellido'])
print("su nombre es " + consulta + " y su apellido es "+consulta1)

# podemos tener diccionarios dentro de diccionarios o listas

dic = {'c1': 55, 'c2': [10, 20, 30], 'c3': {'s1': 100, 's2': 200}}
print(dic['c2'])
# si quiero ver el indice 1
print(dic['c2'][1])
print("mostrandome el numero 20 ")
print("si queremos ver un diccionario dentro de otro")
print(dic['c3']['s2'])
