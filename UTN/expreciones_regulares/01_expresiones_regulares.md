""" Una expresión regular o regex es una cadena de texto especial que ayuda a encontrar patrones en los datos.
 Se puede usar una regex para verificar si existe algún patrón en un tipo de datos diferente.
 Para usar Regex en Python primero debemos importar el módulo Regex que se llama *Re *.
"""
[Match](#match)
[Match](#Search)
[Match](#Buscando-todas-las-coincidencias-usando-findall)
[Match](#Reemplazo-de-una-subcadena)
[Match](#División-de-texto-usando-RegEx-Split)


""" La importamos de la siguiente manera """

```py
import re
```
### metodos en RE.

Para encontrar un patrón usamos diferentes conjuntos de *re* Conjuntos de caracteres que permiten buscar una coincidencia en una cadena.

* *re.match()*: Las búsquedas solo al comienzo de la primera línea de la cadena y devuelven objetos coincidentes si se encuentra, de lo contrario no devuelve ninguno.
* *re.search*: Devuelve un objeto de coincidencia si hay uno en cualquier lugar de la cadena, incluidas las cadenas multilíneas.
* *re.findall*: Devuelve una lista que contiene todas las coincidencias
* *re.split*:	Toma una cadena, la divide en los puntos de partido, devuelve una lista
* *re.sub*:  Reemplaza una o muchas coincidencias dentro de una cadena

### match

```py
# syntac
re.match(substring, string, re.I)
# La subcadena es una cadena o un patrón, la cadena es el texto que buscamos un patrón, re.i es caso ignorar
```

```py
import re

txt = 'Me encanta enseñar a Python y JavaScript'
# Devuelve un objeto con SPAN y coincide
match = re.match('Me encanta enseñar ', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# Podemos obtener la posición de inicio y finalización del partido como tupla usando SPAN
span = match.span()
print(span)     # (0, 15)
# Vamos a encontrar la posición de inicio y parada desde el tramo
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # Me encanta enseñar
```
Como puede ver en el ejemplo anterior, el patrón que estamos buscando 
(o la subcadena que estamos buscando) es *Me encanta enseñar *.
La función de coincidencia devuelve un objeto ** solo ** Si el texto comienza con el patrón.

```py
import re

txt = 'Me encanta enseñar Python y JavaScript'
match = re.match('Me gusta enseñar', txt, re.I)
print(match)  # None
```
La cadena no tiene una cadena con *Me gusta enseñar *, por lo tanto, no había coincidencia y el método de coincidencia no devolvió ninguno.

#### Search

```py
# syntax
re.match(substring, string, re.I)
# La subcadena es un patrón, la cadena es el texto que buscamos un patrón, re.i es caso Ignorar la bandera
```
```py
import re

txt = '''Python es el idioma más hermoso que un ser humano ha creado.
Recomiendo a Python para un primer lenguaje de programación'''

# Devuelve un objeto con SPAN y Match
match = re.search('primer', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='primer'>
# Podemos obtener la posición de inicio y finalización del partido como tupla usando el tramo(span)
span = match.span()
print(span)     # (100, 105)
# Vamos a encontrar la posición de inicio y parada desde el tramo(span)
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # primer
```
Como puede ver, la búsqueda es mucho mejor que el partido porque puede buscar el patrón en todo el texto.La búsqueda devuelve un objeto de coincidencia con una primera coincidencia que se encontró, de lo contrario devuelve _none_.Una función *re *mucho mejor es *findall *.Esta función verifica el patrón a través de toda la cadena y devuelve todas las coincidencias como una lista.

#### Buscando todas las coincidencias usando *findall*


*findall()* Devuelve todos los partidos como una lista

```py
txt = '''Python es el language más hermoso que un ser humano ha creado.
Recomiendo a Python para un primer lenguaje de programación'''

# Devuelve una lista con las veces que aparece la palabra lenguaje en este caso.
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']
```

Como puede ver, la palabra * lenguaje * se encontró dos veces en la cadena. Practicemos un poco más.
Ahora buscaremos ambas palabras - Python y python en la cadena:

```py
txt = '''Python es el idioma más hermoso que un ser humano ha creado.
Recomiendo a Python para un primer lenguaje de programación'''

# Devuelve la lista
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']

```
Utilizando en la expresion * re.I * se incluyen letras minúsculas y mayúsculas.Si no tenemos la bandera Re.i, tendremos que escribir nuestro patrón de manera diferente.Vamos a verlo:

```py
txt = '''Python es el idioma más hermoso que un ser humano ha creado.
Recomiendo a Python para un primer lenguaje de programación'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

```

### Reemplazo de una subcadena

```py
txt = '''Python es el idioma más hermoso que un ser humano ha creado.
Recomiendo a Python para un primer lenguaje de programación'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript es el lenguaje más hermoso que un ser humano ha creado.
# O
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript es el lenguaje más hermoso que un ser humano ha creado.
```

Agregamos un ejemplo más.La siguiente cadena es realmente difícil de leer a menos que eliminemos el símbolo %.Reemplazar el % con una cadena vacía limpiará el texto.

```py

txt = '''%S o%y ma%%es%%tro%r% a%%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)
```

```sh
Soy maestra y me encanta enseñar.
No hay nada tan gratificante como educar y empoderar a las personas.
Encontré la enseñanza más interesante que cualquier otro trabajo.¿Esto te motiva a ser maestro?
```
## División de texto usando RegEx Split

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

Para declarar una variable de cadena, usamos una cotización única o doble.Para declarar la variable regex *r '' *.
El siguiente patrón solo identifica a Apple con minúsculas, para que sea insensible al estuche, o debemos reescribir nuestro patrón o debemos agregar una bandera.
```py
import re

regex_pattern = r'manzana'
txt = 'Apple y plátano son frutas.Un viejo dicho dice que una manzana al día, una forma de médico ha sido reemplazada por un plátano al día, mantiene al médico muy lejos. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# Para hacer que la cartera de carcas sea insensible para agregar bandera '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Manzana', 'manzana']
# o podemos usar un conjunto de métodos de caracteres
regex_pattern = r'[Aa]pple'  # Esto significa que la primera letra podría ser Apple o Apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Manzana', 'manzana']


```
* []:  A set of characters
  * [a-c] means, a or b or c
  * [a-z] means, any letter from a to z
  * [A-Z] means, any character from A to Z
  * [0-3] means, 0 or 1 or 2 or 3
  * [0-9] means any number from 0 to 9
  * [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
* \\:  uses to escape special characters
  * \d means: match where the string contains digits (numbers from 0-9)
  * \D means: match where the string does not contain digits
* . : any character except new line character(\n)
* ^: starts with
  * r'^substring' eg r'^love', a sentence that starts with a word love
  * r'[^abc] means not a, not b, not c.
* $: ends with
  * r'substring$' eg r'love$', sentence  that ends with a word love
* *: zero or more times
  * r'[a]*' means a optional or it can occur many times.
* +: one or more times
  * r'[a]+' means at least once (or more)
* ?: zero or one time
  *  r'[a]?' means zero times or once
* {3}: Exactly 3 characters
* {3,}: At least 3 characters
* {3,8}: 3 to 8 characters
* |: Either or
  * r'apple|banana' means either apple or a banana
* (): Capture and group

![Regular Expression cheat sheet](../images/regex.png)

Let us use examples to clarify the meta characters above 

### Square Bracket

Let us use square bracket to include lower and upper case

```py
regex_pattern = r'[Aa]pple' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
```

If we want to look for the banana, we write the pattern as follows:

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