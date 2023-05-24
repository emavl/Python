
## *__Archivos__*

El texto plano en un archivo de texto (.txt) se refiere a un archivo que contiene solo caracteres de texto sin ningún formato adicional, como negrita, cursiva, tamaño de fuente, color, también puede contener codigo __ACSII__.  
  
Almacenamos nuestros datos en diferentes formatos de archivo. Además del manejo de los mismos, también nos encontramos con diferentes formatos tales como (.txt, .json, .xml, .csv, .tsv, .excel)

. Primero, familiaricémonos con el manejo de archivos con formato de archivo común (.txt).

```py
# Sintaxis
open('Nombre_del_archivo', mode) # mode (r, a, w, x, t,b)  podría ser lectura, escritura, o actualizar.
```

- "r" - Read - Valor por default. Abre un archivo para leer, Devuelve un error si el archivo no existe
- "a" - Append - Abre un archivo para agregar, crea el archivo si no existe
- "w" - Write - Abre un archivo para escribir, crea el archivo si no existe
- "x" - Create - Crea el archivo especificado, devuelve un error si el archivo existe
- "t" - Text - Valor por defecto. Modo de texto
- "b" - Binario - Modo binario (por ejemplo, imágenes)

```py
f = open('./Archivos/Lectura_archivo_ejemplo.txt')
txt = f.read() # lo leemos 
print(type(txt))
print(txt)
f.close()

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

## with

Después de abrir un archivo, debemos cerrarlo. Hay una alta tendencia de olvidar cerrarlos. Hay una nueva forma de abrir archivos usando *With* - Cierra los archivos por sí solo.

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

Para escribir en un archivo existente, debemos agregar un modo como parámetro a la función _open ()_:

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

