# -*- coding: cp1251 -*-

def summa_n (namber):
    summ=0
    for i in range (1,namber+1):
       summ+=i
    return summ
nam=int(input (print (' введите число : ')))
print(summa_n(nam))