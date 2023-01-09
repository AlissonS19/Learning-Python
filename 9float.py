x = 3.3
y = 1.1 + 2.2
print(x, y)
print(x == y)

#Opción 1 con Strings (Se crea una variable convirtiendo la y en str)
y_str = format(y, ".2g")  #El .2g es para decrle que solo quiere 2 dígitos
print(y_str)
print(y_str == str(x))

#Opción 2 más matemátco
tolerance = 0.00001
print(abs(x - y) < tolerance)

#Opción 3
y = round(1.1 + 2.2, 1)
print(x == y)
