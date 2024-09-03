# -*- coding: cp1251 -*-
import os


def test ():
    nam=int(input('\n\n\n\t\t\tвведите число :'))
    
    if nam>0:
        positive()
    else:
        negative()



def positive():
    
    print ('\n\n\n\t\t\tПоложительное')

def negative():
    
    print ('\n\n\n\t\t\tОтрицательное')


while True:
 test()
 