if True:
  print("Debería ejecutarse")

if False:
  print("Debería ejecutarse")

#EJEMPLO 1
mascota = input("¿Cual es tu mascota favorita?: ")

if mascota == "perro" or mascota == "Perro":
  print("Genial, tienes buen gusto")
elif mascota == "gato" or mascota == "Gato":
  print("Suerte con esos seres malvados")
else:
  print("Eso es genial")

#EJEMPLO 2
stock = int(input("Ingresa el número de stock: "))
if stock >= 100 and stock <= 1000:
  print("El stock es correcto")
else:
  print("El stock es incorrecto")


#EJEMPLO 3
num = int (input("Ingresa un número: "))
if num % 2 == 0: 
  print("Es par")
else:
  print("Es impar")