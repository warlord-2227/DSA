#!/usr/bin/python3
# coding=UTF-8

import os 
import sys 

#a = [2,3,4,10,40]
a=[1,4,5,6,10,12,54,68,71,100]
#a =[1]
#write an algorithm to get element from an sorted array in optimized way 
def binary_search(a,start,end,anchor):
    if end>=start:
        mid = start + ((end-start)//2)
        #print(mid,start,end)
        if a[mid]==anchor:
            return mid 
        elif a[mid]<anchor:
           return  binary_search(a,mid+1,end,anchor)
        else:
           return  binary_search(a,start,mid-1,anchor)
    #If no solution found then exit with -1
    else:
        return -1

#anchor = 10
anchor = 71
#anchor = 10
#print(len(a),a)
print(binary_search(a,0,len(a)-1,anchor))
