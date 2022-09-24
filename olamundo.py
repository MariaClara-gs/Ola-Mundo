import sys
from playsound import playsound
from random import randint
numeros = []
n = randint(0,10)
sair = ''


print ("\n\033[1;35mOlá, Mundo!\033[m")

while sair != 's':
     
  if n in numeros:
    if len(numeros) == 11:
      sys.exit("\n\033[1;31mAcabaram as músicas :P\033[m")
    else:
      n = randint(0,10)
   

  else:   
    if n == 0:
      numeros.append(n)
      print("\n\033[1;36mTocando: Close To You\033[m")
      playsound('close.mp3')
      
      
    if n == 1:
      numeros.append(n)
      print("\n\033[1;36mTocando: Honey\033[m")
      playsound('honey.mp3')
      

    if n == 2:
      numeros.append(n)
      print("\n\033[1;36mTocando: 7 Rings\033[m")
      playsound('7-rings.mp3')
     

    if n == 3:
      numeros.append(n)
      print("\n\033[1;36mTocando: Death Bed\033[m")
      playsound('powfu.mp3')
      

    if n == 4:
      numeros.append(n)
      print("\n\033[1;36mTocando: Phobia\033[m")
      playsound('phobia.mp3')
      

    if n == 5:
      numeros.append(n)
      print("\n\033[1;36mTocando: I Love You Boy\033[m")
      playsound('i.mp3')
      
    
    if n == 6:
      numeros.append(n)
      print("\n\033[1;36mTocando: Dream in a Dream\033[m")
      playsound('dream.mp3')
      

    if n == 7:
      numeros.append(n)
      print("\n\033[1;36mTocando: Shower\033[m")
      playsound('shower.mp3')
      

    if n == 8:
      numeros.append(n)
      print("\n\033[1;36mTocando: Lovers\033[m")
      playsound('lovers.mp3')
      

    if n == 9:
      numeros.append(n)
      print("\n\033[1;36mTocando: The Ocean\033[m")
      playsound('theocean.mp3')


    if n == 10:
      numeros.append(n)
      print("\n\033[1;36mTocando: Dimple\033[m")
      playsound('dimple.mp3')

    sair = input(str("\n\033[1;36mDeseja sair?\n Pressione S para sair ou O para continuar."))
    n = randint(0,10)

   



    
    
    
    

    