
# DICCIONARIO

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


for i in range(2):    
    dic_producto = {}
    # ─────────────────────  Tipo de producto ──────────────────────
    if i == 0:             
     tipo_producto = input("\nPor favor, ingrese el primer tipo de producto\n"
                            " \"barbijo\", \"jabón\", \"alcohol\" " )
    elif i == 1:
     tipo_producto = input("\nPor favor, ingrese el segundo tipo de producto\n"
                            " \"barbijo\", \"jabón\", \"alcohol\" " )
    else:
     tipo_producto = input("\nPor favor, ingrese el tercer tipo de producto\n"
                            " \"barbijo\", \"jabón\", \"alcohol\" " )
        
    while (tipo_producto != "barbijo") and (tipo_producto != "jabón") and (tipo_producto != "alcohol"):
            tipo_producto = input("\nError, debe ingresar los productos correctos\n"
                                " \"barbijo\", \"jabón\", \"alcohol\" " )        
    
    dic_producto["Tipo producto"] = tipo_producto
    # ─────────────────────  Precio de producto ──────────────────────
    while True:
        try:
            precio = input("\nPor favor, ingrese el precio del producto ")
            if precio.isdigit():
                precio = int(precio)
                
                dic_producto["precio"] = precio
                break
            else:
                print("\nError, no se aceptan caracteres ‼ ")                
        except ValueError:
                print("\nError, ingrese un valor valido por favor ‼ ")                
    # ─────────────────────  Unidad de producto ──────────────────────        
    while True:
        try:
            unidades = input("\nPor favor, ingrese la cantidad de unidades ")
            if unidades.isdigit():
                unidades = int(unidades)
                
                dic_producto["unidades"] = unidades
                break
            else:
                print("\nError, no se aceptan caracteres ‼ ")                
        except ValueError:
                print("\nError, ingrese un valor valido por favor ‼ ")                
    
    # ─────────────────────  Marca de producto ──────────────────────                
    while True:        
            marca = input("\nIngrese la marca del producto, por favor ")    
            if marca.isalpha():
                
                dic_producto["marca"] = marca
                break
            print("\nError, ingrese una marca valida ")
    
    # ─────────────────────  Fabricante del producto ──────────────────────                
    while True:        
            fabricante = input("\nIngrese el fabricante del producto, por favor ")    
            if fabricante.isalpha():
                
                dic_producto["fabricante"] = fabricante
                   
                break
            print("\nError, ingrese una marca valida ")
            
    # Agrego diccionario dentro de la lista.        
    lista_producto.append(dic_producto)
            
 
    
# i va a ser cada diccionario     
for i in lista_producto:
    print(f"Producto: {i['Tipo producto']} precio: ${i['precio']} unidades: {i['unidades']} Marca:{i['marca']} fabricante:{i['fabricante']}" )
    
# itero cada diccionario por separado en este caso son 3     
# for i in lista_producto:
#     print(i)    