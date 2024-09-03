# -*- coding: cp1251 -*-

def rock_paper_scissors():
   cup="камень"
   while True:
    
    hed=input("введите камень ножнецы или бумагу")
    print('cup',cup,'plauer',hed)
    if hed=='бумага':
        print ('you WIN')
        break
    if hed=='ножнецы':
        print('you LOOOSS')
        break

  # Здесь будет игра «Камень, ножницы, бумага»

def guess_the_number():
  chislo = 5
  plauer_chislo=int(input('угодайте число')

def mainMenu(otvet):
  otvet=int(input('выберете игру 1 «Камень, ножницы, бумага», 2 Угадай число'))
  return otvet

otvet=0
otvet=mainMenu(otvet)
if otvet==1:
    rock_paper_scissors()
    