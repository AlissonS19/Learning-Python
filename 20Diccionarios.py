""" DICCIONARIOS
diccionario = {key : value}

lista -> [ ] -> Mutable
tupla -> ( ) -> Inmutable
diccionario -> { } -> formato key:value, mutable pero no admite duplicidad de keys
"""

persona1 = {"name": "Alisson" , "lastname": "García" , "age": 22}
print(persona1)

print(len(persona1))  #Para saber cuantos elementos tenemos en el diccionario

print(persona1['age']) # Opción 1 para obtner un valor
print(persona1['name']) 
print(persona1.get('lastname')) # Opción 2 para obtener un valor (Better)

print('lastname' in persona1) # Verifica si el elemento está dentro de


# ---- INSERCIÓN Y ACTUALIZACIÓN

persona2 = {
  "name" : "Alisson",
  "lastname" : "García",
  "age" : 22,
  "langs" : ["Python", "JS"], 
  "Idioms" : ["Espanish", "English", "Italian"]
}

print("PERSONA 2 =>", persona2)
persona2['name'] = 'Ali' 

persona2['langs'].append('Java') # Agregar un valor a la lista

del persona2['lastname'] #Como eliminar un elemento (Manera 1)
persona2.pop('age')      #Como eliminar un elemento (Manera 2)
print(persona2)

print("-----------------")

print(persona2.items())
print(persona2.keys())
print(persona2.values())


persona2['age'] = 22   #Agregar un nuevo elemento clave, valor
print(persona2)