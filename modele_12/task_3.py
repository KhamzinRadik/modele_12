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
    nambrt_1=int(input('введите 2 числа '))
  
    

    otvet=int(input ('введите 1 усли вы хотите сложить цифры, 2 если хотите узнать наибольшее из 2х чисел, 3 если минимальную из 2х чисел или 0 для выхода'))
    
    while(otvet<0 or otvet >3):
        if otvet!=0:
            otvet=input ("введен не корректный ответ попробуйте еще раз")
        if otvet==0:
            False
    if otvet==1:
        print (summ (nambrt_1))
    if otvet==2:
        print (maximum(nambrt_1))
    if otvet==3:
        print (minimum(nambrt_1))

