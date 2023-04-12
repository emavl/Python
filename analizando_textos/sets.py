"""
   su particularidad es porque solo admite elementos unicos
 No admite que se repitan los elementos, si sucede eso no lo agrega
 No es una estructura ordenada - y no son inmutables
 no puedo agregar listas y diccionarios
 
 Los set se declaran con los corchetes {}

 """

miSet = set([1,2,3,4,5])

# otra forma de declararlo

otroSet = {1,2,3}

print(miSet)

# que podemos hacer con ellos . . .

# agregar un tuple, por que es inmutable al igual que el set
miSet1 = set((1,2,3,(4,5,6),7,8,9))
print("con el tuple dentro "+ str(miSet1))

print("\npuedo preguntar si se encuentra \nel valor 2 dentro de mi set"
"y eliminarlo con .remove(2) ")
print(2 in miSet)
if 2 in miSet:
  # podemos remover
  miSet.remove(2)

print("impirmo el set " + str(miSet))
print()

#podemos unir set´s
print("podemos unir 2 sets s1 + s2 y asignarlo a s3")
s1 = {1,2,3}
s2 = {4,5,6}
s3 = s1.union(s2)
print(s3)


# o similar el discard
s3.discard(4)
print("\nusando el discard y remove")
print(s3)

print("\nagregamos el numero 10 con add")
s1.add(10)
print(s1)

# metodo pop - elimina un elemento aleatorio
print("\neliminamos con pop")
s1.pop()
print(s1)
# No me permite elegir el indice con el pop para borrar - ej: pop(3)

print ("\ny con clear eliminamos el set por completo")
s1.clear()
print(s1)
print()
