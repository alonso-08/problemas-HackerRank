#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#
def invertir_numero(original_number):
    copy_number = original_number
    reversed_number = 0
    while original_number > 0:
        remainder = original_number % 10
        reversed_number = reversed_number * 10 + remainder
        original_number = original_number // 10
    if (copy_number == reversed_number):
        #print(copy_number, 'is a palindrome number')
        return reversed_number
    else:
        #print(copy_number, 'is not a palindrome number')
        return reversed_number

def beautifulDays(i, j, k):
    
    numero_normal=0
    numero_invertido=0
    divisor=k
    cantidad_numeros_hermosos=0
    if (i>=1 and i<=2000000) and (j>=1 and j<=2000000)and (k>=1 and k<=2000000000):

        for num in range(i,j+1):            
            
            numero_normal=num
            numero_invertido=invertir_numero(numero_normal)  
            nume=10
               
            diferencia=numero_normal-numero_invertido
            
            resultado_divicion=diferencia%divisor
            
            
            if(resultado_divicion==0):
                cantidad_numeros_hermosos=cantidad_numeros_hermosos+1
            else:
                pass
          
        
        return cantidad_numeros_hermosos
    else:
        pass

if __name__ == '__main__':
    print(beautifulDays(1,2000000,1000000000))