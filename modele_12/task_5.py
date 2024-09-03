# -*- coding: cp1251 -*-

def count_letters(string,str_point):
    count =0
    for i in range (0,len(string)):
        if str_point==string[i]:
            count +=1
    return count

string='100 лет в обед'
str_int=input('введите цифру :')
str_str=input('введите символ :')

print(count_letters(string,str_int))
print(count_letters(string,str_str))
