# -*- coding: cp1251 -*-

def rock_paper_scissors():
   cup="������"
   while True:
    
    hed=input("������� ������ ������� ��� ������")
    print('cup',cup,'plauer',hed)
    if hed=='������':
        print ('you WIN')
        break
    if hed=='�������':
        print('you LOOOSS')
        break

  # ����� ����� ���� �������, �������, ������

def guess_the_number():
  chislo = 5
  plauer_chislo=int(input('�������� �����')

def mainMenu(otvet):
  otvet=int(input('�������� ���� 1 �������, �������, ������, 2 ������ �����'))
  return otvet

otvet=0
otvet=mainMenu(otvet)
if otvet==1:
    rock_paper_scissors()
    