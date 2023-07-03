from os import system
import re, random, json

insumo_csv = ("parciales/primer_parcial/Insumos .csv")
system("cls")

# ---------------------------------- F u n c i o n e s ------------------------------------------------

# S i s t e m a


def system_pause() -> None:
    print()
    system('pause')


def limpiar_consola() -> None:
    """ Funcion que limpia a consola """
    print("\n")
    system("pause")
    system("cls")


def pedir_texto(mensaje: str, mensaje_error: str) -> str:
    """chequea que el texto igresado
    por el usuario no contenga numeros,
    espacio o salto de linea, retornando el texto.

    Arg:
        mensaje (str) ──► Peticion del usuario en formato string.
        mensaje_error (str) ──► Error del dato ingresado.

    Return:
        Texto (str) ──► El string ingresado.
    """
    while True:
        try:
            texto = input(mensaje)
            size = texto.split()
            for i in size:
                if i.isalpha():
                    break
                raise ValueError
            break
        except ValueError:
            print(mensaje_error)

    return texto


def pedir_numero(mensaje: str, mensaje_error: str) -> int:
    """
    Peticion al usuario de un numero

    arg:

    mensaje (str) -> Mensaje del usuario para peticion de datos.
    mensaje_error (str) -> mensaje de error

    """
    while True:
        try:
            num = input(mensaje)
            if num.isalpha():
                raise ValueError
            break
        except ValueError:
            print(mensaje_error)

    return int(num)

# ------- M a n e j o    d e    A r c h i v o s  --------------

###  Stock 
def fx_stock_disponible(lista: list[dict]) -> list[dict]:
    """ Agrego una clave 'stock' y un valor int, random
    a cada diccionario de la lista. 

    Args:
        lista (list[dict]): lista de diccionarios.

    Returns:
        list[dict]: Lista de diccionarios.
    """
    return list(map(lambda producto: {**producto, 'stock': int(random.randint(0, 10))}, lista))

### Normalizar datos
def fx_normalizar_datos(lista: str) -> list:
    """
    Lee un archivo de texto con información sobre personajes y devuelve una lista de diccionarios con la información normalizada.
    Args:
        lista (str): El nombre del archivo que contiene los datos a normalizar.
    Returns:
        list: Una lista de diccionarios, donde cada diccionario representa un personaje y contiene su información normalizada.
    """
    primera = True
    insumos = []
    with open(lista, encoding="utf8") as archivo:

        for linea in archivo:
            if primera:
                lista = linea
                primera = False
            else:
                campos = re.findall(r'[^",\n]+', linea)
                id = int(campos[0])
                nombre = campos[1]
                marca = campos[2].strip().capitalize()
                precio = float(campos[3].replace('$', ''))
                caracteristicas = campos[4].split("|!*|")
                insumo = {'id': id, 'nombre': nombre, 'marca': marca,
                          'precio': precio, 'caracteristicas': caracteristicas}

                insumos.append(insumo)

    print("Se han cargado los datos del archivo Insumos.csv correctamente")

    return insumos

### json
def fx_guardar_json(lista: list) -> None:
    """ Funcion que guarda en un archivo json.

    Args:
        lista (list): Lista de insumos.
    """    
    insumos_json = []
    for i in lista:
        if 'Disco Duro' in i['nombre']:
            insumos_json.append({
                            "id": str(i.get('id')),
                            "nombre": i.get('nombre'),
                            "marca": i.get('marca'),
                            "precio": str(i.get('precio')),
                            "caracteristicas": i.get('caracteristicas'),
                        })
                
    print(insumos_json)       

    with open("Parciales/primer_parcial/insumos.json", "w") as archivo:
            json.dump(insumos_json, archivo,indent = 2)

    print("Se ha generado el archivo insumos.json correctamente.")  

### Lectura del archivo json
def leer_json():
    """ Funcion que imprime el archivo json.
    """    
    with open("Parciales/primer_parcial/insumos.json", "r") as archivo:
        insumos_json = json.load(archivo)

    print("Insumos con nombre 'Disco Duro':")
    print(" "+"_"*174)
    print(f"|{'id':^4}|{'Producto':^40}|{'marca':^20}| {'Precio':^9}| {'C a r a c t e r i s i t i c a s':^94}| ")
    print(f" "+"─"*174)
    for insumo_json in insumos_json:
        caracteristicas = ", ".join(insumo_json['caracteristicas'])
        print(f"|{(insumo_json['id']):>4}|{(insumo_json['nombre']):^40}|{(insumo_json['marca']):^20}|${(insumo_json['precio']):>9}| {(caracteristicas):^94}|")
    print(f"─"*175)

