from playsound import playsound
from random import randint
n = 0
n = randint(1,2)
sair = 'a'

print ("Olá, Mundo!")

while sair != 's':
 if n == 1:
   print("Tocando: LION")
   playsound('LION.mp3')
   sair = str(input("Sair?"))
   n = 0
   n = randint(1,2)
 if n == 2:
   print("Tocando: 2011")
   playsound('2011.mp3')
   sair = str(input("Sair?\n*s = sair"))
   n = 0
   n = randint(1,2)
