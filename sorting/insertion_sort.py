#!/usr/bin/python3
# coding=UTF-8

import os 
import sys 

a = [12,11,13,5,6]
#write an algo for insertion sort

def sort_insertion(a):

    #since 1st elements can't have previous elements got from 1
    for i in range(1,len(a)):
        key = a[i]
        j = i-1
        while j>=0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

    return a 

print("This is the file name",sys.argv[0])
print("This is the input given for insertion sort",sys.argv[1:])
try:
    numbers = [float(arg) for arg in sys.argv[1:]]
except Exception as e:
    print("Wrong data type in input",e)
    a = [4,3,2,10,12,1,5,6]
    print("By default we are taking this as numput",a)
    numbers = a

print(sort_insertion(numbers))
