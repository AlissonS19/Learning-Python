#JUEGO: PIEDRA, PAPEL Y TIJERA

user_option = input("Piedra, Papel o Tijera: ")
computer_option = "Tijera"

if computer_option == "Piedra":
  if user_option == "Piedra" or user_option == "piedra":
    print("Empate")
  elif user_option == "Papel" or user_option == "papel":
    print("Ganaste")
  elif user_option == "Tijera" or user_option == "tijera":
    print("Perdiste")
  else:
    print("Opción incorrecta")

elif computer_option == "Papel":
  if user_option == "Piedra" or user_option == "piedra":
    print("Perdiste")
  elif user_option == "Papel" or user_option == "papel":
    print("Empate")
  elif user_option == "Tijera" or user_option == "tijera":
    print("Ganaste")
  else:
    print("Opción incorrecta")

elif computer_option == "Tijera":
  if user_option == "Piedra" or user_option == "piedra":
    print("Ganaste")
  elif user_option == "Papel" or user_option == "papel":
    print("Perdiste")
  elif user_option == "Tijera" or user_option == "tijera":
    print("Empate")
  else:
    print("Opción incorrecta")
