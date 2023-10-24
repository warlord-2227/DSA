"""
Write a program that accepts a sentence and calculate number of upper case and lower case letters 
"""
inp = input("Enter sentence: ")
lower = 0
upper = 0 
for char in inp:
    val = ord(char)
    if val >= 65 and val <=90:
        upper +=1 
    elif val >=97 and val <=122:
        lower += 1 

print("LOWER",lower)
print("UPPER",upper)