# --------------- Fx aplicadas a los insumos ----------------

def fx_cantidad_marcas(lista: list):
    """
    Muestra las marcas de la lista pasada por parametro.

    Args:
    lista -> (list): lista de insumos

    """
    marca = {}

    for insumo in lista:
        if insumo['marca'] not in marca:
            marca[insumo['marca']] = 1
        else:
            marca[insumo['marca']] += 1

    system("cls")
    print(" "+"_"*30)
    print(f"| {'Marca':^16}|{' Cantidades':^9} |")
    print(f" "+"─"*30)
    for marca, cantidad in marca.items():
        print(f"| {marca:^15} | {cantidad:^10} |")
        print(f"─"*31)


def fx_pedir_numero_min_max(mensaje: str, mensaje_error: str, min: int, max: int) -> int:
    """
    Permite seleccionar dentro de un rango de numeros a eleccion del usuario

    Args:
    mensaje (str): (input del usuario)
    mensaje_error (str): (mensaje de error)
    min (int): (parametro asignado por el usuario)
    mira (int): (parametro asignado por el usuario)

    return (int): (retorna un entero comprendido por el min y el max)
    """
    while True:
        try:
            num = int(input(mensaje))
            if (num < min or num > max):
                raise ValueError
            break
        except ValueError:
            print(mensaje_error)

    return num


def fx_insumos_por_marca(lista: list):
    """
    funcion que contiene un conjunto de funciones fx 

    Args:
    lista (list) -> archivo csv pasado por argumento.
    """
    insumos_por_marca = fx_cargar_marca(lista)
    fx_print_insumo_marca(insumos_por_marca)


def fx_cargar_marca(lista: dict[list]) -> dict[list]:
    """
    Fx que itera sobre una lista pasada por parametro
    guardando las variables necesarias para luego cargarlas
    a un diccionario.

    Args:
    lista (dict[list]) -> lista
    return (dict) -> diccionario
    """
    diccionario = {}

    for insumo in lista:
        marca = insumo['marca']
        if marca not in diccionario:
            diccionario[marca] = []

        diccionario[marca].append(insumo)
    return diccionario


def fx_print_insumo_marca(insumos_por_marca: dict[list]) -> None:
    """
    Fx que imprime La marca por sobre el insumo,
    mostrando sus cantidades por casda marca.

    Args:
    insumos_por_marca (dict[list]) -> diccionario de listas.
    """
    lista_insumos = []

    print(" "+"_"*88)
    print(f"|{'Marca':^16}|\t\t\t{'insumo':^10}\t\t\t   | {'precio':^9}  | ")
    print(f" "+"─"*88)

    for marca, lista_insumos in insumos_por_marca.items():
        print(f"| { marca:^16}|{' ':^55} |\t\t|")
        for insumo in lista_insumos:
            nombre = insumo.get('nombre')
            precio = insumo.get('precio')
            print(f"| \t\t  | {nombre:^55}| ${precio:^9} |")
            print(f"|"+" "*19+"─"*69)
            # system('pause')
        # print()
        print(f"─"*88)


# ---------------------- C a r a c t e r i s t i c a s  -----------------------------------


def fx_traer_caract(lista: list[dict], key: str) -> list:
    """ para cada elemento 'item' en la lista,
    la funcion lambda devuelve el valor  de la clave key
    pasada por parametro.

    Args:   list -> lista recibida por parametros. 

    return -> Listado de listas con las caracteristicas.

    """
    return list(map(lambda item: item[key], lista))


def fx_buscar_caracteristica(input_text: str, caracteristicas: list) -> list:
    """ Busca dentro de la lista la caracteristica
    pasada por parametro input_text.

    Args:
        input_text (str): _description_
        caracteristicas (list): _description_

    Returns:
        list: _description_
    """

    lista = []
    for caracteristica in caracteristicas:
        if re.findall(input_text, caracteristica, re.IGNORECASE):
            lista.append(caracteristica)

    return lista


