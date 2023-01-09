""" WHILE
while True:
  print("Se ejecuta")
Si lo dejamos así, entonces se va a ejecutar hasta el infinito
"""

contador = 0

while contador < 10:
  # contador += 1  (Si va aquí entonces se mostrará hasta el 10)
  print(contador)
  contador += 1


print("\n") # Salto de línea


# EJEMPLO 2: Tabla del 7
counter = 0
num_tabla = int(input("Ingresa el número que quieres multiplicar: "))

while counter < 10:
  counter += 1
  print(f'{num_tabla} * {counter} = {num_tabla*counter}')


print("\n") # Salto de línea


""" BREAK """
i = 0

while i < 20:
  print(i)
  i += 1
  if i == 15:
    break


print("\n") # Salto de línea


""" CONTINUE """
while i < 20:
  i += 1
  if i < 17:
    continue
  print(i)
