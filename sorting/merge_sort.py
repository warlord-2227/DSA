#!/usr/bin/python3
# coding=UTF-8

import os 
import sys 

a = [12 ,11 ,13 ,5 ,6 ,7]
def sort_merge(a):
    if len(a) >1 :
        mid = len(a)//2
        L = a[:mid]
        R =a[mid:]
        #Divide till we don't reach the single elements 
        sort_merge(L)
        sort_merge(R)

        i=j=k=0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k +=1 
        #check remining list's element to be added 
        while i < len(L):
            a[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            a[k] = R[j]
            j+=1
            k+=1

print("This is the file name",sys.argv[0])
print("This is the input given for merge sort",sys.argv[1:])
try:
    numbers = [float(arg) for arg in sys.argv[1:]]
except Exception as e:
    print("Wrong data type in input",e)
    a = [4,3,2,10,12,1,5,6]
    print("By default we are taking this as numput",a)
    numbers = a

sort_merge(numbers)
print(numbers)
