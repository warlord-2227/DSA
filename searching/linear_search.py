#!/usr/bin/python3
# coding=UTF-8
import os 
import sys 
a=[12,34,5,2,34]

def linear_search(arr,anchor):
    for i in range(len(arr)):
        if arr[i]==anchor:
            return i
    return -1
a = [4,3,2,10,12,1,5,6]
print("This is file name",sys.argv[0])
print(f"Input for this search array {sys.argv[1:-1]} and anchor {sys.argv[-1]} are")
print(linear_search(sys.argv[1:-1],sys.argv[-1]))

