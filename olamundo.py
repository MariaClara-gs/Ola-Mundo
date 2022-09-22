from playsound import playsound
from random import randint
numeros = list()
n = randint(0,10)
sair = 'a'
#***irei adaptá-lo para perguntar se a pessoa deseja escutar as músicas aleatóriamente ou se deseja que o programa pergunte a cada música se ela deseja sair.***
#***Tentar adaptar para que a pessoa escolha as músicas e monte uma playlist com 5 músicas.(Perguntar se a pessoa quer que pergunte se ela deseja ouvir a música ou não.)

print ("Olá, Mundo!")

while sair != 's':

  while n not in numeros:
    if n == 0:
      numeros.append(n)
      print("\nTocando: Come Through")
      playsound('come-through.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0, 10)
      numeros.append(n)

    if n == 1:
      numeros.append(n)
      print("\nTocando: Honey")
      playsound('honey.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)
      numeros.append(n)

    if n == 2:
      numeros.append(n)
      print("\nTocando: 7 Rings")
      playsound('7-rings.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)
      numeros.append(n)

    if n == 2:
      numeros.append(n)
      print("\nTocando: 2002")
      playsound('2002.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)
      numeros.append(n)

    if n == 3:
      numeros.append(n)
      print("\nTocando: 대취타")
      playsound('Agust D.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)
      numeros.append(n)

    if n == 4:
      numeros.append(n)
      print("\nTocando: Almost Forgot")
      playsound('Almost-Forgot.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)
      numeros.append(n)
    
    if n == 5:
      numeros.append(n)
      print("\nTocando: Close to you")
      playsound('close-to-you.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)
      numeros.append(n)

    if n == 6:
      numeros.append(n)
      print("\nTocando: Flower Shower")
      playsound('FLOWER-SHOWER.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)

    if n == 7:
      numeros.append(n)
      print("\nTocando: Lovers ")
      playsound('Lovers.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)  

    if n == 8:
      numeros.append(n)
      print("\nTocando: Never Ending Story")
      playsound('Never-ending-story.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)
    
    if n == 9:
      numeros.append(n)
      print("\nTocando: On The Rocks")
      playsound('ON THE ROCKS.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)

    if n == 10:
      numeros.append(n)
      print("\nTocando: On The Rocks")
      playsound('Shes-Crazy-But-Shes-Mine.mp3.')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)


    