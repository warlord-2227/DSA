"""
Write a program that calculate and prints the value according to the given formula 
q = ((2*c*d)/h)**0.5
d is list of numbers 
"""
import math
nums = input("Enter numbers:").split(",")
print(nums)
answer = []
c,h = 50,30
for i in range(len(nums)):
    q = math.sqrt((2*c*int(nums[i]))/h)
    answer.append(int(q))

print(answer)

