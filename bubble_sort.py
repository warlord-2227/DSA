import os
import sys 


a = [64, 25, 12, 22, 11]
flag_sort = True

while flag_sort:
    flag_sort = False
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            #temp = a[i]
            #a[i] = a[i+1]
            #a[i+1] = temp
            a[i],a[i+1] = a[i+1],a[i]
            flag_sort = True
print(a)



