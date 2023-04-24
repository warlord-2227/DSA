import os 
import sys 

a = [64, 25, 12, 22, 11]

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j] < a[i]:
            a[i],a[j] = a[j],a[i]
print(a)


