# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 13:07:34 2021

@author: user
"""
"""
#練習


for i in range(1,100):
    if i==15:
        break
    if i%3==0:  # 可整除等於0,取餘數
        print(i,'是3的倍數')
    else:
        print(i,'不是3的倍數')
"""
#作業1  

for i in range(5,0,-1): #{5,4,3,2,1}
    for a in range(0,i):
        print('*',end='')
    print()
for i in range(1,6,1): #{1,2,3,4,5}
    for a in range(0,i):
        print('*',end='')
    print()
print('程式執行完畢') 

#作業2
#1.求使用者輸入一個範圍的整數
#求(1)4的倍數有哪些? (2)求哪些是質數(可被1及自己整除)

n=int(input('輸入2-100之間整數猜數:'))
for i in range(2,n):
    if n%i==0:
        print(n,'不是質數')
        if n%4==0:
            print(n,'是4的倍數')
            break
        break
else:
    print(n,'是質數')
print( )
        
        
#作業3     
#min=1 max=100  ans=61 guess=71 顯示1-70之間
import random
min_int=1
max_int=100
ans=random.randint(min_int,max_int)
guess=0
while ans !=guess:  #!= 不等於
    guess=int(input('輸入猜數:(%d~%d)'%(min_int,max_int)))          
    if guess>ans:
        print('猜小一點')
        print("請猜:%d~%d之間的數字:"%(min_int,guess))
        max_int=guess
    elif guess<ans:
        print('猜大一點')
        print("請猜:%d~%d之間的數字:"%(guess,max_int))
        min_int=guess
    else:
        print('猜對了')
