text = "Ella sabe programar en Python"

#In : verificar si un subtexto o un caracter está dentro del String 
if "Python" in text:
  print("The word Python is in the text:", text)
elif "JS" or "js" in text:
  print("The word JS is in the text: ", text)

#Len : Evaluar el tamaño de un Strig (contando espacios)
size = len("Confianza ")
print(size)
print(len(text))

#Upper() : Para pasar todo a mayúsculas
print(text.upper())

#Lower() : Para pasar todo a minúsculas
print(text.lower())

#Count() : Contar el número de aparicienes que hace un caracter
print(text.count('a'))

#Swapcase() : Intercambia las minúsculas y mayúsculas
print(text.swapcase())

#Startswith()  : Verifica con que empieza
print(text.startswith("Ella"))

#Endswith()  : Verifica con que termina
print(text.endswith("cion"))

#Replace() : Para reemplazar
print(text.replace("Python", "Java"))

#Capitalize()  : Convertir en mayúscula la primera letra del String
text_2 = "hola, como estás"
print(text_2.capitalize())

#Title() : Para colocar la primera letra de cada palabra en mayúscula
print(text_2.title())

#Isdigit() : Verifica si es dígito
print(text_2.isdigit())
print("300".isdigit())
