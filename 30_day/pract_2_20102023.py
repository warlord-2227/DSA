"""
Write a program that can compute a factiorial of a given numbers. The result should be printed in a comma seperated sequence on a single line.
"""
num = input("Enter Integer for factorial:")
if num.isdigit():
    num = int(num)
else:
    print("You should enter number")
    num = 8 

#How to kill program



def get_factorial(n):
    if n == 0:
        return 1
    else:
        return n*get_factorial(n-1)

print(get_factorial(num))