def print_caracterisiticas(caract_encontrada: str, lista_2: list) -> None:
    """ Imprime las caracteristicas encontradas.

    Args:
        caract_encontrada (str): caracteristica
        lista_2 (list): lista
    """
    lista_id = []
    error = "No se encontro esa caracteristica"

    print(" "+"_"*126)
    print(
        f"|{'M a r c a':^16}|\t\t\t\t\t{'C a r a c t e r i s t i c a ':^30}\t\t\t\t\t\t| ")
    print(f" "+"─"*126)

    if len(caract_encontrada) > 0:
        for caracteristica in caract_encontrada:
            for insumo in lista_2:
                if caracteristica in insumo['caracteristicas']:
                    id_insumo = insumo["id"]

                    if id_insumo not in lista_id:
                        nombre = insumo["nombre"]
                        marca = insumo["marca"]
                        lista_id.append(id_insumo)
                        cadena = (f"{marca}")
                        cadena1 = (
                            f"{nombre} su caracteristica es {caracteristica}\t")
                        print("|{:^16}| {:>105}|". format(cadena, cadena1))

    else:
        print("|{:^119}|".format(error))
    print(f""+"─"*128)


def fx_input_caracteristica(lista_1: list, lista_2: list) -> None:
    """ Conjunto de funciones que trabajan con la lista filtrada
    y la lista completa, donde el usuario ingresada la caracteristica a buscar. 

    Args:
        lista_1 (list): lista filtrada.
        lista_2 (list): lista completa.
    """
    input_text = input("\nIngrese una característica: ")
    caract_encontrada = fx_buscar_caracteristica(input_text, lista_1)
    print_caracterisiticas(caract_encontrada, lista_2)


def fx_caracteristicas(lista_1: list[list], lista_2: list) -> None:
    """ Filtra en una lista, el listado de listas con las caracteristicas.
    para ser usada en la fx input_caracteristica()

    Args:
        lista_1 (list[list]): Listado de listas con las caracteristicas.
        lista_2 (list): Lista completa. 
    """
    lista_filtrada = []

    resp = "si"

    for item in lista_1:
        for item_2 in item:
            lista_filtrada.append(item_2)

    while resp.lower() == "si":

        fx_input_caracteristica(lista_filtrada, lista_2)

        resp = input("\n¿Desea buscar otra caracteristica? (si/no):")
        while resp != "si" and resp != "no":
            resp = input("\nError, responda por si o por no, gracias")


def fx_insumo_por_caracteristica(lista: dict[list]) -> None:
    """ Conjunto de funciones para listar las caracteristicas de los insumos
    buscada por el usuario. 

    Args:
        lista (dict[list]): Lista 
    """
    caracteristicas = fx_traer_caract(lista, 'caracteristicas')
    fx_caracteristicas(caracteristicas, lista)


# ------------------------- O r d e n a m i e n t o  ---------------------------------------


def fx_ordenamiento(lista: list[dict], key_1: str, key_2: str) -> list:
    """ Ordenamiento de doble criterio, de la lista pasada por parametros. 
    Args:
        lista (list[dict]): lista a ordenar
        key_1 (str): primer criterio
        key_2 (str): segundo criterio

    Returns:
        list: lista ordenada
    """
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i][key_1] > lista[j][key_1] or (lista[i][key_1] == lista[j][key_1] and lista[i][key_2] < lista[j][key_2]):
                lista[i], lista[j] = lista[j], lista[i]

    return lista


def fx_print_ordenamiento(lista: list[dict], key_1: str, key_2: str) -> None:
    """ Imprsión del ordenamiento propio de la lista pasada por parametros.

    Args:
        lista (list[dict]): lista ordenada.
        key_1 (str): primer criterio.
        key_2 (str): segundo criterio.
    """

    lista_ordenada = fx_ordenamiento(lista, key_1, key_2)

    print(" "+"_"*143)
    print(f"|{'ID':^4}|\t{'N o m b r e ':^53}|{'M a r c a':^18}|{'Precio':^10}|{'C a r a c t e r i s i t c a s':^50} |")
    print(f" "+"─"*143)

    for item in lista_ordenada:
        print(
            f"|{item['id']:>4}|{item['nombre']:^55}|{item['marca']:^18}| ${item['precio']:>8}|{item['caracteristicas'][0]:>50} |")
        print(f"|"+"─"*143)


# --------------------------->  A p p   P r i n c i p a l


