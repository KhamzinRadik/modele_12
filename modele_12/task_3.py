# -*- coding: cp1251 -*-


def summ (a,b):
    summ=a+b
    return summ

def maximum(a,b):
    max=0
    if a>b:
        max=a
    else:
        max=b
    return max

def minimum (a,b):
    min=0
    if a<b:
        min=a
    else :
        min=b

    return min
while (True):
    nambrt_1=int(input('������� 2 ����� '))
    namber_2=int(input())
    otvet=int(input ('������� 1 ���� �� ������ ������� �����, 2 ���� ������ ������ ���������� �� 2� �����, 3 ���� ����������� �� 2� ����� ��� 0 ��� ������'))
    while(otvet<0 or otvet >3):
        if otvet!=0:
            otvet=input ("������ �� ���������� ����� ���������� ��� ���")
        if otvet==0:
            False
    if otvet==1:
        print (summ (nambrt_1,namber_2))
    if otvet==2:
        print (maximum(nambrt_1,namber_2))
    if otvet==3:
        print (minimum(nambrt_1,namber_2))

