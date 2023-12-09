
import math
import os
import random
import re
import sys
from tracemalloc import stop

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(stop_t: int):
    valor_inicial=3
    valor_retornado=3
    if (stop_t>=1 and stop_t<=10**12):
        for time in range(1,stop_t):
            if valor_inicial==1:
                valor_retornado=valor_retornado*2
                valor_inicial=valor_retornado
            else:
                valor_inicial=valor_inicial-1
           
        return valor_inicial
    else:
        pass

    
    
    
        
            

if __name__ == '__main__':
    print(strangeCounter(21))