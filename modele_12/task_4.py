# -*- coding: cp1251 -*-

def flip_over (a):
 str_a=str(a)
 a=str(a)
 count=len(str(a))
 a=''
 for i in range (count-1,-1,-1):  
     a+=str_a[i]
 a=int(a)
 return a


while True:
 namber=int(input('введите число : '))
 if namber==0:  
  break
      
 else:
  print (flip_over(namber))
      

