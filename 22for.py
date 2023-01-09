""" FOR
- El bucle for se utiliza para recorrer los elementos de un objeto iterable (lista, tupla, conjunto, diccionario)

¿Cúando usar “while” o “for” ?
- while: cuando no conozcas la cantidad de elementos a recorrer o la cantidad de iteraciones a realizar.
- for: cuando conozcas la cantidad de elementos a recorrer o el número de iteraciones a realizar.
"""

for element in range(1, 20):
  print(element)

print("\n")  #Salto de línea

my_list = [23, 45, 67, 89, 43]
for i in my_list:
  print(i)

print("\n")  #Salto de línea

my_tupla = ("Ali", "García", "Palacios")
for i in my_tupla:
  print(i)

print("\n")  #Salto de línea

my_diccionary = {
  'novios': ['Yoongi', 'Taeh', 'Aemond', 'Jk'],
  'hijos': 0,
  'languajes': ('Python', 'JS', 'Java')
}
# Manera 1 de tener la clave y valor
for i in my_diccionary:
  print(i, "=>", my_diccionary[i])

# Manera 2 de tener la clave y valor
for key, value in my_diccionary.items():
  print(key, "=>", value)

print("\n")  #Salto de línea

people = [       
  {
    'name': 'Angie',
    'age': 22
  },
  {
    'name': 'Juli',
    'age': 21
  },
  {
    'name': 'Wale',
    'age': 24
  }
]

for person in people:
  print(person)
  print(person['name'])
