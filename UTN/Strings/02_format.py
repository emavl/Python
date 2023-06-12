from os import system
system('cls')

producto = " capuccino"
productoDos = " expresso"
productoTres = " latte "

valor1 = 1.60 
valor2 = 1.10 
valor3 = 3.95
iva =  0.12

total1 = valor1 + (valor1*iva)
total2 = valor2 + (valor2*iva)
total3 = valor3 + (valor3*iva)

# formato de lista centralizado.
print("formato de lista centralizado.")
print("{:^20} {:^20} {:^20} ". format("\n|   PRODUCTO","|VALOR SIN IVA|","TOTAL      |"))
print("{:^20} {:^20} {:^20} ". format(producto,valor1,total1))
print("{:^20} {:^20} {:^20} ". format(productoDos, valor2, total2))
print("{:^20} {:^20} {:^20} ". format(productoTres, valor3, total3))
print()
print(" formato de lista izquierda.")
print("{:^20} {:^20} {:^20} ". format("\nPRODUCTO", "VALOR SIN IVA", "TOTAL"))
print("{:<20} {:<20} {:<20} ". format(producto, valor1, total1))
print("{:<20} {:<20} {:<20} ". format(productoDos, valor2, total2))
print("{:<20} {:<20} {:<20} ". format(productoTres, valor3, total3))
print()
print("formato de lista derecha.")
print("{:>20} {:>20} {:>20} ". format("\nPRODUCTO", "VALOR SIN IVA", "TOTAL"))
print("{:>20} {:>20} {:>20} ". format(producto, valor1, total1))
print("{:>20} {:>20} {:>20} ". format(productoDos, valor2, total2))
print("{:>20} {:>20} {:>20} ". format(productoTres, valor3, total3))
