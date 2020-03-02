# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 18:03:43 2020

@author: Raghav
"""
import getpass
a1 = {'rock':0,'paper':1,'scissors':2}
b1 = {'rock':0,'paper':1,'scissors':2}
while(1):    
    a = getpass.getpass("enter rock,paper or scissors :\n")
    b = getpass.getpass("enter rock,paper or scissors :\n")    
    a=a.lower()
    b=b.lower()
    ch1 = a1[a]
    ch2 = b1[b]
    if(ch1 == ch2):
        print('draw')
    elif(ch1==0 and ch2==1):
        print('player 2 wins')
    elif(ch1==0 and ch2 == 2):
        print('player 1 wins')
    elif(ch1==1 and ch2 == 0):
        print('player 1 wins')
    elif(ch1==1 and ch2 == 2):
        print('player 2 wins')
    elif(ch1==2 and ch2 == 0):
        print('player 2 wins')
    elif(ch1==2 and ch2 == 1):
        print('player 1 wins')
    y=input('do you want to play more "y" or "n"')
    y=y.lower()
    if(y == 'n'):
        break
    else:
        continue