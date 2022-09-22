from playsound import playsound
from random import randint
numeros = []
n = randint(0,10)
sair = 'a'
#***irei adaptá-lo para perguntar se a pessoa deseja escutar as músicas aleatóriamente ou se deseja que o programa pergunte a cada música se ela deseja sair.***
#***Tentar adaptar para que a pessoa escolha as músicas e monte uma playlist com 5 músicas.(Perguntar se a pessoa quer que pergunte se ela deseja ouvir a música ou não.)

print ("Olá, Mundo!")

while sair != 's':

  if n in numeros:
     n = randint(0,10)

  else:   
    if n == 0:
      numeros.append(n)
      print("\nTocando: Come To Me")
      playsound('cometome.mp3')
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
      print("\nTocando: Death Bed")
      playsound('deathbed.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)
      numeros.append(n)

    if n == 3:
      numeros.append(n)
      print("\nTocando: I Love You Boy")
      playsound('iloveyouboy.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)
      numeros.append(n)

    if n == 4:
      numeros.append(n)
      print("\nTocando: Rosyln")
      playsound('rosyln.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)
      numeros.append(n)
    
    if n == 5:
      numeros.append(n)
      print("\nTocando: Close to you")
      playsound('closetoyou.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)
      numeros.append(n)

    if n == 6:
      numeros.append(n)
      print("\nTocando: Say something")
      playsound('saysomething.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)

    if n == 7:
      numeros.append(n)
      print("\nTocando: Lovers ")
      playsound('lovers.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)  

    if n == 8:
      numeros.append(n)
      print("\nTocando: The Ocean")
      playsound('theocean.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)
      numeros.append(n)

    if n == 9:
      numeros.append(n)
      print("\nTocando: War of Hearts")
      playsound('warofhearts.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)
      numeros.append(n)
    
    if n == 8:
      numeros.append(n)
      print("\nTocando: She's Crazy But She's Mine")
      playsound('shes-crazy-but-shes-mine.mp3')
      sair = str(input("\nSair?\n*Precione S para sair*"))
      n = randint(0,10)
      numeros.append(n)
    
    

    