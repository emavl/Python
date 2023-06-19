
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


def fx_buscar_caracteristica(input_text, caracteristicas):

    lista = []
    for caracteristica in caracteristicas:
        if re.findall(input_text, caracteristica, re.IGNORECASE):
            lista.append(caracteristica)

    return lista


def fx_input_caracteristica(lista_1: list, lista_2: list) -> None:

    lista_id = []
    error = "No se encontro esa caracteristica"

    caract = input("\nIngrese una característica: ")
    caract_encontrada = fx_buscar_caracteristica(caract, lista_1)

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


def fx_print_caracteristicas(lista_1: list[list], lista_2: list) -> None:

    lista_filtrada = []

    resp = "si"

    for item in lista_1:
        for item_2 in item:
            lista_filtrada.append(item_2)

    while resp.lower() == "si":

        fx_input_caracteristica(lista_filtrada, lista_2)

        resp = input("\n¿Desea buscar otra caracteristica? (si/no):  ")
        while resp != "si" and resp != "no":
            resp = input("\nError, responda por si o por no, gracias !  ")


def fx_insumo_por_caracteristica(lista: dict[list]) -> None:

    caracteristicas = fx_traer_caract(lista, 'caracteristicas')
    fx_print_caracteristicas(caracteristicas, lista)