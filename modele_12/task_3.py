# -*- coding: cp1251 -*-


def summ (a):
    str_summ=str(a)
    coumt =int(len(str_summ))
    summ=0
    for i in range (0,coumt,1):
        summ+=int(str_summ[i])
    return summ

def maximum(a):
    max=0
    a=str(a)
    count = int(len(a))
    
    for i in range (0,count,1):
       
        if max<int(a[i]):
           max=int(a[i])
    
    return max

def minimum (a):
    
    a=str(a)
    count = int(len(a))
    min=int(a[0])
    for i in range (0,count,1):
        if min>int(a[i]):
           min=int(a[i])
    return min

while (True):
    nambrt_1=int(input('������� 2 ����� '))
  
    

    otvet=int(input ('������� 1 ���� �� ������ ������� �����, 2 ���� ������ ������ ���������� �� 2� �����, 3 ���� ����������� �� 2� ����� ��� 0 ��� ������'))
    
    while(otvet<0 or otvet >3):
        if otvet!=0:
            otvet=input ("������ �� ���������� ����� ���������� ��� ���")
        if otvet==0:
            False
    if otvet==1:
        print (summ (nambrt_1))
    if otvet==2:
        print (maximum(nambrt_1))
    if otvet==3:
        print (minimum(nambrt_1))

