""" TUPLAS
- Los elementos están separados por espacios luego de las comas
- Puede contener cualquier tipo de datos
-  posición de la tupla tiene un índice
- Es inmutable y por lo tanto no puede ser modificada, lo que permite proteger mejor la data si no queremos que se modifique por error
- Las tuplas son solo de lectura
"""

numbers = (1, 2, 3, 3, 4)
names = ('Ali', 'Emi', 'Eli', 'Eli', 'Eli')
print(type(names))

# Acceder a un elemento
print(numbers[1])

# Encontrar un elemento
print('Ali' in names)


#----- MÉTODOS

# Buscar la posición de un elemento
print(numbers.index(3))  #Posición 2
print(names.index('Emi'))  #Posición 1

# Ver cuantas veces está el elemento
print(numbers.count(3))  # 2 veces el número 3
print(names.count('Eli')) # 3 veces Eli

# Pasar de tupla a lista
my_lista = list(numbers)  #Ahora si podemos editar la lista, agregando o eliminando
print(my_lista) 

my_lista.append(5)

# Pasar de lista a tupla
my_tupla = tuple(my_lista)
print(my_tupla)