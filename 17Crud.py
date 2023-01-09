#----- MÉTODOS DE LISTAS -----
"""  
C : Create (Crea registros)
R : Read (Lee registros)
U : Update (Actualiza registros)
D : Delete (Elimina registros)
"""

numbers = [1, 2, 3, 4, 5]

# append(): Añade un ítem al final de la lista.
numbers.append(6)
print(numbers)

# insert(): Agrega un ítem a la lista en un índice específico.
numbers.insert(3, "Ali")
print(numbers)

flowers = ['Rosas', 'Tulipanes', 'Girasoles']
newList = numbers + flowers
print(newList)

# index(): Para saber en que posición está un elemento (error si no aparece).
print(newList.index('Tulipanes'))
newList[newList.index('Tulipanes')] = 'Amo los Tulipanes'
    # newList[posición a cambiar]='Dato a cambiar'
print(newList)

# remove(): Borra un elemento de la lista
newList.remove('Ali')
print(newList)

# pop(): Extrae un ítem de la lista y lo borra.
newList.pop(6)
print(newList)

# reverse(): Le da la vuelta a la lista actual.
newList.reverse()
print(newList)

# sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
ordenar_Lista = [5, 1, 3, 2, 4]
ordenar_Lista.sort()
print(ordenar_Lista)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)  #Pero no funciona cuando hay listas con elementos diferentes

# clear(): Vacía todos los ítems de una lista.

# extend(): Une una lista a otra.

# count(): Cuenta el número de veces que aparece un ítem.
