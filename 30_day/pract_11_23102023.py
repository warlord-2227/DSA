"""
Write a program that takes input as comma seperated 4 digit binary numbers and then check whether they are divisible by 5 or not. Numbers that are divisible by 5 are to be printed in comma seperated sequence 
"""
#TODO filter all the integer case
inp = input ("Enter comma seperated binary numbers:").split(",")
nums = []
for num in inp:
    if num.isdigit() and len(num)==4:
        nums.append(num)

answer = []
for i in nums:
    if int(i,2)%5==0:
        answer.append(i)

out = ",".join(answer)
print(out)

