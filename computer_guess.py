# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 19:23:48 2021

@author: JENI
"""

import random

print('Welcome to Computer Guess Game!!!!')


def guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
          guess = random.randint(low, high)
        else:
          guess =  high
        feedback = input(f'Is {guess} too high(H)? or too low(L)? or correct(C)?\n').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1 
        elif feedback == 'c':
            print('you guessed the number correctly yayyyy!!!')    
        else:
            print('please enter either l for Low,or h for High, or c for correct!!')
        
        
guess(10)