def fx_ejecutar_menu() -> int:
    """
    Menú principal con diferentes tipos de opcíones numericas
    utilizado la funcion (fx_pedir_numero_min_max)

    Returns -> (int) retorna un entero.
    """
    opcion = fx_pedir_numero_min_max("=================================\n"
                                     "        ♦ - Insumos - ♦       \n"
                                     "=================================\n"
                                     " 1) Traer datos desde archivo.\n"
                                     " 2) Listar cantidad por marca.\n"
                                     " 3) Listar insumos por marca.\n"
                                     " 4) Buscar insumo por caracteristica.\n"
                                     " 5) Listar insumos ordenados.\n"
                                     " 6) Realizar compras.\n"
                                     " 7) Guardar datos actualizados.\n"
                                     " 8) Leer Json.\n"
                                     " 9) Actualizar precios.\n"
                                     " 10) Agregar nuevo producto.\n"
                                     " 11) Salir\n"
                                     "=================================\n"
                                     "\n opcion n° ────► ",
                                     "\nError, no contamos con esa opción ‼ \n", 1, 11)

    return opcion


# ------------------------- C o m p r a s  ---------------------------------------

def fx_guardado_txt(lista_de_compras: dict):
    
    resp = input("\nDesea guardar la lista en un archivo txt? ")
    if resp.lower() == 'si':
        total = 0
        with open("Parciales/primer_parcial/compras.txt", 'w') as archivo_txt:
            archivo_txt.write("#------------------------------------------------------------#\n"
                              "\t\tI n f o - B a u s      F a c t u r a c i o n  \n"
                              "#------------------------------------------------------------#\n\n")

            for producto_encontrado in lista_de_compras.values():
                total += producto_encontrado['precio']
                archivo_txt.write(
                    f"\tMarca: {producto_encontrado['marca']:^5}, producto: {producto_encontrado['Producto']:^5}, cantidad:{producto_encontrado['cantidad']:^3}, $:{producto_encontrado['precio']:^5} \n")
                
            archivo_txt.write(f"\n\nTotal - ${total}")
            
            archivo_txt.write("\b#------------------------------------------------------------#\n"                             
                              "#------------------------------------------------------------#\n\n")
    else:
        print("\nMuchas gracias por su compra ")
                

def fx_print_compras(lista_de_compras: dict):
    
    """funcion que imprime por consola los productos.

    Args:
        lista_de_compras (list): listado de productos.
    """
    total = 0

    print("\nProductos ingresados")

    for producto_encontrado in lista_de_compras.values():
        total += producto_encontrado['precio']
        print(
            f"\tMarca: {producto_encontrado['marca']:^5}, producto: {producto_encontrado['Producto']:^5}, cantidad:{producto_encontrado['cantidad']:^3}, $ {round(producto_encontrado['precio'], 2)} ")

    print(f"\nTotal - ${round(total, 2):.2f}")
 
 
def fx_carrito(marca_elegida: str, lista_de_marcas): 
    """ Fn donde se genera la compra del insumo.

    Args:
        marca_elegida (str): marca elegida por el usuario.
        lista_de_marcas (_type_): listado de las marcas.
    """    
    lista_de_compras = {}
    listado = {}
    
    print( f"\nContamos con los siguientes productos de la marca {marca_elegida}\n")

    for marca in lista_de_marcas:
        print(
            f"\t (N° articulo: {marca['id']}) ────> {marca['nombre']} - ${marca['precio']:^5}, ")

    id_del_producto = pedir_numero("\nPor favor, ingrese el número del articulo que desea : ",
                                "Error de tipo, inténtelo nuevamente ")

    producto_elegido = list(filter(lambda item: item['id'] == id_del_producto, lista_de_marcas))

    for producto in producto_elegido:
        if producto['id'] in lista_de_compras:

            cantidad = pedir_numero((f"\n¿Su carrito cuenta con el {producto['nombre']} cuantos mas necesita? "),
                                    "\nError de tipeo ingrese un numero por favor, gracias !")
            if cantidad > producto['stock']:
                print(
                    f"\n No contamos con la cantidad que usted solicita del producto {producto['nombre']}")
            else:
                for item in lista_de_compras.values():
                    item['cantidad'] += cantidad
                    item['precio'] = (
                        item['precio'] + (producto['precio'] * cantidad))
        else:
            system("cls")
            cantidad = pedir_numero((f"\n¿Cuantas unidades va a necesitar del producto  {producto['nombre']}? "),
                                    "\nError de tipeo ingrese un numero por favor, gracias !")
            system("cls")
            if cantidad > producto['stock']:
                print(
                    f"\n No contamos con la cantidad que usted solicita del producto: ( {producto['nombre']} )")
            else:
                precio = producto['precio']
                producto['stock'] -= cantidad
                listado = {'marca': producto['marca'],
                        'Producto': producto['nombre'],
                        'cantidad': cantidad,
                        'precio': (cantidad * precio)}
                lista_de_compras[producto['id']] = listado
                    
    return lista_de_compras
    

