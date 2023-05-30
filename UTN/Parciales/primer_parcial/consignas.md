# Consignas a desarrollar

### Realizar un menú que permita al usuario trabajar con las siguientes opciones

- *__Traer datos desde archivo__*: guardará el contenido del archivo Insumos.csv en una colección. Tener en cuenta que las características de los insumos deben estar en un tipo de colección integrada.  
  
- *__Listar cantidad por marca__*: mostrará todos las marcas indicando la cantidad de insumos que corresponden a esa marca.

- *__Listar insumos por marca__*: mostrará cada marca indicando el nombre del insumo, y precio de cada uno de los insumos que correspondan a esa marca.

- *__Buscar insumo por característica:__* el usuario ingresa una característica (Por ejemplo, “Compatible con Windows”). La opción deberá listar todos los insumos que poseen dicha característica.

- *__Listar insumos ordenados:__* mostrará id, descripción, precio, marca y la primera característica de todos los productos, ordenados por marca de la A-Z y ante de marca por precio descendente.

- *__Realizar compras:__* A partir del ingreso de una marca, el programa mostrará todos los productos de esa marca. El usuario elegirá un producto y la cantidad y se agrega al carrito de compras. Esta acción se repetirá mientras el usuario lo desee (con distintas marcas). Al finalizar mostrar el total de la compra. Si el usuario acepta la misma se deberá generar un archivo txt con la factura de la compra. Indicando cantidad, producto, subtotal y total de la compra.

- *__Guardar Json:__* Generará un archivo de tipo Json con todos los productos cuyo nombre contenga “Disco Duro”

- *__Leer Json:__* permitirá mostrar un listado con los insumos guardados en el archivo Json de la opción 7.
- *__Actualizar precios:__* Dada la inflación del mes de Mayo, es necesario aplicar un aumento del 8.4% a todos los productos (utilizar la función map). Guardar en el archivo Insumos.csv todos los productos actualizados.
Salir del programa

### Nota: Utilizar la función filter y reduce en los puntos que sea necesario
