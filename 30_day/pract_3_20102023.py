"""
Write a program that takes an integer number as input and generates a dictionary contains {i:i*i} such that it is an integral numbers 
between 1 to n(both included). And program should print that dictionary
"""
num = input("Enter one number(should be integer):")
if num.isdigit():
    num = int(num)
else:
    print("Wrong Datatype, please enter number")
    num = 8 

def get_dict(n):
    return {i:i*i for i in range(1,n+1)}

print(get_dict(num))
