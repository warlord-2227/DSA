"""
Use list comprehension to square each odd numbers in the list. The list is input by a sequence of comma seperated numbers
"""
inp = input("Enter comma seperated list of digits:").split(",")
nums = []
for i in inp:
    if i.isdigit():
        nums.append(int(i))

condition = [str(i**2) for i in nums if i%2!=0]
out = ",".join(condition)
print(out)
