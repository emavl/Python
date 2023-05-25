
[Archivos de texto -](#archivos-de-texto)
[Archivos de binarios -](#archivos-binarios)
[Abrir un archivo -](#open)
[Administrador de contexto -](#with)
[Seek -](#seek)

## *__Archivos__*

El texto plano en un archivo de texto (.txt) se refiere a un archivo que contiene solo caracteres de texto sin ningún formato adicional, como negrita, cursiva, tamaño de fuente, color, también puede contener codigo __ACSII__.  
  
Almacenamos nuestros datos en diferentes formatos de archivo. Además del manejo de los mismos, también nos encontramos con diferentes formatos tales como (.txt, .json, .xml, .csv, .tsv, .excel)

. Primero, familiaricémonos con el manejo de archivos con formato de archivo común (.txt).

![Assignment Operators](../archivos/img/archivos.jpeg)

## Archivos de texto

Los archivos de texto contienen caracteres
legibles, es posible no solo leer dicho contenido
sino también modificarlo usando un editor de
texto.

## *__Archivos binarios__*

 Un archivo binario es cualquier archivo que no se
pueda interpretar en forma de texto: una imagen,
un sonido o incluso un archivo comprimido

![Assignment Operators](../archivos/img/modo_apertura.jpeg)

```py
# Sintaxis
open('Nombre_del_archivo', mode) # mode (r, a, w, x, t,b)  podría ser lectura, escritura, o actualizar.
```

- r - Read - Valor por default. Abre un archivo para leer, Devuelve un error si el archivo no existe
- r+ - abre un archivo para escritura y lectura. El puntero del archivo está localizado al comienzo del archivo.
- a - Append - Abre un archivo para agregar, crea el archivo si no existe
- w - Write - Abre un archivo para escribir, crea el archivo si no existe
- w+ abre un archivo para escritura y lectura. Sobreescribe el archivo si este ya existe. Si el archivo no existe lo crea.
- x - Create - Crea el archivo especificado, devuelve un error si el archivo existe
- t - Text - Valor por defecto. Modo de texto
- b - Binario - Modo binario (por ejemplo, imágenes)

## *__Open__*

```py
f = open('./Archivos/Lectura_archivo_ejemplo.txt')
txt = f.read() # lo leemos 
print(type(txt))
print(txt)

f = open('./Archivos/Lectura_archivo_ejemplo.txt')
# En lugar de imprimir todo el texto, imprimamos los primeros 10 caracteres del archivo de texto.
txt = f.read(10) 
print(txt)

# Con readline vamos a leer la primer linea 
linea = f.readline()

# Lea todo el texto Línea por línea y devuelve una lista de líneas
lineas = f.readlines()
```

```sh
# output
<class 'str'> "el tipo del archivo"
"Texto que encontraremos dentro de archivo"

-------------------

"Texto que" 

------------------

<class 'list'>
['Esto es un ejemplo para mostrar cómo abrir un archivo y leer. \ n ',' Esta es la segunda línea del texto.']
```

## *__Seek__*

El método seek permite modificar la posición
actual del puntero

```python
archivo = open('archivo.txt', 'r+')
archivo.seek(11)
print(archivo.tell()) #Esta en el byte 11
linea = archivo.readline()
print(linea,end="") # Hola mundo
archivo.close()
```

## *__with__*

Después de abrir un archivo, debemos cerrarlo. Hay una alta tendencia de olvidar cerrarlos. Hay una nueva forma de abrir archivos usando *__With__* - Cierra los archivos por sí solo, y se encarga de administrar los recursos, lo podemos encontrar en diferentes lenguajes.

```py
with open('./Archivos/Lectura_archivo_ejemplo.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```

```sh
# output

<class 'list'>
['Esto es un ejemplo para mostrar cómo abrir un archivo y leer.',' Esta es la segunda línea del texto.']
```

## Abrir archivos para escribir y actualizar

Para escribir en un archivo existente, debemos agregar un modo como parámetro a la función *open ()*:

- "A" - append - agregará al final del archivo, si el archivo no lo hace, crea un nuevo archivo.
- "W" - Write - sobrescribirá cualquier contenido existente, si el archivo no existe, crea uno.

Agregaremos algún texto al archivo que hemos estado leyendo:

```py
with open('./Archivos/Lectura_archivo_ejemplo.txt','a') as f:
    f.write('Este texto tiene que agregarse al final')
```

El método a continuación crea un nuevo archivo, si el archivo no existe:

```py
with open('./Archivos/Lectura_archivo_ejemplo.txt','w') as f:
    f.write('Este texto se escribirá en un archivo recién creado.')
```

## *__Archivo CSV__*

El CSV es un tipo de documento que representa
los datos de forma parecida a una tabla, es decir,
organizando la información en filas y columnas.
Las columnas son separadas, por un signo de
puntuación (, ; .) u otro carácter y las diferentes
filas suelen separarse por un salto de línea.

## *__Jason__*

El nombre es un acrónimo de las siglas en inglés
de JavaScript Object Notation.
JSON es un formato para el intercambio de datos
basado en texto. Por lo que es fácil de leer tanto
para una persona como para una máquina.

El paquete json permite traducir un diccionario a
formato JSON utilizando el método *__dump__*.

```py
import json

data = {}
data['clientes'] = []
data['clientes'].append({ 'nombre': 'Juan', 'edad': 27})
data['clientes'].append({ 'nombre': 'Ana', 'edad': 26})

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4, ensure_ascii=False )
```