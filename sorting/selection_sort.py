#!/usr/bin/python3
# coding=UTF-8

import os 
import sys 

a = [64,25,12,22,11]

#write selection sort algorithm
def sort_selection(a):
    for i in range(len(a)):
        #TODO if condition is really needed? 
        if i<len(a)-1:
            for j in range(i+1,len(a)):
                local_min = j
                if a[j] < local_min:
                    local_min = j
            if a[i] > a[j]:
                a[i],a[j] = a[j],a[i]
    return a

print("This is the file name",sys.argv[0])
print("This is the input arguments",sys.argv[1:])
try:
    numbers = [float(arg) for arg in sys.argv[1:]]
except Exception as e:
    print("There is a different data type format for arguments",e)
    print("Due to this error we are by default sending this as a input for the function",a)
    numbers = a 
print(sort_selection(numbers))
    



