"""
  1  2  3  4  5  6  7  8  9  10
  H  O  L  A     M  U  N  D  O
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
"""

text = "Ella es programadora"

print(text[0]) #Para mostrar la primera posición del String
print(text[1]) #Para mostrar la segunda posición del String

'''Muestra la última letra del String'''
#Opción 1 :
print (text[len(text)-1])

#Opción 2 : LISTA [inicio:fin:salto]
print(text[-1])

print(text[0:4]) #Ella
print(text[0:6]) #Ella e
print(text[0:9]) #Ella es p
print(text[5:]) #es programadora
print(text[-3]) 
print(text[:]) #Ella es programadora
print(text[0:10:2]) 
print(text[: :2])