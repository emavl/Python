import os
import json
import csv

insumos = r"UTN\file\mi_archivo.txt"

def menu_personas()-> str :
    """menu de opciones para personas

    Returns:
        int: opcion seleccionada
    """
    print("*** Gestion de opciones ***")
    print("------------")
    print("1. Traer datos desde archivo")
    print("2. Listar cantidad por marca")
    print("3. Listar insumos por marca")
    print("4. Buscar insumo por caracteristica")
    print("5. Listar insumos ordenados")
    print("6. Realizar compras")
    print("7. Guardar datos actualizados")
    print("8. Leer Json")
    print("9. Actualizar precios")
    print("10. Agregar nuevo producto")
    print("11. Salir")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def app_insumos(insumos:list):
    flag_traer_datos = False
    while True:
        os.system("cls")

        match menu_personas():
            case 1:
                cargar_datos_desde_archivo(insumos)
                cargar_marcas_disponibles()
                flag_traer_datos = True
            case 2:
                if(flag_traer_datos):
                    listar_cantidad_por_marca(insumos)
                else:
                    print("No se puede listar cantidad por marca si primero no se cargan los datos desde el archivo.")
            case 3:
                if(flag_traer_datos):
                    listar_insumos_por_marca(insumos)
                else:
                    print("No se puede listar insumos por marca si primero no se cargan los datos desde el archivo.")
            case 4:
                if(flag_traer_datos):
                    buscar_insumo_por_caracteristica(insumos)
                else:
                    print("No se puede buscar insumo por caracteristica si primero no se cargan los datos desde el archivo.")
            case 5:
                if(flag_traer_datos):        
                    listar_insumos_ordenados(insumos)
                else:
                    print("No se puede listar insumos ordenados si primero no se cargan los datos desde el archivo.")
            case 6:
                if(flag_traer_datos):        
                    realizar_compras(insumos)
                else:
                    print("No se puede realizar compras si primero no se cargan los datos desde el archivo.")
            case 7:
                formato_exportacion = input("Seleccione el tipo de formato de exportación (csv/json): ")
                if formato_exportacion.lower() == 'csv':
                    guardar_csv(insumos)
                elif formato_exportacion.lower() == 'json':
                    if(flag_traer_datos):        
                        guardar_json(insumos)
                    else:
                        print("No se puede guardar json si primero no se cargan los datos desde el archivo.")    
                else:
                    print("Formato de exportación inválido.")
                
            case 8:
                leer_json()
            case 9:
                if(flag_traer_datos):        
                    actualizar_precios(insumos)
                else:
                    print("No se puede actualizar precios si primero no se cargan los datos desde el archivo.")
            case 10:
                agregar_nuevo_producto()
            case 11:
                confirma = input("Confirma salida? s/n")
                if(confirma == "s"):
                    print("Hasta luego!")
                    break
            case _:
                print("Opción invalida. Por favor, seleccione una opcion valida del menu.")
        input("Presione enter para continuar...")
print("Fin del programa")
           
        

def cargar_datos_desde_archivo(insumos):
    # insumos = []
    nombre_archivo = 'Parciales/primer_parcial/insumos.csv'
    # nombre_archivo = "parcial\\Insumos.csv"
    with open(nombre_archivo, "r", encoding="utf-8") as archivo_csv:
            for linea in archivo_csv:
                # print(linea)
                insumos.append(linea.replace("\n", "").split(","))
    print("Se han cargado los datos del archivo Insumos.csv correctamente")
    # print(insumos)

def cargar_marcas_disponibles():
    global marcas_disponibles
    archivo_marcas = r'C:\Users\crist\OneDrive\Escritorio\parcial\marcas.txt'
    with open(archivo_marcas, 'r') as archivo:
        marcas_disponibles = archivo.read().splitlines()
    print("Se han cargado los datos del archivo marcas.txt correctamente")

def listar_cantidad_por_marca(insumos: dict):
    marcas = {}

    for insumo in insumos:

        if insumo[2] in marcas:
            marcas[insumo[2]] += 1
        else:
            marcas[insumo[2]] = 1
    print("                 *** Lista de Cantidad por Marca ***")
    print("---------------------------------------------------------")
    print(" Marca      Cantidad")
    print("---------------------------------------------------------")
    
    for marca, cantidad in marcas.items():
        if(marca != "MARCA"):
            print(f'{marca}: {cantidad}')

def listar_insumos_por_marca(insumos: dict):
    marcas = {}
    for insumo in insumos:
        if insumo[2] in marcas:
            marcas[insumo[2]].append(insumo)
        else:
            marcas[insumo[2]] = [insumo]

    print("                 *** Lista de Insumos por Marca ***")
    print("---------------------------------------------------------")
    for marca, insumos in marcas.items():
        print(f'{marca}:')
        for insumo in insumos:
            print(f' - {insumo[1]}, {insumo[3]}')

def buscar_insumo_por_caracteristica(insumos):
    caracteristica_buscar = input("Ingrese la caracteristica a buscar: ")
    insumos_con_caracteristica = []

    for insumo in insumos:
        if caracteristica_buscar in insumo[4]:
            insumos_con_caracteristica.append(insumo)

    print(f"Insumos con característica '{caracteristica_buscar}':")
    for insumo in insumos_con_caracteristica:
        print(f"- {insumo[1]} ({insumo[2]})")

def obtener_marca(insumo):
    return insumo[2]

def obtener_precio(insumo):
    precio = insumo[3].replace('$', '')
    return precio
    # return -float(precio)


