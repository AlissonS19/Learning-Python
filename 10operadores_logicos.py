#AND
print("True and True: ", True and True)
print("False and False: ", False and False)
print("True and False: ", True and False)
print(10 > 4 and 7 > 3)
print(10 > 4 and 7 > 8)

stock = int(input ("Ingresa el número de productos: "))
print(stock >= 5 and stock <= 200)


#OR
print("True or True: ", True or True)
print("False or False: ", False or False)
print("True or False: ", True or False)
print(10 > 4 or 7 > 3)
print(10 > 4 or 7 > 8)
print(2 > 4 or 5 > 8)

role = input("Ingrese su rol: ")
print (role == 'admin' or role == "seller")


#NOT
print(not True)
print(not False)

# and
print('NOT AND')
print('not True and True =>', not (True and True))
print('not True and False =>', not (True and False))
print('not False and True =>', not (False and True))
print('not False and False =>', not (False and False))

stock = input('Ingrese el numero de stock => ')
stock = int(stock)

print(not (stock >= 100 and stock <= 1000))