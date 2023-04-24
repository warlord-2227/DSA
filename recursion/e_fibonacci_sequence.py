#!/usr/bin/python3

import os 
import sys 

def fibonacci(n:int)-> int:
    if n==1:
        return 1
    elif n <= 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(int(sys.argv[1])))
