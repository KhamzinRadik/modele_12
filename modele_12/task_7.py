# -*- coding: cp1251 -*-
import random
import math
from random import randint

def rock_paper_scissors():
   
   
   while True:
    otvet_cup=randint(1,3)
    if otvet_cup==1:
           cup='������'
    if otvet_cup==2:
           cup='�������'
    if otvet_cup==2:
           cup='������'
    
    hed=input("������� ������ ������� ��� ������ :")
    print('cup:',cup,'plauer',hed)
    if hed=='������' and cup=='������' :
        print ('you WIN')
        
    if hed=='������' and cup=='�������' :
        print ('you LOOOSS')
        
    if hed=='�������' and cup=='������' :
        print('you LOOOSS')
        
    if hed=='�������' and cup=='������' :
        print('you WIN')
        
    if hed=='������' and cup=='������' :
        print('you LOOOSS')
        
    if hed=='������' and cup=='�������' :
        print('you WIN')
    if hed=='0':
        break   
    

  # ����� ����� ���� �������, �������, ������

def guess_the_number():
  
 
    attempts = 1
    Var1 = randint(1,100)
    print ("�������� ����� �� 1 �� 99")
    Var2 = int(input("��� �������? - "))
    while Var1 != Var2:
        if Var1 > Var2: print (f"����������� ����� ������ {Var2} ")
        elif Var1 < Var2: print (f"����������� ����� ������ {Var2} ")
        attempts += 1
        Var2 = int(input("��� �������? - "))
    print (f"�� ������� ����� {Var1} �� {attempts} ������� ")

def mainMenu(otvet):
  otvet=int(input('�������� ���� 1 �������, �������, ������, 2 ������ �����'))
  return otvet

otvet=0
otvet=mainMenu(otvet)
if otvet==1:
    rock_paper_scissors()
if otvet==2:
    guess_the_number()
    