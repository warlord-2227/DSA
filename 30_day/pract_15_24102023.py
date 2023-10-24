"""
Write a program that calculates a+aa+aaa+aaaa with a given digit as the value of a 
"""
inp = input("Enter a digit:")
if  inp.isdigit():
    num = int(inp)

def get_calculation(a):
    out = a
    temp_array = []
    temp_array.append(a)

    for i in range(1,4):
        temp_array.append(a*(10**i)) 
        out += temp_array[-1]
        for j in range(i):
            out += temp_array[j]
    return out

print(get_calculation(num))

            


   

