#!/bin/python3

from itertools import accumulate
import math
import os
from pickletools import read_uint1
import random
import re
import sys
import  math
#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def round_down(n, decimals=0): 
    multiplier = 10 ** decimals 
    return math.floor(n * multiplier) / multiplier 
  

def viralAdvertising(n):
    personas=5
    contador_dias=1
    shared=0
    liked=0
    cumulative=0
    while contador_dias<=n:
        if contador_dias==1:
            shared=personas
            liked=round_down(personas/2)
            cumulative=round_down(cumulative)+(liked)
            contador_dias+=1
        else:
            shared=liked*3
            liked=round_down(shared/2)
            cumulative=round_down(cumulative)+(liked)
            
            contador_dias+=1
        
    
    
    return int(cumulative)

if __name__ == '__main__':
    print(viralAdvertising(5))