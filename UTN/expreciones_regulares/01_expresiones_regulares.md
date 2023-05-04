# Expreciones regulares  

 Una expresión regular o regex es una cadena de texto especial que ayuda a encontrar patrones en los datos.

 Se puede usar una regex para verificar si existe algún patrón en un tipo de datos diferente.
 Para usar Regex en Python primero debemos importar el módulo Regex que se llama *Re*.

[Match -](#match)
[Search -](#search)
[Findall -](#buscando-todas-las-coincidencias-usando-findall)
[Sub -](#reemplazo-de-una-subcadena)
[Split](#Division-de-texto-usando-RegEx-Split)

 La importamos de la siguiente manera  

```py
import re
```

## *__metodos en RE__*

Para encontrar un patrón usamos diferentes metodos de *__re__*. Conjuntos de caracteres que permiten buscar una coincidencia en una cadena.

* *__re.match()__*: Las búsquedas solo al comienzo de la primera línea de la cadena y devuelven objetos coincidentes si se encuentra, de lo contrario no devuelve ninguno.
* *__re.search__*: Devuelve un objeto de coincidencia si hay uno en cualquier lugar de la cadena, incluidas las cadenas multilíneas.
* *__re.findall__*: Devuelve una lista que contiene todas las coincidencias
* *__re.split__*: Toma una cadena, la divide en los puntos de partido, devuelve una lista
* *__re.sub__*:  Reemplaza una o muchas coincidencias dentro de una cadena
<br>
<br>

## *__match__*

```py
# syntac
re.match(subcadena, cadena, re.I)
# La subcadena es una cadena o un patrón, la cadena es el texto que buscamos un patrón, re.i es caso ignorar
```

```py
mi_cadena = "Esto se trata de expresiones regulares, donde trata las repeticiones"
mi_cadena2 = "Esto no va a tratase de expresiones regulares"


# imprimo el match donde uno me muestra que encontro algo dentro del mi_cadena
# y en donde no pudo me imprime None")

print(re.match("Esto se trata", mi_cadena2)) # None porque no encontro "Esto se trata"
match = re.match("Esto se trata", mi_cadena)
 #<re.Match object; span=(0, 13), match='Esto se trata'>
print(match)

print("-"*40)

# imprimo span que es una tupla formada por dos valores el que comienzo y el que final"
comienzo, final = match.span()
print(f"donde el comienzo es {comienzo} y el final es {final}")

# para comprobar el None podemos utilizar estas 3 formas
 if not (match == None)
 if match != None:
 if match is not None:
     print("contiene el texto")
 else:
     print("No contiene el texto")

# donde en vez de imprimir si es none me dice si contiene o no el texto

```

Como puede ver en el ejemplo anterior, el patrón que estamos buscando
(o la subcadena que estamos buscando) es *__"Esto se trata"__*.
La función de coincidencia devuelve un objeto *__solo__* Si el texto comienza con el patrón.

```py
import re

txt = 'Me encanta enseñar Python y JavaScript'
match = re.match('Me gusta enseñar', txt, re.I)
print(match)  # None
```

La cadena no tiene una cadena con *Me gusta enseñar*, por lo tanto, no había coincidencia y el método de coincidencia no devolvió ninguno.
<br>
<br>

## *__Search__*

```py
# syntax
re.match(sbucadena, cadena, re.I)
# La subcadena es un patrón, la cadena es el texto que buscamos un patrón, re.i es caso Ignorar la bandera
```

```py
import re

txt = "Python es el idioma más hermoso que un ser humano ha creado.Recomiendo a Python para un primer lenguaje de programación
"
# Devuelve un objeto con SPAN y Match
match = re.search('primer', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='primer'>

# Podemos obtener la posición de inicio y finalización de la cadena como tupla usando el tramo(span) = span.
span = match.span()
print(span)     # (100, 105)

# Vamos a encontrar la posición de comienzo y final desde el (span)
comienzo, final = span
print(comienzo, final)  # 100 105
substring = txt[comienzo:final]
print(substring)       # primer
```

<br>

Como puede ver, la búsqueda es mucho mejor que el match porque puede buscar el patrón en todo el texto. La búsqueda devuelve un objeto de coincidencia con una primera coincidencia que se encontró, de lo contrario devuelve *__none__*. Una función *__re__* mucho mejor es *__findall__*. Esta función verifica el patrón a través de toda la cadena y devuelve todas las coincidencias como una lista.

<br>
<br>

## Buscando todas las coincidencias usando *__findall__*

*findall()* Devuelve una lista con todas las ocurrencias

```py
encontrar_todo = re.findall("trata", mi_cadena, re.I)

#Findall nos muestra la cantidad de ocurrencias colocandolo en una lista"
print(encontrar_todo)
txt = "Modelo de expliiiicacion de expreciones"

#Como tambien nos muestra la cantidad de ocurrencias de la misma si estan repetidas"
print(re.findall("i+", txt)) # ['iiii', 'i', 'i']

 # Donde el + significa(encontrame la letra i en el caso de ser repetidas)

------------------------------------------------

txt = '''Python es el language más hermoso que un ser humano ha creado.
Recomiendo a Python para un primer lenguaje de programación'''

# Devuelve una lista con las veces que aparece la palabra lenguaje en este caso.
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']

print(re.findall(" ", txt)
puedo pedirle que me encuentre todos los espacios en blanco
[' ', ' ', ' ', ' ']

```

<br>

La palabra *__" lenguaje "__* se encontró dos veces en la cadena.
 Ahora buscaremos ambas palabras - Python y python en la cadena:
<br>
<br>

```py
txt = '''Python es el idioma más hermoso que un ser humano ha creado.
Recomiendo a Python para un primer lenguaje de programación'''

# Devuelve la lista
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']

```

<br>

Utilizando en la expresion *__re.I__* o *__re.IGNORECASE__* se incluyen letras minúsculas y mayúsculas. Si no tenemos la bandera Re.i, tendremos que escribir nuestro patrón de manera diferente. Vamos a verlo:

<br>

```py
txt = "Python es el idioma más hermoso que un ser humano ha creado.Recomiendo a Python para un primer lenguaje de programación "

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

```

<br>

## *__Reemplazo de una subcadena__*

```py
txt = '''Python es el idioma más hermoso que un ser humano ha creado.
Recomiendo a Python para un primer lenguaje de programación'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript es el lenguaje más hermoso que un ser humano ha creado.
# O
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript es el lenguaje más hermoso que un ser humano ha creado.

mi_cadena3 =" esta Leccion es para darnos una leccion de una list"

# reemplazo parte de la cadena por otra

print(re.sub("Esto se trata","hoy vamos a hablar", mi_cadena))
#hoy vamos a hablar de expresiones regulares, donde trata las repeticiones

# Otras formas de hacelo
 
print(re.sub("leccion","LECCION", mi_cadena3))
 # esta Leccion es para darnos una LECCION de una list

print(re.sub("leccion|Leccion","LECCION", mi_cadena3))
# esta LECCION es para darnos una LECCION de una list

print(re.sub("[l|L]eccion","LECCION", mi_cadena3))
# esta LECCION es para darnos una LECCION de una list
```

<br>

## *__División de texto usando RegEx Split__*

```py
txt = '''Soy maestra y me encanta enseñar.
No hay nada tan gratificante como educar y empoderar a las personas.
Encontré la enseñanza más interesante que cualquier otro trabajo.
¿Esto te motiva a ser maestro?'''
print(re.split('\n', txt)) # dividido usando \n - símbolo de fin de línea
```

```sh
['Soy maestra y me encanta enseñar. "," No hay nada tan gratificante como educar y empoderar a las personas "." Encontré la enseñanza más interesante que cualquier otro trabajo "." ¿Te motiva a ser maestro?']
```

## Escribiendo RegEx Patronas

Para declarar una variable de cadena se utilizan comillas simples o dobles. Para declarar la variable RegEx r''. El siguiente patrón sólo identifica manzana con minúsculas, para hacerlo insensible a mayúsculas y minúsculas deberíamos reescribir nuestro patrón o añadir una bandera

```py
import re

regex_pattern = r'manzana'

txt = 'Manzana y plátano son frutas.Un viejo dicho dice que una manzana al día, una forma de médico ha sido reemplazada por un plátano al día, mantiene al médico muy lejos. '

matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# Para distinguir entre mayúsculas y minúsculas agregamos la bandera '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Manzana', 'manzana']

# o podemos usar un conjunto de métodos de caracteres

regex_pattern = r'[Aa]pple'  # Esto significa que la primera letra podría ser Apple o Apple

matches = re.findall(regex_pattern, txt)
print(matches)  # ['Manzana', 'manzana']


```

* [ ]:  Un conjunto de caracteres
  * [a-c] significa, conjunto de las letras a o b o c.
  * [a-z] significa, cualquier letra dentro del abecedario en minuscula.
  * [A-Z] significa, cualquier letra dentro del abecedario en mayuscula.
  * [0-3] significa, conjunto de numeros del 1 al 3
  * [0-9] significa, conjunto de numeros del 1 al 9
  * [A-Za-z0-9] cualquier caracter, si es de la (a - z), (A - Z) o (0 al 9)
* \\ :  usa para escapar de los caracteres especiales
  * \d  coincidir donde la cadena contiene dígitos (números de 0-9)
  * \D  coincidir donde la cadena no contiene dígitos
*.: Cualquier personaje excepto el caracter de nueva línea (\ n)

* ^: comienza con
  * r'^subcadena' eg r'^love', Una oración que comienza con una palabra amor
  * r'[^abc] significa no A, no B, no c.
* $: ends with
  * r'subcadena$ ' eg r'love$' , oración que termina con una palabra amor
* *: cero o más veces
  * r'[a]*' significa una opcional o puede ocurrir muchas veces.
* +: una o muchas veces
  * r'[a]+' significa al menos una vez (o más)
* ?: cero o una vez
  * r'[a]?' significa cero veces o una vez
* {3}: Exactamente 3 caracteres
* {3,}: Al menos 3 caracteres
* {3,8}: 3 a 8 caracteres
* |: or o
  * r'manzana | banana' significa manzana o un plátano
* (): Capture and group

Usemos ejemplos para aclarar los meta caracteres anteriores

<br>

## *__Square Bracket__*

Utilicemos corchetes para incluir minúsculas y mayúsculas

```py
regex_pattern = r'[Aa]pple' # este corchete significa A o a
txt = 'La manzana y la banana son frutas. Un viejo dicho dice que una manzana y una banana al día mantiene al médico muy lejos.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
```

Si quisieramos buscar tambien la banana sería de la siguiente manera

```py
regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket means either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']
```

Using the square bracket and or operator , we manage to extract Apple, apple, Banana and banana.

### Escape character(\\) in RegEx

```py
regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want
```

### One or more times(+)

```py
regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!
```

### Period(.)

```py
regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times 
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### Zero or more times(\*)

Zero or many times. The pattern could may not occur or it can occur many times.

```py
regex_pattern = r'[a].*'  # . any character, * any character zero or more times 
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### Zero or one time(?)

Zero or one time. The pattern may not occur or it may occur once.

```py
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
```

### Quantifier in RegEx

We can specify the length of the substring we are looking for in a text, using a curly bracket. Let us imagine, we are interested in a substring with a length of 4 characters:

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']
```

### Cart ^

* Starts with
  
```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']
```

* Negation

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']
```

## 💻 Exercises: Day 18

### Exercises: Level 1

 1. What is the most frequent word in the following paragraph?

```py
    paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
```

```sh
    [
    (6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')
    ]
```

2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

```py
points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-4) # 12
```

### Exercises: Level 2

1. Write a pattern which identifies if a string is a valid python variable

    ```sh
    is_valid_variable('first_name') # True
    is_valid_variable('first-name') # False
    is_valid_variable('1first_name') # False
    is_valid_variable('firstname') # True
    ```

### Exercises: Level 3

1. Clean the following text. After cleaning, count three most frequent words in the string.

    ```py
    sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

    print(clean_text(sentence));
    I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
    print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
    ```
