from os import system
import re
insumo_csv = ("Parciales/primer_parcial/insumos.csv")
system("cls")

# ---------------------------------- F u n c i o n e s ------------------------------------------------

# S i s t e m a


def limpiar_consola() -> None:
    """ Funcion que limpia a consola """
    print("\n")
    system("pause")
    system("cls")

# A r c h i v o


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
                marca = campos[2].strip()
                precio = float(campos[3].replace('$', ''))
                caracteristicas = campos[4].split("|!*|")
                insumo = {'id': id, 'nombre': nombre, 'marca': marca,
                          'precio': precio, 'caracteristicas': caracteristicas}

                insumos.append(insumo)

    print("Se han cargado los datos del archivo Insumos.csv correctamente")

    return insumos


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
    lista (dict[list]) -> archivo csv pasado por
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
                                     "\n opcion n° ────► ",
                                     "\nError, no contamos con esa opción ‼ \n", 1, 11)

    return opcion


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

# ----------------------- M e n ú   -   P r i n c i p a l  -----------------------


def app_insumos(insumos: list):
    flag = False

    while True:

        match fx_ejecutar_menu():
            case 1:
                flag, insumos = opcion_1(insumos, flag)
            case 2:
                opcion_2(insumos, flag)
            case 3:
                opcion_3(insumos, flag)
            # case 4:
            #     if(flag):
            #         pass
            #     else:
            #         print("No se puede buscar insumo por caracteristica si primero no se cargan los datos desde el archivo.")
            # case 5:
            #     if(flag):
            #         pass
            #     else:
            #         print("No se puede listar insumos ordenados si primero no se cargan los datos desde el archivo.")
            # case 6:
            #     if(flag):
            #         pass
            #     else:
            #         print("No se puede realizar compras si primero no se cargan los datos desde el archivo.")
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
            # case 9:
            #     if(flag):
            #         actualizar_precios(insumos)
            #     else:
            #         print("No se puede actualizar precios si primero no se cargan los datos desde el archivo.")
            # case 10:
            #     agregar_nuevo_producto()
            case 11:
                system("cls")
                print("Gracias por su visita, vuelva pronto ♥")
                break
# -------------------------------------------------------------------------------------------------------


archivo = fx_normalizar_datos(insumo_csv)


# app_insumos(insumo_csv)


def fx_buscar_caracteristica(input_text, caracteristicas):

    lista = []
    for caracteristica in caracteristicas:
        if re.findall(input_text, caracteristica, re.IGNORECASE):
            lista.append(caracteristica)

    return lista


# caracterisitcas = ["color", "size","Resolución Full HD", "500gb", "compatible con linux", "compatible con windows"]

# # Solicitar entrada del usuario
# caract = input("Ingrese una característica: ")
# caract_encontrada = fx_buscar_caracteristica(caract, caracterisitcas)

# if len(caract_encontrada) > 0:
#     print("Opciones sugeridas:")
#     for item in caract_encontrada:
#         print(item)
# else:
#     print("no se encontro esa caracteristica")


def fx_traer_caract(lista: list[dict], key: str) -> list:
    """
    esta funcion carga a una lista,
    la caracteristica indicada por el usuario.

    Args:   list -> lista recibida por parametros 

    return -> Listado de las caracteristicas

    """
    elemento = []

    for item in lista:
        elemento.append(item[key])

    return elemento


def fx_insumo_por_caracteristica(lista: dict[list]):

    caracteristicas = fx_traer_caract(lista, 'caracteristicas')
    lista_filtrada = []
    error = "No se encontro esa caracteristica"
    lista_id = []

    for item in caracteristicas:
        for item_2 in item:
            lista_filtrada.append(item_2)

    caract = input("Ingrese una característica: ")
    caract_encontrada = fx_buscar_caracteristica(caract, lista_filtrada)

    print(" "+"_"*120)
    print(f"|{'Marca':^16}|\t\t\t\t\t{'C a r a c t e r i s t i c a ':^20}\t\t\t\t\t| ")
    print(f" "+"─"*120)

    if len(caract_encontrada) > 0:
        for caracteristica in caract_encontrada:
            for insumo in lista:
                if caracteristica in insumo['caracteristicas']:
                    id_insumo = insumo["id"]

                    if id_insumo not in lista_id:
                        nombre = insumo["nombre"]
                        marca = insumo["marca"]
                        lista_id.append(id_insumo)
                        cadena = (f"{marca}")
                        cadena2 = (f"{nombre} su caracteristica es {caracteristica}\t")
                        # print(cadena+cadena2)
                        print("|{:^16}| {:>98}|". format(cadena, cadena2))
                        # print( f"|{marca:^16}|\t {nombre} su caracteristica es {caracteristica}\t|")
                        
    else:
        print( "|{:^119}|".format(error))
    print(f""+"─"*120)

fx_insumo_por_caracteristica(archivo)

# def eliminar_elementos(lista, patron):
#     patron_regex = re.compile(patron)
#     lista_filtrada = [elemento for elemento in lista if not patron_regex.search(elemento)]
#     return lista_filtrada

# # Ejemplo de uso
# mi_lista = ['apple [fruit]', 'banana', 'orange [fruit]', 'grape [fruit]']

# lista_filtrada = eliminar_elementos(mi_lista, r'\[.*\]')
# print(lista_filtrada)