def listar_insumos_ordenados(insumos):
    ordenados = sorted(insumos, key=obtener_marca)
    # ordenados = sorted(ordenados, key=obtener_precio)
    
    for insumo in ordenados:
        caracteristicas = insumo[4]
        print(f"{insumo[0]} - {insumo[1]} - {insumo[2]} - {insumo[3]} - {caracteristicas}")


def realizar_compras(insumos):
    carrito = {}
    total = 0

    while True:
        marca = input("Ingrese la marca de los insumos que desea comprar: ")
        insumos_marca = list(filter(lambda i: i[2] == marca, insumos))
        if not insumos_marca:
            print(f"No hay insumos de la marca {marca}.")
            continue
        print(f"Insumos de la marca {marca}:")
        for i, insumo in enumerate(insumos_marca):
            print(f"{i + 1}. {insumo[1]} - {insumo[3]}")

        opcion = input("Seleccione el insumo que desea comprar (ingrese el número): ")
        if not opcion.isdigit() or int(opcion) not in range(1, len(insumos_marca) + 1):
            print("Opción inválida.")
            continue

        insumo_seleccionado = insumos_marca[int(opcion) - 1]
        cantidad = input("Ingrese la cantidad que desea comprar: ")
        if not cantidad.isdigit():
            print("Cantidad inválida.")
            continue

        insumo_a_comprar = insumo_seleccionado[3].replace('$', '')

        subtotal = float(insumo_a_comprar) * int(cantidad)
        total += subtotal
        carrito[insumo_seleccionado[1]] = {'cantidad': int(cantidad), 'subtotal': subtotal}

        continuar = input("¿Desea comprar mas insumos? (s/n): ")
        if continuar.lower() == 'n':
            break

    if not carrito:
        print("No se compro ningun insumo.")

    print("Detalle de la compra:")
    for nombre, detalle in carrito.items():
        print(f"{detalle['cantidad']} x {nombre} - ${detalle['subtotal']}")
    print(f"Total: ${total}")

    confirmar = input("¿Desea confirmar la compra? (s/n): ")
    if confirmar.lower() != 's':
        print("Compra cancelada.")
    
    nombre_archivo = input("Ingrese el nombre del archivo para guardar la factura (sin extensión): ")
    archivo_factura = f"{nombre_archivo}.txt"

    with open(archivo_factura, "w") as archivo:
        archivo.write("Factura de la compra\n")
        archivo.write("--------------------\n")
        archivo.write("Detalle de la compra:\n")
        for nombre, detalle in carrito.items():
            archivo.write(f"{detalle['cantidad']} x {nombre} - ${detalle['subtotal']}\n")
        archivo.write(f"Total: ${total}\n")

    print(f"La factura se ha generado y guardado en el archivo {archivo_factura}.")

def guardar_json(insumos):
    insumos_json = []
    for insumo in insumos:
        if "Disco Duro" in insumo[1]:
            insumos_json.append({
                "id": insumo[0],
                "nombre": insumo[1],
                "marca": insumo[2],
                "precio": str(insumo[3]),
                "caracteristicas": insumo[4]
            })

    with open("insumos.json", "w") as archivo:
        json.dump(insumos_json, archivo)

    print("Se ha generado el archivo insumos.json correctamente.")

def guardar_csv(insumos):
    nombre_archivo = input("Ingrese el nombre del archivo para guardar los datos (incluya la extensión .csv): ")
    if not nombre_archivo.lower().endswith('.csv'):
        print("El archivo debe tener extensión .csv.")
        return
    
    with open(nombre_archivo, 'w', encoding="utf-8") as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(['ID', 'NOMBRE', 'MARCA', 'PRECIO', 'CARACTERISTICAS'])
        for insumo in insumos:
            caracteristicas = insumo[4]
            writer.writerow([insumo[0], insumo[1], insumo[2], insumo[3], caracteristicas])
    
    print(f"Se han guardado los datos en el archivo {nombre_archivo} correctamente.")


def leer_json():
    with open("insumos.json", "r") as archivo:
        insumos_json = json.load(archivo)

    print("Insumos con nombre 'Disco Duro':")
    for insumo_json in insumos_json:
        print(f"ID: {insumo_json['id']}, Nombre: {insumo_json['nombre']}, Marca: {insumo_json['marca']}, Precio: {insumo_json['precio']}, Características: {insumo_json['caracteristicas']}")

def actualizar_precios(insumos):

    # Actualizar precios
    insumos = list(map(lambda insumo: {
        'ID': insumo[0],
        'NOMBRE': insumo[1],
        'MARCA': insumo[2],
        'PRECIO': round(float(insumo[3].replace("$","")) * 1.084, 2),
        'CARACTERISTICAS': insumo[4]
    }, insumos))
    guardar_csv(insumos)
    print("Se han actualizado los precios correctamente.")

def agregar_nuevo_producto():
    global insumos, marcas
    print("Ingrese los datos del nuevo producto:")
    nombre = input("Nombre: ")
    marca = input("Marca: ")
    precio = input("Precio: ")
    caracteristicas = []
    
 # Se limita la cantidad de características a un mínimo de una y un máximo de tres
    print("Ingrese las características (entre 1 y 3):")
    while len(caracteristicas) < 3:
        caracteristica = input(f"Característica {len(caracteristicas) + 1}: ")
        if caracteristica:
            caracteristicas.append(caracteristica)
        else:
            break

    nuevo_producto = {
        'ID': len(insumos) + 1,
        'NOMBRE': nombre,
        'MARCA': marca,
        'PRECIO': float(precio),
        'CARACTERISTICAS': caracteristicas
    }
    insumos.append(nuevo_producto)
    marcas.append(marca)
    print("El nuevo producto ha sido agregado.")