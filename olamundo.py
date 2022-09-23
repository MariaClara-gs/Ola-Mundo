from playsound import playsound
from random import randint
numeros = []
n = randint(0,10)
sair = ''
#***irei adaptá-lo para perguntar se a pessoa deseja escutar as músicas aleatóriamente ou se deseja que o programa pergunte a cada música se ela deseja sair.***
#***Tentar adaptar para que a pessoa escolha as músicas e monte uma playlist com 5 músicas.(Perguntar se a pessoa quer que pergunte se ela deseja ouvir a música ou não.)

print ("Olá, Mundo!")

while sair != 's':
     
  if n in numeros:
    if len(numeros) == 11:
      print('')
    else:
       n = randint(0,10)
   

  else:   
    if n == 0:
      numeros.append(n)
      print("\nTocando: Close To You")
      playsound('close.mp3')
      
      
    if n == 1:
      numeros.append(n)
      print("\nTocando: Honey")
      playsound('honey.mp3')
      

    if n == 2:
      numeros.append(n)
      print("\nTocando: 7 Rings")
      playsound('7-rings.mp3')
     

    if n == 3:
      numeros.append(n)
      print("\nTocando: Death Bed")
      playsound('powfu.mp3')
      

    if n == 4:
      numeros.append(n)
      print("\nTocando: Phobia")
      playsound('phobia.mp3')
      

    if n == 5:
      numeros.append(n)
      print("\nTocando: Love Shot")
      playsound('loveshot.mp3')
      
    
    if n == 6:
      numeros.append(n)
      print("\nTocando: Dream in a Dream ")
      playsound('dream.mp3')
      

    if n == 7:
      numeros.append(n)
      print("\nTocando: Shower")
      playsound('shower.mp3')
      

    if n == 8:
      numeros.append(n)
      print("\nTocando: Lovers ")
      playsound('lovers.mp3')
      

    if n == 9:
      numeros.append(n)
      print("\nTocando: The Ocean")
      playsound('theocean.mp3')


    if n == 10:
      numeros.append(n)
      print("\nTocando: Dimple")
      playsound('dimple.mp3')

  sair = input(str("\n Deseja sair?\n Pressione S para sair ou O para continuar."))
  n = randint(0,10)

   



    
    
    
    

    