def fx_carrito_de_compras(lista_principal: list) -> list:
    """ funcion que agrega los productos seleccionados por el usuario

    Args:
        lista_principal (list): lista principal

    Returns:
        lista_de_compras(list): lista con los productos.
    """
    resp = "si"
    lista_de_compras = {}
    
    print("=========================================================\n"
    "        ♦ - Bienvenido al sector de compras  - ♦       \n"
    "=========================================================\n")

    while resp.lower() == "si":

        marca_elegida = pedir_texto("\nPor favor, ingrese la marca del producto: ",
                                    "Error de tipo, inténtelo nuevamente ").capitalize()
        system('cls')

        lista_de_marcas = list(
            filter(lambda item: item['marca'] == marca_elegida, lista_principal))

        if len(lista_de_marcas) == 0:
            print(f"No contamos con la marca {marca_elegida}")
        else:
            lista_de_compras.update(fx_carrito(marca_elegida, lista_de_marcas)) 

        resp = input("\n¿ Desea comprar otro producto ? (si/no): ")
        system("cls")
        while resp.lower() not in ["si", "no"]:
            resp = input("\nError, responda 'si' o 'no': ")
    
    system("cls")
    
    if len(lista_de_compras) == 0:
        print("\nNo se an ingresado productos")
    else:
        fx_print_compras(lista_de_compras)
        
        resp = input("\n¿Desea conservar estos productos? (si/no): ")
        while resp.lower() not in ["si", "no"]:
            resp = input("\nError, responda 'si' o 'no': ")

        if resp == "no":        
            lista_de_compras.clear()
        else:
            fx_guardado_txt(lista_de_compras)
    



# --------------- F u n c i o n e s     s i m p l e s -------------------


def opcion_1(lista: list, flag: bool):
    """
    funcion que contiene un conjunto de fx 

    Args:
    lista (list) -> archivo csv pasado por argumento
    flag (bool) -> bandera para cambia un estado.

    Returns:
    flag (bool) -> Utilizada como chequeo .
    insumos (list) -> Devuelve una lista de diccionarios.                
    """
    system("cls")
    insumos = fx_normalizar_datos(lista)
    insumos = fx_stock_disponible(insumos)
    flag = True
    limpiar_consola()

    return flag, insumos


def opcion_2(lista: list, flag: bool) -> bool:
    """
    funcion que contiene la fx cantidad marcas 

    Args:
    lista (list) -> archivo csv pasado por argumento.
    flag (bool) -> bandera para cambiar un estado.

    """
    system("cls")
    if (flag):
        fx_cantidad_marcas(lista)
    else:
        print("Por favor debe de cargan los datos desde el archivo\npara poder mostrar la cantidad de insumos por marca.")

    limpiar_consola()


def opcion_3(lista: list, flag: bool) -> bool:
    """
    funcion que contiene un conjunto de fx. 

    Args:
    lista (list) -> archivo csv pasado por argumento.
    flag (bool) -> bandera para cambiar un estado.

    """

    system("cls")
    if (flag):
        fx_insumos_por_marca(lista)
    else:
        print("Por favor debe de cargan los datos desde el archivo\npara poder listar insumos por marca.")

    limpiar_consola()


def opcion_4(lista: list, flag: bool) -> bool:
    """
    funcion que contiene un conjunto de fx. 

    Args:
    lista (list) -> archivo csv pasado por argumento.
    flag (bool) -> bandera para cambiar un estado.

    """

    system("cls")
    if (flag):
        fx_insumo_por_caracteristica(lista)
    else:
        print("Por favor debe de cargan los datos desde el archivo\npara poder listar insumos por caracteristica.")
    limpiar_consola()


def opcion_5(lista: list, flag: bool) -> bool:
    """ funcion que contiene un conjunto de fx. 

    Args:
        lista (list) -> archivo csv pasado por argumento.
        flag (bool) -> bandera para cambiar un estado.

    """

    system("cls")
    if (flag):
        fx_print_ordenamiento(lista, 'marca', 'precio')
    else:
        print("Por favor debe de cargan los datos desde el archivo\npara poder listar insumos ordenados.")
    limpiar_consola()


