""" TRANSFORMACIONES DE TIPO DE DATO """
name = "Alisson"
age = 22
single = True

#Manera 1
print("Hi, I'm " + name + ", I have " + str(age) +
      " and Am I single?, well.." + str(single))

age2 = input("Ingresa tu proxima edad: ")
print(type(age2))

age3 = int(age2)
print(type(age3))

nota1 = int(input("Ingresa tu nota general: "))
print(type(nota1))

#Manera 2
print(f"My age is {age}")
