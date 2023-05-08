import re
from os import system

system("cls")

lista_nombres = ['Juan pablo Estevez','Hernan Solano', 'María Perez','Ismel Roj']


#     Para encontrar los que comienzan uso ^
for elemento in lista_nombres:
    if re.findall('^Sandra', elemento):
        print (elemento)
    else:
        print ("No se a encuentrado")
 
print("-"*80)        
        
#     Para encontrar los que finalizan uso $
for elemento in lista_nombres:
    if re.findall('Estevez$', elemento):
        print (elemento)   
        
print("-"*80)        
        
#     Rango de los que contengan la letra a
for elemento in lista_nombres:
    if re.findall('[a-a]', elemento):
        print (elemento)