def opcion_6(lista: list, flag: bool) -> bool:
    """ funcion que contiene un conjunto de fx. 

    Args:
        lista (list) -> archivo csv pasado por argumento.
        flag (bool) -> bandera para cambiar un estado.

    """

    system("cls")
    if (flag):
        fx_carrito_de_compras(lista)
    else:
        print("Por favor debe de cargan los datos desde el archivo\npara poder generar una orden de compras.")
    limpiar_consola()


def opcion_7(lista: list, flag: bool) -> bool:
    """ funcion que contiene un conjunto de fx. 

    Args:
        lista (list) -> archivo csv pasado por argumento.
        flag (bool) -> bandera para cambiar un estado.

    """

    system("cls")
    if (flag):
        fx_guardar_json(lista)
    else:
        print("Por favor debe de cargan los datos desde el archivo\npara poder generar el archivo json.")
    limpiar_consola()
    
   
def opcion_8(lista: list, flag: bool) -> bool:
    """ funcion que contiene un conjunto de fx. 

    Args:
        lista (list) -> archivo csv pasado por argumento.
        flag (bool) -> bandera para cambiar un estado.

    """

    system("cls")
    if (flag):
        leer_json(lista)
    else:
        print("Por favor debe de cargan los datos desde el archivo\npara poder leer el archivo json.")
    limpiar_consola()
   
    
def opcion_9(lista: list) -> list:
    """ funcion que contiene un conjunto de fx. 

    Args:
        lista (list) -> archivo csv pasado por argumento.
        flag (bool) -> bandera para cambiar un estado.

    """

    system("cls")

    # insumos = fx_actualizar_datos(lista)
    insumos = fx_stock_disponible(insumos)

    # with open("Parciales/primer_parcial/insumos.csv", "w") as archivo:
    #     for linea in lista:
    #         archivo.write(f"{linea}")

    # fx_insumos_por_marca(archivo)
    limpiar_consola()
    return insumos


# ----------------------- M e n ú   -   P r i n c i p a l  -----------------------


def app_insumos(insumos) -> None:
    """ Programa principal

    Args:
        insumos (list): Archivo CSV 
    """
    flag = False
    entro = True
    
    while True:
        match fx_ejecutar_menu():
            case 1:
                if entro:
                    flag, insumos = opcion_1(insumos, flag)
                    entro = False
                else:
                    system("cls")
                    print("\nYa se normalizaron los datos\n")
            case 2:
                opcion_2(insumos, flag)
            case 3:
                opcion_3(insumos, flag)
            case 4:
                opcion_4(insumos, flag)
            case 5:
                opcion_5(insumos, flag)
            case 6:
                opcion_6(insumos, flag)
            case 7:
                opcion_7(insumos, flag)
            case 8:
                opcion_8(insumos, flag)
            case 9:
                pass
            # case 10:
            #     agregar_nuevo_producto()
            case 11:
                system("cls")
                print("Gracias por su visita, vuelva pronto ♥")
                break

# -------------------------------------------------------------------------------------------------------


# app_insumos(insumo_csv)

lista = fx_normalizar_datos(insumo_csv)
lista = fx_stock_disponible(lista)

   
def guardar_csv(insumos):
    nombre_archivo = input(
        "Ingrese el nombre del archivo para guardar los datos (incluya la extensión .csv): ")
    if not nombre_archivo.lower().endswith('.csv'):
        print("El archivo debe tener extensión .csv.")
        return

    with open(nombre_archivo, 'w', encoding="utf-8") as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(['ID', 'NOMBRE', 'MARCA', 'PRECIO', 'CARACTERISTICAS'])
        for insumo in insumos:
            caracteristicas = insumo[4]
            writer.writerow([insumo[0], insumo[1], insumo[2],
                            insumo[3], caracteristicas])

    print(
        f"Se han guardado los datos en el archivo {nombre_archivo} correctamente.")
    
 
def actualizar_precios(insumos):

    insumos = list(map(lambda insumo: {
        'ID': insumo[0],
        'NOMBRE': insumo[1],
        'MARCA': insumo[2],
        'PRECIO': round(float(insumo[3].replace("$", "")) * 1.084, 2),
        'CARACTERISTICAS': insumo[4]
    }, insumos))
    guardar_csv(insumos)
    print("Se han actualizado los precios correctamente.")    