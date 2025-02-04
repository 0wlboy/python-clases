import random

randomNumber = random.randint(1, 100)

intentos = 0  

while intentos < 5:  
    try:
        userNumber = int(input("Adivina el número entre 1 y 100: "))
    except ValueError:
        print("Entrada inválida. Debes ingresar un número entero.")
        continue

    intentos += 1 

    if userNumber == randomNumber:
        print("¡Felicidades! Adivinaste el número.")
        break  
    elif userNumber < randomNumber:
        print("El número es mayor. Piensa un poco mas grande!")
    else:
        print("El número es menor. Piensa un poco mas pequeño!")

if intentos == 5 and userNumber != randomNumber: 
    print("¡Lo siento! Perdiste. El número era: ", randomNumber)