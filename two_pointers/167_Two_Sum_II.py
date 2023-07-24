#!/usr/bin/python3
# coding=UTF-8

import os 
import sys 
from typing import List

#All the numbers in input are sorted 
#this program only covers possibler outputs if the output is not possible then those exist scenario's aren't covered in this program
def two_sum(numbers:List[int],target:int)->List[int]:
    lptr = 0 
    rptr = len(numbers)-1
    value = numbers[lptr]+numbers[rptr]
    
    while (lptr<rptr) and (target!=value):
        if value > target :
            value -= numbers[rptr]
            rptr -= 1
            value += numbers[rptr]
        else:
            value -= numbers[lptr]
            lptr += 1
            value += numbers[lptr]

    return [lptr+1,rptr+1]

#Base test case 
numbers = [2,7,11,13,15,21]
target = 17
print(numbers,target)
print(two_sum(numbers,target))
    
