# para agregar elementos vamos a hacerlo de esta forma

dic = {1:'a',2:'b'}
# agrego letra c

dic[3] = 'c'
print(dic)
# para traer las claves
print(dic.keys())
#para traer los valores
print(dic.values())
# me trae el contenido completo
print(dic.items())

print("\n"+"─"*50)

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
# podemos reemplazar los datos de esta forma
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
mi_dic["pais"] = "Colombia"
print(mi_dic)

