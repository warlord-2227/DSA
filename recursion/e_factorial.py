#!/usr/bin/python3
#shebang for interpreter 

import os 
import sys
import argparse

parser = argparse.ArgumentParser(description="Factorial program")
#Add an argument to parser 
parser.add_argument("--number",type=int,help="factorial number")
args = parser.parse_args()
def factorial(n:int)->int:
    if n==0 or n==1 : 
        return 1
    else:
        return n * factorial(n-1)



#You can use following block as well 
#print(factorial(int(sys.argc[1])))
if args.number:
    print(factorial(args.number))
else:
    print(factorial(5))

