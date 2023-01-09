#JUEGO: PIEDRA, PAPEL Y TIJERA

user_option = input("Piedra, Papel o Tijera: ").lower()
computer_option = "tijera"

if computer_option == "piedra":
  if user_option == "piedra":
    print("Empate")
  elif user_option == "papel":
    print("Ganaste")
  elif user_option == "tijera":
    print("Perdiste")
  else:
    print("Opción incorrecta")

elif computer_option == "piedra":
  if user_option == "piedra":
    print("Perdiste")
  elif user_option == "papel":
    print("Empate")
  elif user_option == "tijera":
    print("Ganaste")
  else:
    print("Opción incorrecta")

elif computer_option == "tijera":
  if user_option == "piedra":
    print("Ganaste")
  elif user_option == "papel":
    print("Perdiste")
  elif user_option == "tijera":
    print("Empate")
  else:
    print("Opción incorrecta")
