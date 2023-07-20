#TODO add shebang and auther's name here
import os 
import sys 

a = [12,9,8,7,6]
#Write bubble sort algorithm


def sort_array(a):
    #TODO instead of flag use something different 
    sort_flag = True
    while sort_flag:
        sort_flag = False
        for i in range(len(a)):
            if i != len(a)-1:
                if a[i] > a[i+1]:
                    #TODO write even swapping algorithm for it 
                    a[i],a[i+1] = a[i+1],a[i]
                    sort_flag = True
    
    return a


print("This is the file name",sys.argv[0])
print("This is the arguments in list",sys.argv[1:])
try:
    numbers = [float(arg) for arg in sys.argv[1:]]
except Exception as e:
    print("There is problem with input",e)
    print("By default array choosen from the list as below")
    numbers = a 
print(sort_array(numbers))
