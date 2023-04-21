# LISTAS

# La división de higiene está trabajando en un control de stock para productos
# sanitarios. Debemos realizar la carga de
# una compra de productos de prevención de contagio, de cada una debe obtener los
# siguientes datos:
# · El tipo ("barbijo", "jabón" o "alcohol")
# · El precio
# · La cantidad de unidades
# · La marca
# · El fabricante
# Se debe informar los datos de la compra procesados para poder iniciar el control de
# stock.


import os 
os.system("cls")

lista_producto = []
lista_precio = []
lista_unidades = []
lista_marca = []
lista_fabricante = []
iteraciones = 3

for i in range(iteraciones):    
   
    # ─────────────────────  Tipo de producto ──────────────────────  
    lista_iteracion = ["primer","segundo","tercer"]          
    tipo_producto = input(f"\nPor favor, ingrese el {lista_iteracion[i]} tipo de producto\n"
                           "      \"barbijo\", \"jabón\", \"alcohol\" ─────► " )
    
    # Coloco las 2 condiciones la compleja y la mas simplificada   
    while (tipo_producto != "barbijo") and (tipo_producto != "jabón") and (tipo_producto != "alcohol"):
            tipo_producto = input("\nError, debe ingresar los productos correctos\n"
                                " \"barbijo\", \"jabón\", \"alcohol\" " )    
    # while tipo_producto not in ["barbijo","alcohol","jabón"]:           
    #         tipo_producto = input("\nError, debe ingresar los productos correctos\n"
    #                             " \"barbijo\", \"jabón\", \"alcohol\" ─────► " )    
    
    lista_producto.append(tipo_producto)   
    
    # ─────────────────────  Precio de producto ──────────────────────
            
    while True:
        try:
            precio = input("\nPor favor, ingrese el precio del producto ─────► ")
            if precio.isdigit():
                precio = int(precio)
                lista_precio.append(precio)                
                break
            else:
                print("\nError, no se aceptan caracteres ‼ ")                
        except ValueError:
                print("\nError, ingrese un valor valido por favor ‼ ─────► ")                
    # ─────────────────────  Unidad de producto ──────────────────────        
    while True:
        try:
            unidades = input("\nPor favor, ingrese la cantidad de unidades ─────► ")
            if unidades.isdigit():
                unidades = int(unidades)
                lista_unidades.append(unidades)                   
                break
            else:
                print("\nError, no se aceptan caracteres ‼ ")                
        except ValueError:
                print("\nError, ingrese un valor valido por favor ‼ ─────► ")                
    
    # ─────────────────────  Marca de producto ──────────────────────                
    while True:        
            marca = input("\nIngrese la marca del producto, por favor ─────► ")    
            if marca.isalpha():
                lista_marca.append(marca)                   
                break
            print("\nError, ingrese una marca valida ─────► ")
    
    # ─────────────────────  Fabricante del producto ──────────────────────                
    while True:        
            fabricante = input("\nIngrese el fabricante del producto, por favor ─────► ")    
            if fabricante.isalpha():
                lista_fabricante.append(fabricante)                           
                break
            print("\nError, ingrese una marca valida ─────► ")
    os.system("cls")
 
# formato vertical        
# for i in range(iteraciones):
#     print(f"Producto: {lista_producto[i]} precio: ${lista_precio[i]} unidades: {lista_unidades[i]} Marca:{lista_marca[i]} fabricante:{lista_fabricante[i]}" )

# forma horizontal 
print("  "+"_"*73)   
print( f" {'|   producto ':^13}|{'precio':^8}|{'unidades':^5}|{'Marca ':^20}|{'Fabricante':^20}|")
print("  "+"¯"*73)
for i in range(iteraciones):
    print(f" |   {lista_producto[i]:>8} |{'$'+str(lista_precio[i]):>8}| {lista_unidades[i]:>7}|{lista_marca[i]:^20}|{lista_fabricante[i]:^20}|" )
print("  "+"¯"*73)

# una forma de imprimirlo es de esta de forma cruda
# for i in lista_producto:
#     print(i)    

