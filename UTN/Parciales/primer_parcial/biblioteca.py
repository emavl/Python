from os import system
import re
import random
import functools

insumo_csv = ("primer_parcial/insumos.csv")
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

# ------- D a t o s   n o r m a l i z a d o s --------------


def fx_stock_disponible(lista: list[dict]) -> list[dict]:
    """ Agrego una clave 'stock' y un valor int, random
    a cada diccionario de la lista. 

    Args:
        lista (list[dict]): lista de diccionarios.

    Returns:
        list[dict]: Lista de diccionarios.
    """
    return list(map(lambda producto: {**producto, 'stock': int(random.randint(0, 10))}, lista))


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

def fx_print_compras(lista_de_compras: list):
    """funcion que imprime por consola los productos.

    Args:
        lista_de_compras (list): listado de productos.
    """
    total = 0

    print("\nProductos ingresados")

    for producto_encontrado in lista_de_compras:
        total += producto_encontrado['precio']
        print(
            f"\tMarca: {producto_encontrado['marca']:^5}, producto: {producto_encontrado['Producto']:^5}, cantidad:{producto_encontrado['cantidad']:^3}, $:{producto_encontrado['precio']:^5} ")

    print(f"\nTotal - ${total}")

    resp = input("\nDesea guardar la lista en un archivo txt? ")
    if resp.lower() == 'si':
        total = 0
        with open("Parciales/primer_parcial/compras.txt", 'w') as archivo_txt:
            archivo_txt.write("#------------------------------------------------------------#\n"
                              "Factura hecha en archivo txt\n")

            for producto_encontrado in lista_de_compras:
                total += producto_encontrado['precio']
                archivo_txt.write(
                    f"\tMarca: {producto_encontrado['marca']:^5}, producto: {producto_encontrado['Producto']:^5}, cantidad:{producto_encontrado['cantidad']:^3}, $:{producto_encontrado['precio']:^5} ")
                archivo_txt.write(f"\nTotal - ${total}")


def fx_carrito_de_compras(lista_principal: list) -> list:
    """ funcion que agrega los productos seleccionados por el usuario

    Args:
        lista_principal (list): lista principal

    Returns:
        lista_de_compras(list): lista con los productos.
    """
    resp = "si"
    lista_de_compras = []
    listado = []

    while resp.lower() == "si":

        marca_elegida = pedir_texto("\nPor favor, ingrese la marca del producto: ",
                                    "Error de tipo, inténtelo nuevamente ").capitalize()
        system('cls')

        lista_de_marcas = list(
            filter(lambda item: item['marca'] == marca_elegida, lista_principal))

        if len(lista_de_marcas) == 0:
            print(f"No contamos con la marca {marca_elegida}")
            break

        print(
            f"\nContamos con los siguientes productos de la marca {marca_elegida}\n")

        for marca in lista_de_marcas:
            print(
                f"\t────> {marca['nombre']} - ${marca['precio']:^5}, ")

        producto_elegido = pedir_texto("\nPor favor, ingrese el producto que desea : ",
                                       "Error de tipo, inténtelo nuevamente ")

        cantidad = pedir_numero((f"\n¿Del producto ♪ {producto_elegido} ♫, cuantos va a necesitar? "),
                                "\nError de tipeo ingrese un numero por favor, gracias !")

        for producto in lista_de_marcas:
            if producto['nombre'] == producto_elegido:
                if cantidad > producto['stock']:
                    print(
                        f"\n El producto {producto['nombre']}, de la marca {producto['marca']}, no contamos con la cantidad que usted solicita")
                else:
                    if producto_elegido in lista_de_compras:
                        cantidad = pedir_numero((f"\n¿Su carrito cuenta con {producto_elegido} necesita mas? "),
                                                "\nError de tipeo ingrese un numero por favor, gracias !")
                    else:
                        precio = producto['precio']
                        producto['stock'] -= cantidad
                        listado = {'marca': marca_elegida,
                                   'Producto': producto_elegido,
                                   'cantidad': cantidad,
                                   'precio': (cantidad * precio)}
                        lista_de_compras.append(listado)

        resp = input("\n¿ Desea comprar otro producto ? (si/no): ")
        while resp.lower() not in ["si", "no"]:
            resp = input("\nError, responda 'si' o 'no': ")

    return lista_de_compras


def fx_compras(lista_principal: list[dict]):
    """ conjunto de fx para el ingreso al carrito

    Args:
        lista_principal (list[dict]): lista principal.
    """
    print("=========================================================\n"
          "        ♦ - Bienvenido al sector de compras  - ♦       \n"
          "=========================================================\n")

    lista_de_compras = fx_carrito_de_compras(lista_principal)

    fx_print_compras(lista_de_compras)


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
        fx_compras(lista)
    else:
        print("Por favor debe de cargan los datos desde el archivo\npara poder generar una orden de compras.")
    limpiar_consola()


def opcion_9(lista: list) -> list:
    """ funcion que contiene un conjunto de fx. 

    Args:
        lista (list) -> archivo csv pasado por argumento.
        flag (bool) -> bandera para cambiar un estado.

    """

    system("cls")

    insumos = fx_actualizar_datos(lista)
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

    while True:

        match fx_ejecutar_menu():
            case 1:
                flag, insumos = opcion_1(insumos, flag)
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
            # case 7:
            #     formato_exportacion = input("Seleccione el tipo de formato de exportación (csv/json): ")
            #     if formato_exportacion.lower() == 'csv':
            #         guardar_csv(insumos)
            #     elif formato_exportacion.lower() == 'json':
            #         if(flag):
            #             guardar_json(insumos)
            #         else:
            #             print("No se puede guardar json si primero no se cargan los datos desde el archivo.")
            #     else:
            #         print("Formato de exportación inválido.")

            # case 8:
            #     leer_json()
            case 9:
                # insumos = opcion_9(insumo_csv)
                pass
            # case 10:
            #     agregar_nuevo_producto()
            case 11:
                system("cls")
                print("Gracias por su visita, vuelva pronto ♥")
                break


# -------------------------------------------------------------------------------------------------------


app_insumos(insumo_csv)

# lista = fx_normalizar_datos(insumo_csv)
# lista = fx_stock_disponible(lista)

# def actualizar_datos(lista: list):


#     lista_con_aumento = list(
#         map(lambda product: {**product, "precio": round(product["precio"] * 8.4, 2)}, lista))

#     return lista_con_aumento


# def guardar_archivo(lista: list,):

#     with open("Parciales/primer_parcial/insumos.csv", "w",encoding = "utf-8") as file:
#         writer = csv.DictWriter(file)
#         writer.writerows(lista)
#             # for linea in lista:
#             #     file.write(f"{linea}\n")

# lista_actualizada = actualizar_datos(lista)

# guardar_archivo(lista_actualizada)
