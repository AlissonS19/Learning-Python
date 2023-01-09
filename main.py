""" PROYECTO FINAL: PIEDRA PAPEL O TIJERA """
import random

print("Bienvenido jugador \n")

opciones = ('piedra', 'papel', 'tijera')
contador = 0
win = 0
lose = 0

while contador < 20:
  option_user = input("¿Piedra, papel o tijera? => ").lower()
  contador += 1
  option_computer = random.choice(opciones)
  print('El computador eligió : ', option_computer)

  if option_computer == 'piedra':
    if option_user == 'piedra':
      print('Empate \n')
    elif option_user == 'papel':
      print('Ganaste! \n')
      win += 1
    elif option_user == 'tijera':
      print('Perdiste \n')
      lose += 1

  elif option_computer == 'papel':
    if option_user == 'piedra':
      print('Perdiste \n')
      lose += 1
    elif option_user == 'papel':
      print('Empate! \n')
    elif option_user == 'tijera':
      print('Ganaste! \n')
      win += 1

  elif option_computer == 'tijera':
    if option_user == 'piedra':
      print('Ganaste! \n')
      win += 1
    elif option_user == 'papel':
      print('Perdiste \n')
      lose += 1
    elif option_user == 'tijera':
      print('Empate! \n')

  if win == 4 and lose < win:
    print('\n ACABAS DE GANAR LA PARTIDA')
    break
