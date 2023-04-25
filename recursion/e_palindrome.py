#! /usr/bin/python3
import os 
import sys 

def palindrome(x:int)->bool:
    s = str(x)
    if len(s) <= 1:
        return True
    else:
        return s[0]==s[-1] and palindrome(s[1:-1])


print(palindrome(sys.argv[1]))

