# -*- coding: cp1251 -*-
import random
import math
from random import randint

def rock_paper_scissors():
   
   
   while True:
    otvet_cup=randint(1,3)
    if otvet_cup==1:
           cup='камень'
    if otvet_cup==2:
           cup='ножнецы'
    if otvet_cup==2:
           cup='бумагу'
    
    hed=input("введите камень ножнецы или бумагу :")
    print('cup:',cup,'plauer',hed)
    if hed=='бумага' and cup=='камень' :
        print ('you WIN')
        
    if hed=='бумага' and cup=='ножнецы' :
        print ('you LOOOSS')
        
    if hed=='ножнецы' and cup=='камень' :
        print('you LOOOSS')
        
    if hed=='ножнецы' and cup=='бумага' :
        print('you WIN')
        
    if hed=='камень' and cup=='бумага' :
        print('you LOOOSS')
        
    if hed=='камень' and cup=='ножнецы' :
        print('you WIN')
    if hed=='0':
        break   
    

  # Здесь будет игра «Камень, ножницы, бумага»

def guess_the_number():
  
 
    attempts = 1
    Var1 = randint(1,100)
    print ("Загадано число от 1 до 99")
    Var2 = int(input("Ваш вариант? - "))
    while Var1 != Var2:
        if Var1 > Var2: print (f"Угадываемое число больше {Var2} ")
        elif Var1 < Var2: print (f"Угадываемое число меньше {Var2} ")
        attempts += 1
        Var2 = int(input("Ваш вариант? - "))
    print (f"Вы угадали число {Var1} за {attempts} попыток ")

def mainMenu(otvet):
  otvet=int(input('выберете игру 1 «Камень, ножницы, бумага», 2 Угадай число'))
  return otvet

otvet=0
otvet=mainMenu(otvet)
if otvet==1:
    rock_paper_scissors()
if otvet==2:
    guess_the_number()
    