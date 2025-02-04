import random

ganadas = 0
perdidas = 0 
empates = 0 
jugar = True

while (jugar): 
  print('Tus resultados fueron: Ganadas: '+str(ganadas)+" Perdidas: "+str(perdidas)+" Empates: "+str(empates))
  try: 
    player = int(input('1)piedra, 2)papel o 3)tijeras: '))
  except ValueError:
    print('Porfavor introduzca un numero') 

    continue
  computer = random.randint(1, 3)

  match player: 
    case 1: 
      match computer:
        case 2:
          print('Perdiste! piedra es envuelto por papel')
          perdidas += 1
        case 3: 
          print('Ganaste! Piedra destroza tijera')
          ganadas += 1
        case _:
          print('Empate! Los dos usan piedra')
          empates += 1
    case 2: 
      match computer:
        case 3:
          print('Perdiste! papel es cortado por tijera')
          perdidas += 1
        case 1: 
          print('Ganaste! papel envuelve piedra')
          ganadas += 1
        case _:
          print('Empate! Los dos usan papel')
          empates += 1
    case 3: 
      match computer:
        case 1:
          print('Perdiste! tijeras son destrozadas por piedra')
          perdidas += 1
        case 2: 
          print('Ganaste! tijeras cortan papel')
          ganadas += 1
        case _:
          print('Empate! Los dos usan tijeras')
          empates += 1

  player = input('Quieres seguir jugando?') 
  respuesta = player.upper().strip()

  if respuesta == 'NO': 
    print('Pues adios')
    jugar= False
  else:
    print('Pues continuemos!')
