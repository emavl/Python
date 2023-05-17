empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0

fruits = ['plátano ',' naranja ',' mango ',' limón']                     # list of fruits
vegetables = ['Tomate', 'papa', 'repollo', 'cebolla', 'zanahoria']      # list of vegetables
animal_products = ['leche ',' carne ',' mantequilla ', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finlandia ',' Estonia ',' Dinamarca ',' Suecia ',' Noruega']

# Imprima las listas y la longitud
print('Frutas:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Number of countries:', len(countries))

# Lista de modificación

fruits = ['plátano ',' naranja ',' mango ',' limón '] 
first_fruit = fruits[0] # Estamos accediendo al primer elemento utilizando su índice
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Accessing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)       # lemon
print(second_last)      # mango

# Slicing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4] # Devuelve todas las frutas
#Esto también es dar el mismo resultado que el anterior
print("Si no establecemos dónde detenerse, se necesita todo")
all_fruits = fruits[0:] # print("Si no establecemos dónde detenerse, se necesita todo")
orange_and_mango = fruits[1:3] # it does not include the end index
orange_mango_lemon = fruits[1:]

fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[-4:] # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1] # it does not include the end index
orange_mango_lemon = fruits[-3:]


fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits[0] = 'Avocado' 
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

# checking items
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# Append
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
print(fruits)

# insert
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'mango', 'lime','lemon',]
print(fruits)

# remove
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']

# pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()     
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)     
print(fruits)       # ['orange', 'mango'] 

# del 
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]     
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]     
print(fruits)       # ['orange', 'lemon']
del fruits
# print(fruits)       # This should give: NameError: name 'fruits' is not defined

# clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()     
print(fruits)       # []

# copying a lits

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()     
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

# join
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )

# join with extend
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
print("\nusando extend")
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )

# count
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

# index
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24)) 
# Reverse
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)  
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) 

# sort
print("\nsort")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits) 
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) 
ages.sort(reverse=True)
print(ages) 